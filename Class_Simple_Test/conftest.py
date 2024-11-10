from pytest import fixture


@fixture
def payload():
    return [10,60]


@fixture
def payload_erro():
    return ["a", "b"]
