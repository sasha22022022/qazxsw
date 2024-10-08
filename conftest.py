import pytest

def pytest_addoption(parser):
  parser.addoption(
    "--lang", 
    action="store", 
    default="en", 
    help="Язык интерфейса (по умолчанию: en)"
  )

@pytest.fixture
def lang(request):
  return request.config.getoption("--lang")
