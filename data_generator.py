from PATH import *
import rstr
import random
import numpy as np


NAME_REGEX = "[a-z]{1,6}"
NOTICE_REGEX = "[a-z]{1,100}"


def random_person_id():
    """
    generate person id from exist person id
    also
    generate unexpected person id which cause exception
    """
    global exist_person_id
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 and len(exist_person_id) != 0:
        id = random.choice(exist_person_id)
    else:
        id = random.randint(0, 1000)
    return id


def random_group_id():
    """
    generate group id from exist group id
    also
    generate unexpected group id which cause exception
    """
    global exist_group_id
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 and len(exist_group_id) != 0:
        id = random.choice(exist_group_id)
    else:
        id = random.randint(0, 1000)
    return id


def random_message_id():
    """
    generate message id from exist message id
    also
    generate unexpected message id which cause exception
    """
    global exist_message_id
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 and len(exist_message_id) != 0:
        id = random.choice(exist_message_id)
    else:
        id = random.randint(0, 1000)
    return id


def random_message_attribute(ins):
    global exist_emoji_id

    if ins == 'eid':
        id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
        if id_choice == 1 and len(exist_message_id) != 0:
            id = random.choice(exist_message_id)
        else:
            id = random.randint(0, 10000)
        return id
    elif ins == 'money':
        return random.randint(0, 200)
    elif ins == 'notice':
        return rstr.xeger(NOTICE_REGEX)


def gen_ap():  # add person
    global person_id_order
    global exist_person_id
    # id_choice = np.random.choice([0, 1], p=p.ravel())
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_person_id) == 0:
        id = person_id_order
        person_id_order = person_id_order + 1
        exist_person_id.append(id)
    else:
        id = random.choice(exist_person_id)

    name = rstr.xeger(NAME_REGEX)
    age = random.randint(0, 200)

    return "ap " + str(id) + " " + name + " " + str(age)


def gen_ar():
    id1 = random_person_id()
    id2 = random_person_id()
    value = random.randint(1, 100)
    return "ar " + str(id1) + " " + str(id2) + " " + str(value)


def gen_qv():
    id1 = random_person_id()
    id2 = random_person_id()
    return "qv " + str(id1) + " " + str(id2)


def gen_cn():
    id1 = random_person_id()
    id2 = random_person_id()
    return "cn " + str(id1) + " " + str(id2)


def gen_qnr():
    id = random_person_id()
    return "qnr " + str(id)


def gen_qps():
    return "qps"


def gen_qci():
    id1 = random_person_id()
    id2 = random_person_id()
    return "qci " + str(id1) + " " + str(id2)


def gen_qbs():
    return "qbs"


def gen_ag():
    global exist_group_id
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_group_id) == 0:
        id = group_id_order
        id_order = group_id_order + 1
        exist_group_id.append(id)
    else:
        id = random.choice(exist_group_id)

    return "ag " + str(id)


def gen_atg():
    id1 = random_person_id()
    id2 = random_group_id()
    return "atg " + str(id1) + " " + str(id2)


def gen_qgs():
    return "qgs"


def gen_qgps():  # query_group_people_sum
    id = random_group_id()
    return "qgps " + str(id)


def gen_qgvs():  # query_group_value_sum
    id = random_group_id()
    return "qgvs " + str(id)


def gen_qgam():  # query_group_age_mean
    id = random_group_id()
    return "qgam " + str(id)


def gen_qgav():  # query_group_age_var
    id = random_group_id()
    return "qgav " + str(id)


def gen_dfg():  # del_from_group
    id1 = random_person_id()
    id2 = random_group_id()
    return "dfg " + str(id1) + " " + str(id2)


def gen_am():  # add_message
    global exist_person_id
    global exist_group_id
    global exist_message_id

    global person_id_order
    global group_id_order
    global message_id_order

    social_value = random.randint(-1000, 1000)
    type = random.randint(0, 1)
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_message_id) == 0:
        id = message_id_order
        message_id_order = message_id_order + 1
        exist_message_id.append(id)
    else:
        id = random.choice(exist_message_id)

    if type == 0:
        id1 = random_person_id()
        id2 = random_person_id()
    else:
        id1 = random_person_id()
        id2 = random_group_id()
    return "am " + str(id) + " " + str(social_value) + " " + str(type) + " " + str(id1) + " " + str(id2)


def gen_arem():
    global exist_person_id
    global exist_group_id
    global exist_message_id

    global person_id_order
    global group_id_order
    global message_id_order

    attribute = random_message_attribute('money')
    type = random.randint(0, 1)
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_message_id) == 0:
        id = message_id_order
        message_id_order = message_id_order + 1
        exist_message_id.append(id)
    else:
        id = random.choice(exist_message_id)

    if type == 0:
        id1 = random_person_id()
        id2 = random_person_id()
    else:
        id1 = random_person_id()
        id2 = random_group_id()
    return "arem " + str(id) + " " + str(attribute) + " " + str(type) + " " + str(id1) + " " + str(id2)


