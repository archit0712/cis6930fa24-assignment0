import main

def test_download():
    data = main.main(page=52)
    assert data is None, 'Failed to download data from API'
    assert len(data['items']) > 0, 'No items on the page'