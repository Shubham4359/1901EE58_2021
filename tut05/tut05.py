import csv
from openpyxl import Workbook

students = {}
subjects = {}


class Subject:
    def __init__(self, subno, subname, ltp, credit, sub_type, grade):
        self.subno = subno
        self.subname = subname
        self.ltp = ltp
        self.credit = credit
        self.sub_type = sub_type
        self.grade = grade


class Sem:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subno, subname, ltp, crd, sub_type, grade):
        self.subjects.append(Subject(subno, subname, ltp, crd, sub_type, grade))


class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        self.sem = []
        for i in range(8):
            self.sem.append(Sem())

    def update_sem(self, semno, subno, crd, grade, sub_type):
        if int(semno) > 8:
            return
        subname = subjects[subno]["subname"]
        ltp = subjects[subno]["ltp"]
        self.sem[int(semno) - 1].add_subject(subno, subname, ltp, crd, sub_type, grade)


with open("names-roll.csv") as f:
    f = csv.DictReader(f)
    for line in f:
        rollno = line["Roll"]
        students[rollno] = Student(rollno, line["Name"])


with open("subjects_master.csv") as f:
    f = csv.DictReader(f)
    for line in f:
        subno = line["subno"]
        subjects[subno] = {}
        subjects[subno]["subname"] = line["subname"]
        subjects[subno]["ltp"] = line["ltp"]
        subjects[subno]["crd"] = line["crd"]


with open("grades.csv") as f:
    f = csv.DictReader(f)
    for line in f:
        rollno = line["Roll"]
        students[rollno].update_sem(
            line["Sem"],
            line["SubCode"],
            line["Credit"],
            line["Grade"],
            line["Sub_Type"],
        )


grade_num = {
    "AA": 10,
    "AB": 9,
    "BB": 8,
    "BC": 7,
    "CC": 6,
    "CD": 5,
    "DD": 4,
    "F": 0,
    "I": 0,
}


def generate_marksheet():
    for rollno, student_data in students.items():
        wb = Workbook()

        sem_wise_credit = []
        SPI = []

        for semno, sem in enumerate(student_data.sem):
            curr_credit = 0
            curr_spi = 0
            ws = wb.create_sheet()
            ws.title = f"Sem{semno + 1}"
            ws.append(
                [
                    "Sl No.",
                    "Subject No.",
                    "Subject Name",
                    "L-T-P",
                    "Credit",
                    "Subject Type",
                    "Grade",
                ]
            )
            for slno, subject in enumerate(sem.subjects):
                curr_credit += int(subject.credit)
                if subject.grade not in grade_num:
                    subject.grade = "F"
                curr_spi += int(grade_num[subject.grade]) * int(subject.credit)
                ws.append(
                    [
                        slno + 1,
                        subject.subno,
                        subject.subname,
                        subject.ltp,
                        subject.credit,
                        subject.sub_type,
                        subject.grade,
                    ]
                )

            sem_wise_credit.append(curr_credit)
            try:
                SPI.append(round(curr_spi / curr_credit, 2))
            except Exception:
                SPI.append(0)

        total_credits = [sem_wise_credit[0]]
        CPI = [SPI[0]]

        for i in range(1, 8):
            total_credits.append(total_credits[-1] + sem_wise_credit[i])
            CPI.append(
                round(
                    (CPI[-1] * total_credits[-2] + SPI[i] * sem_wise_credit[i])
                    / total_credits[-1],
                    2,
                )
            )

        ws = wb.worksheets[0]
        ws.title = "Overall"
        ws.append(["Roll No.", rollno])
        ws.append(["Name of Student", student_data.name])
        ws.append(["Discipline", rollno[4:-2]])
        ws.append(["Semester No."] + [i for i in range(1, 9)])
        ws.append(["Semester wise Credit Taken"] + sem_wise_credit)
        ws.append(["SPI"] + SPI)
        ws.append(["Total Credits Taken"] + total_credits)
        ws.append(["CPI"] + CPI)

        # Save the file
        wb.save(f"output/{rollno}.xlsx")


generate_marksheet()
