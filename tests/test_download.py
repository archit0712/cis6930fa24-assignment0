import requests
import json
from unittest.mock import patch
from main import fetch_data_from_api, fetch_data_from_file, parse_data
sample_data = {
    "items": [
        {
            "title": "BORIS YAKOVLEVICH LIVSHITS",
            "subjects": ["Counterintelligence"],
            "field_offices": ["newyork"]
        },
        {
            "title": "JESUS DE LA CRUZ - LYNN, MASSACHUSETTS",
            "subjects": ["ViCAP Missing Persons"],
            "field_offices": []
        },
        {
            "title": "IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGAN",
            "subjects": ["ViCAP Missing Persons"],
            "field_offices": ["detroit"]
        }
    ]
}

@patch('requests.get')
def test_fetch_data_from_api(mock_get):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(sample_data).encode('utf-8')
    mock_get.return_value = mock_response

    data = fetch_data_from_api(1)
    assert data is not None  # Ensure that data is not None
    assert isinstance(data, dict)  # Ensure the data is a dictionary
    assert 'items' in data  # Ensure the data contains the 'items' key
    assert len(data['items']) == 3  # Ensure there are 3 items in the response

# Test extracting titles from FBI API data
def test_extract_titles():
    parsed_data = parse_data(sample_data)
    expected_titles = [
        "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork",
        "JESUS DE LA CRUZ - LYNN, MASSACHUSETTSþViCAP Missing Personsþ",
        "IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGANþViCAP Missing Personsþdetroit"
    ]
    assert parsed_data == expected_titles
# Test fetching data from a file and ensuring thorn-separated values are correct
@patch('requests.get')
def test_fetch_data_from_file(mock_get):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(sample_data).encode('utf-8')
    
    mock_get.return_value = mock_response

    # Create a temporary file
    file_path = "result.json"

    # Fetch and write to the file
    data = fetch_data_from_file(file_path)
    assert data is not None
    assert 'items' in data

    # Read back from the file
    with open(file_path, 'r') as f:
        file_data = json.load(f)

    assert file_data == [
        {
            "title": "BORIS YAKOVLEVICH LIVSHITS",
            "subjects": ["Counterintelligence"],
            "field_offices": ["newyork"]
        },
        {
            "title": "JESUS DE LA CRUZ - LYNN, MASSACHUSETTS",
            "subjects": ["ViCAP Missing Persons"],
            "field_offices": []
        },
        {
            "title": "IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGAN",
            "subjects": ["ViCAP Missing Persons"],
            "field_offices": ["detroit"]
        }
    ]


# Test for thorn-separated file output
def test_parse_data():
    thorn_separated_output = parse_data(sample_data)
    expected_output = [
        "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork",
        "JESUS DE LA CRUZ - LYNN, MASSACHUSETTSþViCAP Missing Personsþ",
        "IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGANþViCAP Missing Personsþdetroit"
    ]
    assert thorn_separated_output == expected_output