import xlrd
import json

DEPT_XLS_SHEET_INDEX = 0
STUDENT_GRADES_XLS_PATH = 'data/temp_student_file.xls'
DEPT_XLS_PATH = 'data/temp_dept_file.xlsx'
STUDENT_GRADES_SHEET_INDEX = 0
CONST_JSON_PATH = 'data/dept_info.json'
STUDENT_JSON_PATH = 'data/student.json'
DATA_DIFF_JSON = 'data/data_diff.json'


def return_json_from_db():
    try:
        with open(CONST_JSON_PATH, 'r') as fp:
            data = json.load(fp)
        return data
    except Exception as e:
        return json.dumps({'msg': 'False e', 'error': e.args})


def update_json_in_db(updated_courses):
    try:
        with open(CONST_JSON_PATH, 'w') as f:
            binary = updated_courses.read()
            binary = binary.decode('utf8').replace("'", '"')
            data = json.loads(binary)
            if not isinstance(data, list):
                raise Exception('data must be in list format - your type is {}'.format(type(data)))
            if not all(isinstance(item, dict) for item in data):
                raise Exception('every instance in the list must be dict')
            for block in data:
                if 'year' not in block:
                    raise Exception('key year is missing')
                if 'courses' not in block:
                    raise Exception('key courses is missing')
                if not isinstance(block['courses'], list):
                    raise Exception('courses must be list - your type is {}'.format(type(block['courses'])))
                for course in block['courses']:
                    if not isinstance(course, dict):
                        raise Exception('each course must be dict - your type is {}'.format(type(course)))
                    if not all(k in course for k in ('name', 'points', 'course_number')):
                        raise Exception('each course must be have the keys: name ,points, course_number ')

            return json.dumps({'msg': 'all good'})
            json_fomat = json.dumps(data, indent=4, sort_keys=True)
            f.write(json_fomat)
            return json.dumps({'msg': 'True'})
    except Exception as e:
        return json.dumps({'msg': 'False', 'error': e.args})


def compare_courses(student_courses):
    diff_courses = {}
    try:
        with open(CONST_JSON_PATH, 'r') as fp:
            stored_data = json.load(fp)
        for year in stored_data:
            for courses in year['courses']:
                if courses['course_number'] not in student_courses:
                    diff_courses[courses['course_number']] = {'course_name': courses['name'],
                                                              'course_points': courses['points']}
        if diff_courses is not None:
            return json.dumps(diff_courses)
        else:
            return json.dumps({'msg': 'True'})
    except Exception as e:
        return json.dumps({'msg': 'False', 'error': e.args})


def parse_xls(xls_file):
    # Parse student courses from xls
    student_courses = {}
    with open(STUDENT_GRADES_XLS_PATH, 'w') as f:
        f.write(xls_file.read())
    try:
        workbook = xlrd.open_workbook(STUDENT_GRADES_XLS_PATH)
        sheet = workbook.sheet_by_index(STUDENT_GRADES_SHEET_INDEX)
        for rowx in range(sheet.nrows):
            row = sheet.row_values(rowx)
            try:
                student_course_num = int(row[32].encode('ascii').split('-')[1])
                student_course_name = row[19]
                student_course_grade = row[5]
                student_course_points = row[6]
                student_courses[student_course_num] = {'course_name': student_course_name,
                                                       'course_points': student_course_points,
                                                       'course_grade': student_course_grade}
            except:
                pass

        data_diff = compare_courses(student_courses)

        # debug only
        with open(STUDENT_JSON_PATH, 'w') as fp:
            json.dump(student_courses, fp, sort_keys=True, indent=4)

        with open(DATA_DIFF_JSON, 'w') as fp:
            json.dump(data_diff, fp, sort_keys=True, indent=4)

        return json.dumps(data_diff)
    except Exception as e:
        return json.dumps({'msg': 'False', 'error': e.args})


def parse_dept_xlsx(dept_xlsx):
    dept_courses = {}
    remain_points = []
    matrix = []
    with open(DEPT_XLS_PATH, 'w') as f:
        f.write(dept_xlsx.read())
    workbook = xlrd.open_workbook(DEPT_XLS_PATH)
    sheet = workbook.sheet_by_index(DEPT_XLS_SHEET_INDEX)
    for rowx in range(sheet.nrows):
        row = sheet.row_values(rowx)
        try:
            if isinstance(row[0], float) and isinstance(row[3], float):
                course_number = int(row[0])
                course_name = row[1]
                course_points = float(row[3])
                dept_courses[course_number] = {'course_name': course_name,
                                               'course_points': course_points}
            elif isinstance(row[3], float):
                remain_points.append([row[1], float(row[3])])
        except:
            pass
    degree_points = remain_points.pop()[1]
    #
    # Parse student courses from xls