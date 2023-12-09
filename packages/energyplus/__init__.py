class __utils:
    import builtins
    import contextlib

    @classmethod
    @contextlib.contextmanager
    def temporary_attr(cls, o, name: str):
        a = cls.builtins.getattr(o, name)
        try: yield
        finally: cls.builtins.setattr(o, name, a)

    import sys

    @classmethod
    @contextlib.contextmanager
    def temporary_search_path(cls, *paths):
        with cls.temporary_attr(cls.sys, 'path'):
            cls.builtins.setattr(cls.sys, 'path', [str(p) for p in paths])
            try: yield
            finally: pass

__filedir__ = __import__('os').path.dirname(
    __import__('os').path.realpath(__file__)
)

with __utils.temporary_search_path(
    __import__('os').path.join(
        __filedir__, 
        'lib',
    ),
    *__import__('sys').path,
):
    from pyenergyplus import (
        api,
        datatransfer,
        func,
        plugin,
        runtime,
        state,
    )
