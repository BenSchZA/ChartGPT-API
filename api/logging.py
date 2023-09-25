import difflib
import logging
import time

import flask

logger = logging.getLogger("chartgpt")


def get_unified_diff(string1, string2):
    """
    Returns a unified diff of two strings as a multiline string.

    Parameters:
    - string1 (str): First string.
    - string2 (str): Second string.

    Returns:
    - str: Unified diff as a multiline string.
    """

    # Split the strings by lines to compare them as sequences of lines.
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    # Compute the unified diff
    diff = list(difflib.unified_diff(lines1, lines2))

    # Join the diff lines into a single multiline string
    return "\n".join(diff)


def get_unified_diff_changes(string1, string2):
    """
    Returns a unified diff of two strings, showing only changed lines.

    Parameters:
    - string1 (str): First string.
    - string2 (str): Second string.

    Returns:
    - str: Unified diff as a multiline string with only changed lines.
    """

    # Split the strings by lines to compare them as sequences of lines.
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    # Compute the unified diff
    diff = list(difflib.unified_diff(lines1, lines2))

    # Filter only lines that show changes (i.e., lines that start with '+' or '-')
    changed_lines = [
        line
        for line in diff
        if line.startswith(("+", "-")) and not line.startswith(("---", "+++"))
    ]

    # Join the changed lines into a single multiline string
    return "\n".join(changed_lines)


class JobIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.job_id = job_id() if flask.has_request_context() else ""
        return True


def job_id():
    if getattr(flask.g, "job_id", None):
        return flask.g.job_id
    else:
        flask.g.job_id = None
        return flask.g.job_id


def wrap(pre, post):
    """Wrapper"""

    def decorate(func):
        """Decorator"""

        def call(*args, **kwargs):
            """Actual wrapping"""
            pre(func)
            start_time = time.time()
            result = func(*args, **kwargs)
            post(func, duration=time.time() - start_time)
            return result

        return call

    return decorate


def entering(func):
    """Pre function logging"""
    logger.debug("Entered %s", func.__name__)


def exiting(func, duration=None):
    """Post function logging"""
    logger.debug("Exited  %s after %.2f seconds", func.__name__, duration)
