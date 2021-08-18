import os
from tempfile import gettempdir

from secure_cookie.session import FilesystemSessionStore


def test_default_tempdir():
    store = FilesystemSessionStore()
    assert store.path == gettempdir()


def test_basic_fs_sessions(tmpdir):
    store = FilesystemSessionStore(str(tmpdir))
    x = store.new()
    assert x.new
    assert not x.modified
    x["foo"] = [1, 2, 3]
    assert x.modified
    store.save(x)

    x2 = store.get(x.sid)
    assert not x2.new
    assert not x2.modified
    assert x2 is not x
    assert x2 == x
    x2["test"] = 3
    assert x2.modified
    assert not x2.new
    store.save(x2)

    x = store.get(x.sid)
    store.delete(x)
    x2 = store.get(x.sid)
    # the session is not new when it was used previously.
    assert not x2.new


def test_non_urandom(tmpdir):
    urandom = os.urandom
    del os.urandom
    try:
        store = FilesystemSessionStore(str(tmpdir))
        store.new()
    finally:
        os.urandom = urandom


def test_renewing_fs_session(tmpdir):
    store = FilesystemSessionStore(str(tmpdir), renew_missing=True)
    x = store.new()
    store.save(x)
    store.delete(x)
    x2 = store.get(x.sid)
    assert x2.new


def test_fs_session_lising(tmpdir):
    store = FilesystemSessionStore(str(tmpdir), renew_missing=True)
    sessions = set()
    for _ in range(10):
        sess = store.new()
        store.save(sess)
        sessions.add(sess.sid)

    listed_sessions = set(store.list())
    assert sessions == listed_sessions


def test_create_directories_if_needed(tmpdir):
    path = f"{tmpdir}/more/dirs/"
    store = FilesystemSessionStore(path)
    x = store.new()
    x["foo"] = [1, 2, 3]
    assert x.modified
    store.save(x)
