import main

def test_download():
    data = main.fetch_data_from_api(page=1)
    assert data is not None, 'Failed to download data from API'
    assert len(data['items']) > 0, 'No items on the page'