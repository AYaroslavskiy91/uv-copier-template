import sys
from _typeshed import Incomplete
from collections.abc import Callable, Generator
from contextlib import AbstractContextManager, _GeneratorContextManager
from logging import Logger
from subprocess import Popen
from typing import Any, ClassVar

from plumbum.commands import CommandNotFound as CommandNotFound
from plumbum.commands import ConcreteCommand
from plumbum.commands.daemons import posix_daemonize as posix_daemonize
from plumbum.commands.daemons import win32_daemonize as win32_daemonize
from plumbum.commands.processes import iter_lines as iter_lines
from plumbum.lib import IS_WIN32 as IS_WIN32
from plumbum.lib import ProcInfo
from plumbum.lib import StaticProperty as StaticProperty
from plumbum.machines.base import BaseMachine, PopenAddons
from plumbum.machines.env import BaseEnv
from plumbum.machines.session import ShellSession
from plumbum.path.local import LocalPath
from plumbum.path.local import LocalWorkdir as LocalWorkdir
from plumbum.path.remote import RemotePath as RemotePath

class PlumbumLocalPopen(PopenAddons):
    iter_lines: Callable[
        [Incomplete],
        Generator[
            tuple[Incomplete | None, ...] | tuple[int, Incomplete],
            Incomplete,
            Incomplete,
        ],
    ]
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(
        self,
    ) -> Generator[
        tuple[Incomplete | None, ...] | tuple[int, Incomplete], Incomplete, Incomplete
    ]: ...
    def __enter__(self) -> Popen[str]: ...
    def __exit__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, name): ...

if sys.platform == "win32":
    from plumbum.machines._windows import (
        IMAGE_SUBSYSTEM_WINDOWS_CUI as IMAGE_SUBSYSTEM_WINDOWS_CUI,
    )
    from plumbum.machines._windows import (
        get_pe_subsystem as get_pe_subsystem,
    )
logger: Logger

class LocalEnv(BaseEnv):
    __slots__ = ()
    CASE_SENSITIVE: bool
    def __init__(self) -> None: ...
    def expand(self, expr) -> bytes | str: ...
    def expanduser(self, expr) -> bytes | str: ...

class LocalCommand(ConcreteCommand):
    # "Cannot override class variable (previously declared on base class
    #   "ConcreteCommand") with instance variable"
    QUOTE_LEVEL: ClassVar[int] = 2
    def __init__(self, executable, encoding: str = "auto") -> None: ...
    @property
    def machine(self) -> LocalMachine: ...
    def popen(
        self,
        args=(),
        cwd: Incomplete | None = None,
        env: Incomplete | None = None,
        **kwargs,
    ) -> PlumbumLocalPopen: ...

class LocalMachine(BaseMachine):
    cwd: ClassVar[StaticProperty]
    env: ClassVar[LocalEnv]
    custom_encoding: str  # Actually a ClassVar, but parent class uses as instance var
    uname: ClassVar[Incomplete]
    _program_cache: ClassVar[dict[tuple[str, str], LocalPath]] = {}
    def __init__(self) -> None: ...
    @classmethod
    def which(cls, progname) -> LocalPath: ...
    def path(self, *parts) -> LocalPath: ...
    def __contains__(self, cmd) -> bool: ...
    def __getitem__(self, cmd) -> LocalCommand: ...
    def daemonic_popen(
        self,
        command,
        cwd: str = "/",
        stdout: Incomplete | None = None,
        stderr: Incomplete | None = None,
        append: bool = True,
    ) -> Popen[Any]: ...
    def list_processes(self) -> Generator[ProcInfo, Incomplete, None]: ...
    def pgrep(self, pattern) -> Generator[ProcInfo, Incomplete, None]: ...
    def session(self, new_session: bool = False) -> ShellSession: ...
    def tempdir(self) -> AbstractContextManager[LocalPath]: ...
    def as_user(
        self, username: Incomplete | None = None
    ) -> AbstractContextManager[None]: ...
    def as_root(self) -> _GeneratorContextManager[None]: ...
    python: LocalCommand

local: LocalMachine
