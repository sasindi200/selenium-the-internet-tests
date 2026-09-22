import os
import tempfile
from pages.upload_page import UploadPage


def test_file_upload(driver):
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w") as f:
        f.write("test file content")

    page = UploadPage(driver)
    page.open_upload()
    page.upload_file(path)

    assert os.path.basename(path) == page.get_uploaded_filename()
    os.remove(path)