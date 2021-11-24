import pandas as pd
import re

def is_rno(roll_number):
	return re.match(r"\d\d\d\d\w\w\d\d",roll_number)
 
 
def get_ltp(string_ltp):
	ltp = string_ltp.split('-')
	return ltp

def get_complete_sheet(course_taken):
	sbj1 = 1
	cnt1=6
	while sbj1 < cnt1: sbj1 += 1
	result_sheet = set()
	for index, row in course_taken.iterrows():
		course = row["subno"]
		if is_rno(row["rollno"]):
			if ltp_for_subjects[course][0] != "0":
			 result_sheet.add((row["rollno"],row["subno"],"1"))
			if ltp_for_subjects[course][1] != "0":
				result_sheet.add((row["rollno"],row["subno"],"2"))
			if ltp_for_subjects[course][2] != "0":
				result_sheet.add((row["rollno"],row["subno"],"3"))

	return result_sheet


def get_done_list (fb_info):
	result_sheet = set()
	donnee_list=0
	for index, row in fb_info.iterrows():
		if is_rno(row["stud_roll"]):
			result_sheet.add((row["stud_roll"],row["course_code"],str(row["feedback_type"])))
	for index, row in fb_info.iterrows():
		if is_rno(row["stud_roll"]): donnee_list +=1
	return result_sheet


fb_info = pd.read_csv("course_feedback_submitted_by_students.csv")
course_master = pd.read_csv("course_master_dont_open_in_excel.csv")
student_info = pd.read_csv("studentinfo.csv")
course_taken = pd.read_csv("course_registered_by_all_students.csv")
output_format_file = pd.DataFrame(columns = ["Roll Number","Registered Sem","Scheduled Sem","Course Code","Name","Email","AEmail","Contact"])

sch_sem = {}

for index,row in course_taken.iterrows():
	if is_rno(row["rollno"]):
		#sch_sem[row["rollno"]] = {}
		#print(row)
		if row["rollno"] not in sch_sem:
			sch_sem[row["rollno"]] = {}

		sch_sem[row["rollno"]][row["subno"]] = (row["register_sem"],row["schedule_sem"])
		#sch_sem[row["rollno"][row["subno"]]] = 5

ltp_for_subjects = {}

for index, row in course_master.iterrows():
	ltp_for_subjects[row["subno"]] = get_ltp(row["ltp"])

complete_sheet = get_complete_sheet(course_taken)
#complete_sheet.sort()

information_of_particular_students = {}

for index,row in student_info.iterrows():
	information_of_particular_students[row["Roll No"]] = {}
	information_of_particular_students[row["Roll No"]] = row

done_list = get_done_list(fb_info)
#done_list.sort()

complete_sheet = complete_sheet | done_list
remaining_list = done_list ^ complete_sheet

# print(len(remaining_list))
# print(len(complete_sheet))
# print(len(done_list))

for entry in remaining_list:
	#print(entry)
	roll_number = entry[0]
	course = entry[1]
	feed_type = entry[2]
	registered_semester = sch_sem[roll_number][course][0]
	scheduled_semester = sch_sem[roll_number][course][1]
	if roll_number in information_of_particular_students:
		name = information_of_particular_students[roll_number]["Name"]
		mail = information_of_particular_students[roll_number]["email"]
		amail = information_of_particular_students[roll_number]["aemail"]
		contact = information_of_particular_students[roll_number]["contact"]
		new_row = {"Roll Number":roll_number, "Registered Sem":registered_semester,"Scheduled Sem":scheduled_semester,"Course Code":course,"Email":mail,"AEmail":amail,"Contact":contact,"Name":name};
		#print(new_row)
		output_format_file = output_format_file.append(new_row,ignore_index=True)

#print(output_format_file)
#output_format_file.reset_index()
output_format_file.to_excel("course_feedback_remaining.xlsx",index=False)