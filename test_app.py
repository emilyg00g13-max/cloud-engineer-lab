from app import greet

def test_greet():
    assert greet("Cloud Engineer") == "Hello, Cloud Engineer!"

def test_greet_with_another_name():
    assert greet("AWS") == "Hello, AWS!"
