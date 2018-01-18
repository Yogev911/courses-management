import xlrd
DEPT_XLS_PATH = 'Workbook2.xlsx'
DEPT_XLS_SHEET_INDEX = 0
STUDENT_GRADES_XLS_PATH ='Workbook3.xls'
STUDENT_GRADES_SHEET_INDEX = 0

def main():

    dept_courses = [] # each course contains [course_number, course_name, course_points]
    remain_points = []
    matrix = []

    # Parse Dept. courses from const xlsx
    workbook = xlrd.open_workbook(DEPT_XLS_PATH)
    sheet = workbook.sheet_by_index(DEPT_XLS_SHEET_INDEX)
    for rowx in range(sheet.nrows):
        row = sheet.row_values(rowx)
        try:
            if isinstance(row[0],float) and isinstance(row[3],float):
                course_number = int(row[0])
                course_name = row[1]
                course_points = float(row[3])
                dept_courses.append([course_number, course_name, course_points])
            elif isinstance(row[3],float):
                remain_points.append([row[1],float(row[3])])
        except:
            pass
    degree_points = remain_points.pop()[1]
    #
    # Parse student courses from xls
    workbook = xlrd.open_workbook(STUDENT_GRADES_XLS_PATH)
    sheet = workbook.sheet_by_index(STUDENT_GRADES_SHEET_INDEX)
    for rowx in range(sheet.nrows):
        row = sheet.row_values(rowx)
        try:
            matrix.append(row)
        except:
            pass

    student_courses = []
    for row in matrix:
        try:
            # print 'course number = {} ,\t name = {} ,\t grade = {} ,\t\t points = {} '.format(row[32].encode('ascii').split('-')[1],row[19].encode('utf-8'),row[5].encode('utf-8'),row[6])
            student_course_num = int(row[32].encode('ascii').split('-')[1])
            student_course_name = row[19].encode('utf-8')
            student_course_grade = row[5]
            student_course_points = row[6]
            student_courses.append([student_course_num, student_course_name, student_course_points, student_course_grade])
        except:
            pass

    dept_dict = {}
    for dept_course in dept_courses:
        dept_dict[dept_course[0]] = [dept_course[1],dept_course[2]]

    student_dict = {}
    for student_course in student_courses:
        student_dict[student_course[0]] = [student_course[1],student_course[2],student_course[3]]


    #check diff in xls
    for d_key,d_val in dept_dict.iteritems():
        pass
    #
if __name__ == '__main__':
    main()