def gen_anm():
    global exist_person_id
    global exist_group_id
    global exist_message_id

    global person_id_order
    global group_id_order
    global message_id_order

    attribute = random_message_attribute('notice')
    type = random.randint(0, 1)
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_message_id) == 0:
        id = message_id_order
        message_id_order = message_id_order + 1
        exist_message_id.append(id)
    else:
        id = random.choice(exist_message_id)

    if type == 0:
        id1 = random_person_id()
        id2 = random_person_id()
    else:
        id1 = random_person_id()
        id2 = random_group_id()
    return "anm " + str(id) + " " + str(attribute) + " " + str(type) + " " + str(id1) + " " + str(id2)


def gen_aem():
    global exist_person_id
    global exist_group_id
    global exist_message_id

    global person_id_order
    global group_id_order
    global message_id_order

    attribute = random_message_attribute('eid')
    type = random.randint(0, 1)
    id_choice = np.random.choice([0, 1], p=[0.1, 0.9])
    if id_choice == 1 or len(exist_message_id) == 0:
        id = message_id_order
        message_id_order = message_id_order + 1
        exist_message_id.append(id)
    else:
        id = random.choice(exist_message_id)

    if type == 0:
        id1 = random_person_id()
        id2 = random_person_id()
    else:
        id1 = random_person_id()
        id2 = random_group_id()
    return "aem " + str(id) + " " + str(attribute) + " " + str(type) + " " + str(id1) + " " + str(id2)


def gen_sm():  # send_message
    id = random_message_id()
    return "sm " + str(id)


def gen_qsv():
    id = random_person_id()
    return "qsv " + str(id)


def gen_qrm():  # query_received_messages
    id = random_person_id()
    return "qrm " + str(id)


def gen_sei():  # store_emoji_id id(int)
    id = random_message_attribute('eid')
    return 'sei ' + str(id)


def gen_qp():  # query_popularity id(int)
    id = random_message_attribute('eid')
    return 'qp ' + str(id)


def gen_dce():  # delete_cold_emoji limit(int)
    id = random_message_attribute('eid')
    if id in exist_emoji_id:
        exist_emoji_id.remove(id)
    return 'dce ' + str(id)


def gen_qm():  # query_money id(int)
    id = random_person_id()
    return 'qm ' + str(id)


def gen_sim():  # send_indirect_message id(int)
    id = random_message_id()
    return 'sim ' + str(id)


def generate_data():
    np.random.seed()
    instr_cnt = random.randint(14000, 14999)
    # instr_cnt = 50
    num = [3000, 10000, 333, 333, 333,
           500, 300, 500, 10, 300,
           200, 200, 200, 200, 200,
           200, 200, 5000, 200, 200,
           5000, 300, 300, 300, 300, 3000, 300, 3000]
    sum = 0
    for x in num:
        sum = sum + x
    p = []
    for x in num:
        x = x / sum
        p.append(x)

    choice_list = range(0, 28)
    instr_list = []
    for i in range(instr_cnt):
        sig = np.random.choice(choice_list, p=p)
        instr = ""
        if sig == 0:
            instr = gen_ap()  # 0.5
        elif sig == 1:
            instr = gen_ar()
        elif sig == 2:
            instr = gen_qv()
        elif sig == 3:
            instr = gen_cn()
        elif sig == 4:
            instr = gen_qnr()  # 0.03
        elif sig == 5:
            instr = gen_qps()
        elif sig == 6:
            instr = gen_qci()  # 0.03
        elif sig == 7:
            instr = gen_qbs()
        elif sig == 8:
            instr = gen_ag()  # 0.01
        elif sig == 9:
            instr = gen_atg()
        elif sig == 10:
            instr = gen_qgs()
        elif sig == 11:
            instr = gen_qgps()
        elif sig == 12:
            instr = gen_qgvs()
        elif sig == 13:
            instr = gen_qgam()
        elif sig == 14:
            instr = gen_qgav()
        elif sig == 15:
            instr = gen_dfg()
        elif sig == 16:
            instr = gen_am()
        elif sig == 17:
            instr = gen_sm()
        elif sig == 18:
            instr = gen_qsv()
        elif sig == 19:
            instr = gen_qrm()

        elif sig == 20:
            instr = gen_arem()
        elif sig == 21:
            instr = gen_anm()
        elif sig == 22:
            instr = gen_aem()
        elif sig == 23:
            instr = gen_sei()
        elif sig == 24:
            instr = gen_qp()
        elif sig == 25:
            instr = gen_dce()
        elif sig == 26:
            instr = gen_qm()
        elif sig == 27:
            instr = gen_sei()

        instr_list.append(instr)
    file = open(PATH + 'stdin.txt', 'w')
    for instr in instr_list:
        file.write(instr)
        file.write('\n')
    file.close()
    return instr_list
