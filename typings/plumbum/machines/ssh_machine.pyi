import types
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Self

from plumbum._typing import PopenLike
from plumbum.commands import ProcessExecutionError as ProcessExecutionError
from plumbum.commands import shquote as shquote
from plumbum.lib import IS_WIN32 as IS_WIN32
from plumbum.machines.local import local as local
from plumbum.machines.remote import BaseRemoteMachine
from plumbum.machines.session import ShellSession
from plumbum.path.local import LocalPath
from plumbum.path.remote import RemotePath

class SshTunnel:
    __slots__ = ["__weakref__", "_dport", "_lport", "_reverse", "_session"]
    def __init__(self, session, lport, dport, reverse) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        t: type[BaseException] | None,
        v: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def lport(self) -> Incomplete: ...
    @property
    def dport(self) -> Incomplete | str: ...
    @property
    def reverse(self) -> Incomplete: ...

class SshMachine(BaseRemoteMachine):
    host: Incomplete
    def __init__(
        self,
        host,
        user: Incomplete | None = None,
        port: Incomplete | None = None,
        keyfile: Incomplete | None = None,
        ssh_command: Incomplete | None = None,
        scp_command: Incomplete | None = None,
        ssh_opts: Sequence[str] = (),
        scp_opts: Sequence[str] = (),
        password: Incomplete | None = None,
        encoding: str = "utf8",
        connect_timeout: int | None = 10,
        new_session: bool = False,
    ) -> None: ...
    def popen(
        self,
        args,
        ssh_opts: Sequence[str] = (),
        env: Incomplete | None = None,
        cwd: Incomplete | None = None,
        **kwargs,
    ) -> PopenLike: ...
    def nohup(self, command) -> None: ...
    def daemonic_popen(
        self,
        command,
        cwd: str = ".",
        stdout: Incomplete | None = None,
        stderr: Incomplete | None = None,
        append: bool = True,
    ) -> None: ...
    def session(
        self, isatty: bool = False, new_session: bool = False
    ) -> ShellSession: ...
    def tunnel(
        self,
        lport,
        dport,
        lhost: str | None = "localhost",
        dhost: str | None = "localhost",
        connect_timeout: int = 5,
        reverse: bool = False,
    ) -> SshTunnel: ...
    def download(self, src: str | RemotePath, dst: str | LocalPath) -> None: ...
    def upload(self, src: str | LocalPath, dst: str | RemotePath) -> None: ...

class PuttyMachine(SshMachine):
    def __init__(
        self,
        host,
        user: Incomplete | None = None,
        port: Incomplete | None = None,
        keyfile: Incomplete | None = None,
        ssh_command: Incomplete | None = None,
        scp_command: Incomplete | None = None,
        ssh_opts: Sequence[str] = (),
        scp_opts: Sequence[str] = (),
        encoding: str = "utf8",
        connect_timeout: int | None = 10,
        new_session: bool = False,
    ) -> None: ...
    def session(
        self, isatty: bool = False, new_session: bool = False
    ) -> ShellSession: ...
