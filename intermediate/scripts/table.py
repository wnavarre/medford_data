import texttable

class PrettyTable:
    def __init__(self, data): self._data = data
    def __repr__(self): return repr(data)
    def __str__(self):
        t = texttable.Texttable()
        t.add_rows([
            [ str(e) for e in r ] for r in self._data
        ])
        return t.draw()

class Cell:
    def __init__(self, value, *, heading=False):
        self._value = value
        self._is_heading = heading
    def is_heading(self): return self._is_heading
    def value(self): return value
    def __str__(self): return str(self._value)
    def __repr__(self): return repr(self._value)

def ValueCell(value): return Cell(value)

def HeadingCell(value): return Cell(value, heading=True)

def EmptyCell(): return Cell("")

def cross_table(rows, cols, f, *, pretty=True):
    out = [ list([ EmptyCell() ]) ]
    out[-1].extend(HeadingCell(col[0]) for col in cols)
    for row_heading, row_value in rows:
        out.append([HeadingCell(row_heading)])
        out[-1].extend(ValueCell(f(row_value, col_value)) for _, col_value in cols)
    print([len(x) for x in out])
    if pretty:
        return PrettyTable(out)
    else:
        return out
