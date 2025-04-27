from _typeshed import Incomplete, ReadableBuffer
from types import TracebackType
from typing import Any, Literal, Self

from plumbum.commands import BaseCommand
from plumbum.commands import run_proc as run_proc
from plumbum.commands.processes import ProcessExecutionError
from plumbum.machines.base import PopenAddons

class ShellSessionError(Exception): ...
class SSHCommsError(ProcessExecutionError, EOFError): ...
class SSHCommsChannel2Error(SSHCommsError): ...
class IncorrectLogin(SSHCommsError): ...
class HostPublicKeyUnknown(SSHCommsError): ...

shell_logger: Incomplete

class MarkedPipe:
    pipe: Incomplete
    marker: bytes
    def __init__(self, pipe, marker) -> None: ...
    def close(self) -> None: ...
    def readline(self) -> bytes: ...

class SessionPopen(PopenAddons):
    host: Incomplete
    proc: Incomplete
    argv: Incomplete
    isatty: Incomplete
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    custom_encoding: Incomplete
    returncode: Incomplete
    def __init__(
        self, proc, argv, isatty, stdin, stdout, stderr, encoding, *, host
    ) -> None: ...
    def poll(self) -> int | str | None: ...
    def wait(self) -> int | str | None: ...
    def communicate(
        self, input: ReadableBuffer | None = None
    ) -> tuple[bytes, bytes]: ...

class ShellSession:
    host: Incomplete
    proc: Incomplete
    custom_encoding: Incomplete
    isatty: Incomplete
    def __init__(
        self,
        proc,
        encoding: str = "auto",
        isatty: bool = False,
        connect_timeout: int = 5,
        *,
        host: Incomplete | None = None,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        t: type[BaseException] | None,
        v: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def alive(self) -> bool: ...
    def close(self) -> None: ...
    def popen(self, cmd: str | BaseCommand) -> SessionPopen: ...
    def run(
        self,
        cmd: str | BaseCommand,
        retcode: int | None = 0,
    ) -> tuple[Any, str | Any | Literal[b""], str | Any | Literal[b""]]: ...
