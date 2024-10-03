from collections import defaultdict
from get_similar_hash import map_strings_to_numbers


class Student:
    def __init__(self, ID, gpa, uni_id, subject, paper_title):
        self.gpa = gpa
        self.ID = ID
        self.uni_id = uni_id
        self.subject = subject
        self.paper_title = paper_title

    def __str__(self):
        return f"Student(id : {self.ID!s} ,university_id : {self.uni_id!s} ,gpa : {("%.2f" % self.gpa)!s} ," + \
            f"subject : {self.subject!s} ,paper_title : {self.paper_title!s})"

    def __repr__(self):
        return str(self)


class University:
    def __init__(self, ID: str = "", students: dict = None, name: str = ""):
        self.ID = ID
        self.name = name
        self.last_student_id = 0
        self.students = students

    def add_student(self, student: Student):
        student.ID = str(self.ID).zfill(3) + str(self.last_student_id)
        self.students[student.ID] = student
        self.last_student_id += 1
        return student

    def __str__(self):
        return f"University(id: {self.ID!s} ,name: {self.name!s})"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    global_id = 0
    all_universities = dict()


    def get_subjects():  # adjustable
        return {
            "Literature": get_gpa_chart(),
            "Modern": get_gpa_chart(),
            "languages": get_gpa_chart(),
            "Music": get_gpa_chart(),
            "Philosophy": get_gpa_chart(),
            "Theology": get_gpa_chart(),
            "Sciences": get_gpa_chart(),
            "Social": get_gpa_chart(),
        }


    def get_gpa_chart():
        ret = dict()
        for i in range(2001):
            ret[str(i)] = get_paper_title_chart()
        return ret


    def get_paper_title_chart():
        return defaultdict(list)


    def get_chart():
        ret = dict()
        for i in range(1000):
            ret[str(i)] = get_subjects()
        return ret


    all_titles = {  # adjustable
        "abcd",
        "abce",
        "abcf",
        "abde",
        "yuio",
        "yuik",
        "yuil",
        "vbnm",
        "vbnj",
        "vbnh",
        "vbng",
        "1234",
        "1235",
        "1236",
        "9876",
        "9875",
        "9873",
        "9870"
    }

    all_subjects = {  # adjustable
        "Literature": True,
        "Modern": True,
        "languages": True,
        "Music": True,
        "Philosophy": True,
        "Theology": True,
        "Sciences": True,
        "Social": True,
    }
    all_students = dict()
    full_chart = get_subjects()
    full_chart_by_university = get_chart()
    threshold = 2  # adjust decrease for better accuracy
    mapped_titles = map_strings_to_numbers(all_titles, threshold)
    gpa_fluctuation = 0.5  # adjustable
    print(mapped_titles)
    reserved = set()
    print("menu:")
    while True:
        ch = input("\tnew university [nu]\n\tempty reserved [er]\n\tget team [gt]\n\tget student info [gsi]\n\t"
                   "new student [ns]\n\texit [exit]\nchoice : ")
        if ch == "exit":
            break
        elif ch == "nu":
            uni = University(str(global_id), dict(), input("name : "))
            all_universities[uni.ID] = uni
            print(uni)
            global_id += 1
        elif ch == "ns":
            data = input("info : gpa,subject,university_id,paper_title : ").split(',')
            if not all_subjects.get(data[1]):
                print("invalid subject")
                continue
            if data[3] not in all_titles:
                print("invalid title")
                continue
            st = Student("-1", float(data[0]), data[2], data[1], data[3])
            st = all_universities.get(st.uni_id).add_student(st)
            all_students[st.ID] = st
            full_chart[st.subject][str(int(st.gpa * 100))][str(mapped_titles[st.paper_title])].append(st)
            full_chart_by_university[str(st.uni_id)][st.subject][str(int(st.gpa * 100))][
                str(mapped_titles[st.paper_title])].append(st)
            print(st)
            # print(all_students)
        elif ch == "gsi":
            print(all_students[input("student_id : ")])
        elif ch == "gt":
            # print(full_chart_by_university['0']['Social']['1200']['4'])
            st = all_students.get(input("student id : "))
            if not st:
                print("not found")
                continue
            suggest = set()
            f = int(gpa_fluctuation * 100)
            ii = 0
            while ii <= f:
                if int(st.gpa * 100) + ii < 2001:
                    for x in full_chart_by_university[str(st.uni_id)][st.subject][str(int(st.gpa * 100) + ii)][
                            str(mapped_titles[st.paper_title])]:
                        if st.ID != x.ID:
                            suggest.add(x.ID)
                        if len(suggest) >= 5:
                            break
                if int(st.gpa * 100) - ii >= 0:
                    for x in full_chart_by_university[str(st.uni_id)][st.subject][str(int(st.gpa * 100) - ii)][
                            str(mapped_titles[st.paper_title])]:
                        if st.ID != x.ID:
                            suggest.add(x.ID)
                        if len(suggest) >= 5:
                            break
                if len(suggest) >= 5:
                    break
                ii += 1
            ii = 0
            while ii <= f:
                if len(suggest) >= 5:
                    break
                if int(st.gpa * 100) + ii < 2001:
                    for x in full_chart[st.subject][str(int(st.gpa * 100) + ii)][
                            str(mapped_titles[st.paper_title])]:
                        if st.ID != x.ID:
                            suggest.add(x.ID)
                        if len(suggest) >= 5:
                            break
                if int(st.gpa * 100) - ii >= 0:
                    for x in full_chart[st.subject][str(int(st.gpa * 100) - ii)][
                            str(mapped_titles[st.paper_title])]:
                        if st.ID != x.ID:
                            suggest.add(x.ID)
                        if len(suggest) >= 5:
                            break
                if len(suggest) >= 5:
                    break
                ii += 1
            if len(suggest) >= 5:
                print(suggest)
                if st.ID in reserved:
                    reserved.remove(st.ID)
            else:
                print("not enough students for the team try again later")
                reserved.add(st.ID)
                print(suggest)
        elif ch == 'er':
            reserved.clear()
