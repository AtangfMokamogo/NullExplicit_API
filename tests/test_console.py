import pytest
from pytest_mock import mocker
from analysis_engines.image_engine import ImageEngine
from analysis_engines.text_engine import TextEngine
from models.engines.pickle_storage import PickleStorage
from models.image_query import ImageQuery
from models.text_query import TextQuery
from models.engines.database_storage import DBStorage

def test_do_greet(capsys, mocker):
    from console import NullExplicitConsole
    
    console = NullExplicitConsole()
    console.do_greet("John")
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello John!"

def test_do_AnalyzeImage(mocker):
    from console import NullExplicitConsole

    mock_analyze_file = mocker.patch.object(ImageEngine, 'analyze_file')

    console = NullExplicitConsole()
    console.do_AnalyzeImage('image1.jpeg')

    mock_analyze_file.assert_called_once()

def test_do_AnalyzeText(mocker):
    from console import NullExplicitConsole
    
    mock_analyze_text = mocker.patch.object(TextEngine, 'analyze_text')
    
    console = NullExplicitConsole()
    console.do_AnalyzeText('')
    
    mock_analyze_text.assert_called_once()

def test_do_unpickle(capsys, mocker):
    from console import NullExplicitConsole

    mock_de_pickler = mocker.patch.object(PickleStorage, 'de_pickler')
    mock_de_pickler.return_value = {'key': 'value'}

    console = NullExplicitConsole()
    console.do_unpickle('file.pickle')

    mock_de_pickler.assert_called_once()

    captured = capsys.readouterr()
    assert "this is the object" in captured.out
    assert "{'key': 'value'}" in captured.out
