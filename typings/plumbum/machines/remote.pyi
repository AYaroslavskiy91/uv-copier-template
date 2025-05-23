import contextlib
import types
from _typeshed import Incomplete
from collections.abc import Generator
from typing import ClassVar, Never, Self

from plumbum._typing import PopenLike
from plumbum.commands import CommandNotFound as CommandNotFound
from plumbum.commands import ConcreteCommand
from plumbum.commands import shquote as shquote
from plumbum.lib import ProcInfo
from plumbum.machines.base import BaseMachine
from plumbum.machines.env import BaseEnv
from plumbum.machines.session import ShellSession
from plumbum.path.local import LocalPath
from plumbum.path.remote import RemotePath, RemoteWorkdir
from plumbum.path.remote import StatRes as StatRes

class RemoteEnv(BaseEnv):
    __slots__: list[str] = ["_orig", "remote"]
    remote: Incomplete
    def __init__(self, remote) -> None: ...
    def __delitem__(self, name) -> None: ...
    def __setitem__(self, name, value) -> None: ...
    def pop(self, name, *default) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def expand(self, expr): ...
    def expanduser(self, expr): ...
    def getdelta(self) -> dict[str | Incomplete, Incomplete]: ...

class RemoteCommand(ConcreteCommand):
    __slots__: tuple[str,] = ("remote",)
    QUOTE_LEVEL: ClassVar[int]
    remote: Incomplete
    def __init__(self, remote, executable, encoding: str = "auto") -> None: ...
    @property
    def machine(self) -> Incomplete: ...
    def popen(self, args=(), **kwargs): ...
    def nohup(
        self,
        cwd: str = ".",
        stdout: str = "nohup.out",
        stderr: Incomplete | None = None,
        append: bool = True,
    ): ...

class ClosedRemoteMachine(Exception): ...

class ClosedRemote:
    __slots__ = ["__weakref__", "_obj"]
    def __init__(self, obj) -> None: ...
    def close(self) -> None: ...
    def __getattr__(self, name) -> Never: ...

class BaseRemoteMachine(BaseMachine):
    @property
    def cwd(self) -> RemoteWorkdir: ...
    custom_encoding: Incomplete
    connect_timeout: Incomplete
    uname: Incomplete
    env: Incomplete
    def __init__(
        self,
        encoding: str = "utf8",
        connect_timeout: int = 10,
        new_session: bool = False,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        t: type[BaseException] | None,
        v: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    def path(self, *parts) -> RemotePath: ...
    def which(self, progname): ...
    def __getitem__(self, cmd: str | RemotePath) -> RemoteCommand: ...
    @property
    def python(self) -> RemoteCommand: ...
    # FIXME(RR): session-popen are fake abstract methods that always raise NotImplementedError
    def session(
        self, isatty: bool = False, *, new_session: bool = False
    ) -> ShellSession: ...  # Never | ShellSession
    def download(self, src: str | RemotePath, dst: str | LocalPath): ...  # -> Never:
    def upload(self, src: str | LocalPath, dst: str | RemotePath): ...  # -> Never:
    def popen(self, args, **kwargs) -> PopenLike: ...  # Never | PopenLike
    def list_processes(self) -> Generator[ProcInfo, Incomplete, None]: ...
    def pgrep(self, pattern: str | bytes) -> Generator[ProcInfo, Incomplete, None]: ...
    def tempdir(self) -> contextlib.AbstractContextManager[RemotePath]: ...
    def expand(self, expr): ...
    def expanduser(self, expr): ...
