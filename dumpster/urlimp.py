from importlib import import_module
from pathlib import Path
from urllib.request import urlopen


def basename(url: str) -> str:
    return url.split('#')[0].split('?')[0].split('/')[-1].split('.')[0]


def import_url(url: str, *, path: str = 'modules', name: str = None):
    script = str(urlopen(url).read().decode())
    _path = Path(path)
    _path.mkdir(parents=True, exist_ok=True)
    name = name or basename(url)
    _file = _path / (f'{name}.py')
    _file.write_text(script)
    package = _path.replace('/', '.')
    return import_module(f'.{name}', package)

