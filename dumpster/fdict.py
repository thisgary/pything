from pathlib import Path


def eval_file(path: str, default: str = 'None'):
    p = Path(path)
    if p.exists(): 
        t = p.read_text()
        if len(t) > 0: 
            default = t
    return eval(default)


class fdict(dict):
    def __init__(self, mapping: dict = {}, *, 
            path: str = 'fdict', init: bool = False, **kwargs):
        if not init: 
            d = eval_file(path, '{}')
            kwargs.update(d)
        super(fdict, self).__init__(mapping, **kwargs)
        self.path = path
        self.write()

    def write(self) -> None:
        Path(self.path).write_text(str(self))

