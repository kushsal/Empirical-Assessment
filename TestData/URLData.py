import openpyxl

def get_url_for_testcase(file_path, testcase_name):
    print(f"Reading Excel: {file_path}")
    print(f"Looking for test case: {testcase_name}")
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
        if row[0] and row[0].strip() == testcase_name.strip():# first column is TestCase name
            print(f"Looking for: {testcase_name}")
            print(f"Found row: {row[0]} → URL: {row[1]}")
            return row[1]             # second column is URL
    return None