import datetime
import json

from werkzeug.http import parse_cookie
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response

from secure_cookie._compat import to_native
from secure_cookie.cookie import SecureCookie


def test_basic_support():
    c = SecureCookie(secret_key=b"foo")
    assert c.new
    assert not c.modified
    assert not c.should_save
    c["x"] = 42
    assert c.modified
    assert c.should_save
    s = c.serialize()

    c2 = SecureCookie.unserialize(s, b"foo")
    assert c is not c2
    assert not c2.new
    assert not c2.modified
    assert not c2.should_save
    assert c2 == c

    c3 = SecureCookie.unserialize(s, b"wrong foo")
    assert not c3.modified
    assert not c3.new
    assert c3 == {}

    c4 = SecureCookie({"x": 42}, "foo")
    c4_serialized = c4.serialize()
    assert SecureCookie.unserialize(c4_serialized, "foo") == c4


def test_expire_support():
    c = SecureCookie(secret_key=b"foo")
    c["x"] = 42
    in_the_future = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    s_future = c.serialize(expires=in_the_future)
    in_the_past = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    s_past = c.serialize(expires=in_the_past)

    c2 = SecureCookie.unserialize(s_future, b"foo")
    assert c2["x"] == 42

    c3 = SecureCookie.unserialize(s_past, b"foo")
    assert "x" not in c3


def test_wrapper_support():
    req = Request.from_values()
    resp = Response()
    c = SecureCookie.load_cookie(req, secret_key=b"foo")
    assert c.new
    c["foo"] = 42
    assert c.secret_key == b"foo"
    c.save_cookie(resp)

    req = Request.from_values(
        headers={
            "Cookie": 'session="%s"'
            % parse_cookie(resp.headers["set-cookie"])["session"]
        }
    )
    c2 = SecureCookie.load_cookie(req, secret_key=b"foo")
    assert not c2.new
    assert c2 == c


def test_json():
    class JSONCompat:
        dumps = staticmethod(json.dumps)

        @staticmethod
        def loads(s):
            # json on Python < 3.6 fails on bytes
            return json.loads(to_native(s, "utf8"))

    class JSONSecureCookie(SecureCookie):
        serialization_method = JSONCompat

    secure = JSONSecureCookie({"foo": "bar"}, "secret").serialize()
    data = JSONSecureCookie.unserialize(secure, "secret")
    assert data == {"foo": "bar"}
