from hello_world import hello

def test_hello_world():
    hello()
    with open("hello.txt", "r") as f:
        assert "Hello World" in f.readlines()[0]

def test_hello_world_temp(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    hello()
    assert tmp_path / "hello.txt"
    print(tmp_path)

def test_hello_world_temp_content(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    hello()
    with open("hello.txt", "r") as f:
        assert "Hello World" in f.readlines()[0]

