
import json
from main import get_data

#  Open the file in read mode
f = open("result.json", "r")
sample_data = json.load(f)

# Test to check if the data is not empty
def test_fetch_data_from_api():
    data = get_data(page=1)
    assert data is not None  # Ensure that data is not None
    assert 'items' in data  # Ensure the data contains the 'items' key
    assert len(data['items']) > 0  # Ensure the data contains at least one item