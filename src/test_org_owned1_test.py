from . import test_org_owned1

def test_test_org_owned1():
    assert test_org_owned1.apply("Jane") == "hello Jane"
