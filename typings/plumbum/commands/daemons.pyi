from _typeshed import Incomplete
from subprocess import Popen
from typing import Any, Literal

from plumbum.commands.processes import ProcessExecutionError as ProcessExecutionError

class _fake_lock:
    @staticmethod
    def acquire(_) -> Literal[True]: ...
    @staticmethod
    def release() -> None: ...

def posix_daemonize(
    command,
    cwd,
    stdout: Incomplete | None = None,
    stderr: Incomplete | None = None,
    append: bool = True,
) -> Popen[Any]: ...
def win32_daemonize(
    command,
    cwd,
    stdout: Incomplete | None = None,
    stderr: Incomplete | None = None,
    append: bool = True,
): ...
