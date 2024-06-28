"""Converter methods from CSV to Trac wiki table."""
import re
from collections.abc import Iterator
from typing import Any

Row = list[Any]
Table = Iterator[Row]


class _TracSep:
    delim = '||'
    sep = '||'
    header = '='
    row = '\n'


trac_link_case = re.compile(r'^[A-Z][a-z][^ _]*[A-Z][a-z]')


def to_tracstr(obj: Any) -> str:
    """Convert to string and escape Trac links."""
    strval = str(obj)
    strval = strval.replace('#', '!#')
    escape = '!' if trac_link_case.search(strval) else ''
    return escape + strval


def trac_table_row(row: Row, *, header: bool = False) -> Iterator[str]:
    """Output one row of table."""
    yield _TracSep.delim
    for item in row:
        if header:
            yield _TracSep.header
        yield f' {to_tracstr(item)} '
        if header:
            yield _TracSep.header
        yield _TracSep.sep


def trac_table_iter(rows: Table) -> Iterator[str]:
    """Output formatted table."""
    yield from trac_table_row(next(rows), header=True)
    yield _TracSep.row
    for row in rows:
        yield from trac_table_row(row)
        yield _TracSep.row