import intralinks_test.folders_helper

def test_folders(v2_client, test_data):
    intralinks_test.folders_helper.test_folders(v2_client, test_data)