import pandas as pd
from . import myfunctions as mf
import pprint
def preprocessing(file,year_from,year_to):
    excel_data = pd.read_excel(file)
    data = pd.DataFrame(excel_data)
    remove_list = []

    #YEAR
    year_list, year_remove_index = mf.create_list_and_remove_index(data,"22Q10",mf.year_to_int)
    remove_list.append(year_remove_index)
    #AGE
    age_list = data['01Q1'].tolist()
    for i, age in enumerate(age_list):
        if age[0] == '<':
            age_list[i] = 20
        elif age[0] == '>':
            age_list[i] = 85
        else:
            age_list[i] = (int(age[0])+1)*10

    #GENDER
    gender_list, gender_remove_index = mf.create_list_and_remove_index(data,'02Q2',mf.gender_to_int)
    remove_list.append(gender_remove_index)
    #BMI
    bmi_list = data["03Q3"].tolist()
    bmi_list = list(map(float, bmi_list))
    bmi_remove_index = [n for n,bmi in enumerate(bmi_list) if bmi>50 or bmi < 15]
    remove_list.append(bmi_remove_index)

    #INDICATION
    indication_list, indication_remove_index = mf.create_list_and_remove_index(data,'21Q9',mf.indication_to_int)
    remove_list.append(indication_remove_index)

    #TYPE OF ACCESS
    type_of_access_list, type_of_access_remove_index = mf.create_list_and_remove_index(data,'23Q11',mf.typeofaccess_to_int)
    remove_list.append(type_of_access_remove_index)

    #MESH
    mesh_list1, dummy = mf.create_list_and_remove_index(data,'24Q12',mf.mesh_to_int)
    mesh_list2, dummy = mf.create_list_and_remove_index(data,'52Q21',mf.mesh_to_int)
    mesh_remove_index = []
    mesh_list = []
    for i in range(len(mesh_list1)):
        if mesh_list1[i] == 'NaN' and mesh_list2[i] == 'NaN':
            mesh_remove_index.append(i)
            mesh_list.append('NaN')
        else:
            if mesh_list1[i] != 'NaN' and mesh_list2[i] == 'NaN':
                mesh_list.append(mesh_list1[i])
            elif mesh_list2[i] != 'NaN' and mesh_list1[i] == 'NaN':
                mesh_list.append(mesh_list2[i])
    remove_list.append(mesh_remove_index)

    #INTRAOPERATIVE
    intraoperative_list, intraoperative_remove_index = mf.create_list_and_remove_index(data,'25Q13',mf.intraoperative_to_int)
    remove_list.append(intraoperative_remove_index)

    #COMPLICATION
    complication_list, complication_remove_index = mf.create_list_and_remove_index(data,'35Q15',mf.intraoperative_to_int)
    remove_list.append(complication_remove_index)


    new_remove_list = remove_list[0]
    #union to remove
    for i in range(len(remove_list)):
        new_remove_list = mf.union(new_remove_list,remove_list[i])

    table_of_data = [year_list, age_list, gender_list,bmi_list, indication_list,type_of_access_list,mesh_list,
                     intraoperative_list, complication_list]


    for i in table_of_data:
        for j in sorted(new_remove_list, reverse=True):
            del i[j]

    index_to_remove = [i for i, v in enumerate(table_of_data[0]) if int(year_from) > v or int(year_to) < v]
    for i in table_of_data:
        for j in sorted(index_to_remove,reverse=True):
            del i[j]

    return table_of_data
