import xlrd
import json

DEPT_XLS_PATH = 'Workbook2.xlsx'
DEPT_XLS_SHEET_INDEX = 0
STUDENT_GRADES_XLS_PATH = 'Workbook3.xls'
STUDENT_GRADES_SHEET_INDEX = 0
CONST_JSON_PATH = '../data/dept_info.json'


def return_json_from_db():
    with open(CONST_JSON_PATH, 'r') as fp:
        data = json.load(fp)
    return data


def compare_courses(student_courses):
    diff_courses = {}
    with open(CONST_JSON_PATH, 'r') as fp:
        stored_data = json.load(fp)
    for year in stored_data:
        for courses in year['courses']:
            if courses['course_number'] not in student_courses:
                # print 'you need to do course {} number: {}'.format(courses['name'],courses['course_number'])
                diff_courses[courses['course_number']] = {'course_name': courses['name'],
                                                       'course_points': courses['points']}
    if diff_courses is not None:
        return diff_courses
    else:
        return {'msg': 'True'}


def parse_xls(xls_file):
    # Parse student courses from xls
    with open(xls_file.filename, 'w') as f:
        f.write(xls_file.read())
    matrix = []
    student_courses = {}
    try:
        workbook = xlrd.open_workbook(xls_file.filename)
        sheet = workbook.sheet_by_index(STUDENT_GRADES_SHEET_INDEX)
    except Exception as e:
        print e.message
    for rowx in range(sheet.nrows):
        row = sheet.row_values(rowx)
        try:
            matrix.append(row)
        except:
            pass

    for row in matrix:
        try:
            student_course_num = int(row[32].encode('ascii').split('-')[1])
            student_course_name = row[19]
            # print student_course_name
            # print student_course_name.encode('utf-8')
            # print student_course_name.decode('utf-8')
            student_course_grade = row[5]
            student_course_points = row[6]
            student_courses[student_course_num] = {'course_name': student_course_name,
                                                   'course_points': student_course_points,
                                                   'course_grade': student_course_grade}
        except:
            pass

    with open('student.json', 'w') as fp:
        json.dump(student_courses,fp, sort_keys=True, indent=4)

    data_diff = compare_courses(student_courses)
    return json.dumps(data_diff)


def update_json_in_db(updated_courses):
    try:
        with open(CONST_JSON_PATH, 'w') as f:
            f.write(updated_courses.read())
            return {'msg': 'False'}
    except Exception as e:
        return {'msg': e.message}








# dept_courses = [] # each course contains [course_number, course_name, course_points]
# remain_points = []
# matrix = []
#
# # Parse Dept. courses from const xlsx
# workbook = xlrd.open_workbook(DEPT_XLS_PATH)
# sheet = workbook.sheet_by_index(DEPT_XLS_SHEET_INDEX)
# for rowx in range(sheet.nrows):
#     row = sheet.row_values(rowx)
#     try:
#         if isinstance(row[0],float) and isinstance(row[3],float):
#             course_number = int(row[0])
#             course_name = row[1]
#             course_points = float(row[3])
#             dept_courses.append([course_number, course_name, course_points])
#         elif isinstance(row[3],float):
#             remain_points.append([row[1],float(row[3])])
#     except:
#         pass
# degree_points = remain_points.pop()[1]
# #
# # Parse student courses from xls
# workbook = xlrd.open_workbook(STUDENT_GRADES_XLS_PATH)
# sheet = workbook.sheet_by_index(STUDENT_GRADES_SHEET_INDEX)
# for rowx in range(sheet.nrows):
#     row = sheet.row_values(rowx)
#     try:
#         matrix.append(row)
#     except:
#         pass
#
# student_courses = []
# for row in matrix:
#     try:
#         # print 'course number = {} ,\t name = {} ,\t grade = {} ,\t\t points = {} '.format(row[32].encode('ascii').split('-')[1],row[19].encode('utf-8'),row[5].encode('utf-8'),row[6])
#         student_course_num = int(row[32].encode('ascii').split('-')[1])
#         student_course_name = row[19].encode('utf-8')
#         student_course_grade = row[5]
#         student_course_points = row[6]
#         student_courses.append([student_course_num, student_course_name, student_course_points, student_course_grade])
#     except:
#         pass
#
# dept_dict = {}
# for dept_course in dept_courses:
#     dept_dict[dept_course[0]] = [dept_course[1],dept_course[2]]
#
# student_dict = {}
# for student_course in student_courses:
#     student_dict[student_course[0]] = [student_course[1],student_course[2],student_course[3]]
#
#
# #check diff in xls
# for d_key,d_val in dept_dict.iteritems():
#     pass


