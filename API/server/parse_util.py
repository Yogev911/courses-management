import xlrd
import json
DEPT_XLS_PATH = 'Workbook2.xlsx'
DEPT_XLS_SHEET_INDEX = 0
STUDENT_GRADES_XLS_PATH = 'Workbook3.xls'
STUDENT_GRADES_SHEET_INDEX = 0
CONST_JSON_PATH = 'data/dept_info.json'
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])


class api_handler(object):
    def __init__(self):
        pass

    def return_json_from_db(self):
        return json.dumps({'msg':'True'})

    def parse_xls(self, xls_binary):
        pass

    def set_json(self, json):
        pass

