"""
Custom extensions.
"""

from copier_templates_extensions import ContextHook
from jinja2.ext import Extension


class ContextUpdater(ContextHook):
    """
    Inplace updater of Jinja Context
    """
