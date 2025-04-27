from plumbum.machines.local import local as local
from plumbum.path.base import Path
from plumbum.path.local import LocalPath
from plumbum.path.remote import RemotePath

def delete(*paths: str | LocalPath | RemotePath) -> None: ...
def move(src, dst: str | LocalPath | RemotePath) -> LocalPath | Path | None: ...
def copy(
    src: tuple[str | LocalPath | RemotePath, ...]
    | list[str | LocalPath | RemotePath]
    | str
    | LocalPath
    | RemotePath,
    dst: str | LocalPath | RemotePath,
) -> LocalPath | Path | None: ...
def gui_open(filename) -> None: ...
