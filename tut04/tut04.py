from openpyxl import Workbook

student_data = {}
subject_data = {}

with open("regtable_old.csv") as f:
    # skip first line
    next(f)
    for line in f:
        rollno, register_sem, _, subno, _, _, _, _, sub_type = line.split(",")

        if rollno not in student_data:
            student_data[rollno] = []
        data = {}
        data["register_sem"] = register_sem
        data["subno"] = subno
        data["sub_type"] = sub_type
        student_data[rollno].append(data)

        if subno not in subject_data:
            subject_data[subno] = []

        data["rollno"] = rollno
        subject_data[subno].append(data)


def output_by_subject():
    for subno, data_list in subject_data.items():
        wb = Workbook()
        # grab the active worksheet
        ws = wb.active
        ws.append(["rollno", "register_sem", "subno", "sub_type"])
        for data in data_list:
            ws.append(
                [
                    rollno,
                    data["register_sem"],
                    data["subno"],
                    data["sub_type"].strip("\n"),
                ]
            )

        # Save the file
        wb.save(f"output_by_subject/{subno}.xlsx")


def output_individual_roll():
    for rollno, data_list in student_data.items():
        wb = Workbook()
        # grab the active worksheet
        ws = wb.active
        ws.append(["rollno", "register_sem", "subno", "sub_type"])
        for data in data_list:
            ws.append(
                [
                    rollno,
                    data["register_sem"],
                    data["subno"],
                    data["sub_type"].strip("\n"),
                ]
            )

        # Save the file
        wb.save(f"output_individual_roll/{rollno}.xlsx")


output_individual_roll()
output_by_subject()
