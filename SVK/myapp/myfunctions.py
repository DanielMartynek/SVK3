import math

import numpy as np


def create_list_and_remove_index(data,column,function):
    x_list = data[column].tolist()
    x_list = list(map(function,x_list))
    list_remove_index = [n for n,i in enumerate(x_list) if i == "NaN"]
    return x_list, list_remove_index

#YEAR
def year_to_int(string):
    if isinstance(string,str):
        return int(string[0:4])
    else:
        return "NaN"

#GENDER
# 1 - male
# 0 - female
def gender_to_int(string):
    if string == "male":
        return 1
    elif string == "female":
        return 0

#INDICATION
#Elective = True
#Emergency = False
#"" = "NaN"
def indication_to_int(string):
    if string =="Elective":
        return True
    elif string =="Emergency":
        return False
    elif math.isnan(string):
        return "NaN"

#TYPE OF ACCESS
# "" = "NaN"
# "Open approach" = 1
# "Endoscopic extra-peritoneal (TEP)" = 2
# "Endoscopic trans-abdominal (TAPP)" = 3
#"Robotic Endoscopic extra-peritoneal (rTEP)" = 4
#"Robotic Endoscopic trans-abdominal (rTAPP)" = 5
#"Other" = 6
def typeofaccess_to_int(string):
    if string =="Open approach":
        return 1
    elif string =="Endoscopic extra-peritoneal (TEP)":
        return 2
    elif string =="Endoscopic trans-abdominal (TAPP)":
        return 3
    elif string =="Robotic Endoscopic extra-peritoneal (rTEP)":
        return 4
    elif string =="Robotic Endoscopic trans-abdominal (rTAPP)":
        return 5
    elif string =="Other":
        return 6
    elif math.isnan(string):
        return "NaN"

def mesh_to_int(string):
    # "Yes, mesh repair done" = False
    # "No, non-mesh repair done" = True
    if string == "Yes, mesh repair done":
        return False
    elif string =="No, non-mesh repair done":
        return True
    elif math.isnan(string):
        return "NaN"

def intraoperative_to_int(string):
    # 1 = True
    # 0 = False
    # NaN = "NaN"
    if string == 1:
        return True
    elif string == 0:
        return False
    elif math.isnan(string):
        return "NaN"

def complications_to_int(string):
    if string:
        return True
    elif not string:
        return False
    elif math.isnan(string):
        return "NaN"

def union(list1,list2):
    final_list = list(set(list1) | set(list2))
    return final_list

def histograms(table):
    count_list = []
    label_list = []
    for i in range(len(table)):
        if i == 0:
            continue
        if i == 1:
            counts,dummy = np.histogram(table[i], bins=7)
            bins = ["<20", "25-34", "35-44", "45-54", "55-64","65-74",">75"]

        elif i == 2:
            bins = ["Female", "Male"]
            counts,dummy = np.histogram(table[i], bins=2)
        elif i == 3:
            bins = range(15,41,1)
            counts,dummy = np.histogram(table[i], bins=bins)
        elif i == 4:
            bins = ["Emergency", "Elective"]
            counts,dummy = np.histogram(table[i], bins=2)
        elif i == 5:
            bins = ['Open','TEP','TAPP','rTEP','rTAP','Other']
            counts,dummy = np.histogram(table[i], bins=6)
        elif i == 6:
            bins = ['Non-mesh repair done','Mesh repair done']
            counts,dummy = np.histogram(table[i], bins=2)
        elif i == 7:
            bins = ['No', 'Yes']
            counts,dummy = np.histogram(table[i], bins=2)
        elif i == 8:
            bins = ['True','False']
            counts,dummy = np.histogram(table[i], bins=2)

        count_list.append(counts.tolist())
        label_list.append(bins)
    return count_list

def gender_class(table):
    male_index = [i for i,gender in enumerate(table[2]) if gender == 1]
    female_index = [i for i,gender in enumerate(table[2]) if gender == 0]
    male_age = [table[1][i]+1 for i in male_index]
    female_age = [table[1][i]-1 for i in female_index]
    male_bmi = [table[3][i] for i in male_index]
    female_bmi = [table[3][i] for i in female_index]
    female_age_std = np.std(female_age)
    female_bmi_std = np.std(female_bmi)
    female_bmi_average = np.average(female_bmi)
    female_age_average = np.average(female_age)
    male_age_std = np.std(male_age)
    male_bmi_std = np.std(male_bmi)
    male_bmi_average = np.average(male_bmi)
    male_age_average = np.average(male_age)
    list = [female_bmi_std,female_age_std,female_bmi_average,female_age_average,male_bmi_std,male_age_std,male_bmi_average,male_age_average]

    return male_age,male_bmi,female_age,female_bmi, list


def problem_class(table):
    comp_index = [i for i,comp in enumerate(table[8]) if comp]
    nocomp_index = [i for i,comp in enumerate(table[8]) if not comp]
    comp_age = [table[1][i]+1 for i in comp_index]
    nocomp_age = [table[1][i]-1 for i in nocomp_index]
    comp_bmi = [table[3][i] for i in comp_index]
    nocomp_bmi = [table[3][i] for i in nocomp_index]
    comp_age_std = np.std(comp_age)
    comp_bmi_std = np.std(comp_bmi)
    comp_bmi_average = np.average(comp_bmi)
    comp_age_average = np.average(comp_age)
    nocomp_age_std = np.std(nocomp_age)
    nocomp_bmi_std = np.std(nocomp_bmi)
    nocomp_bmi_average = np.average(nocomp_bmi)
    nocomp_age_average = np.average(nocomp_age)
    list = [comp_bmi_std,comp_age_std,comp_bmi_average,comp_age_average,nocomp_bmi_std,nocomp_age_std,nocomp_bmi_average,nocomp_age_average]

    return comp_age,comp_bmi,nocomp_age,nocomp_bmi,list



