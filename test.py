import networkx as nx
import data_generator as gen
import Exc
import sys
import subprocess
import time

global graph
graph = nx.Graph()
global group_dic
group_dic = {}
global message_dic
message_dic = {}

'''
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.socialValue = 0
        self.messages = []
'''


def ap_handler(cmd):
    id = int(cmd[1])
    name = cmd[2]
    age = int(cmd[3])
    if id in graph:
        raise Exc.EqualPersonIdExc(id)
    graph.add_node(id, id=id, name=name, age=age, socialValue=0, messages=[])
    graph.add_edge(id, id, value=0)
    print("Ok")


def ar_handler(cmd):
    id1 = int(cmd[1])
    id2 = int(cmd[2])
    value = int(cmd[3])
    if id1 not in graph:
        raise Exc.PersonIdNotFoundExc(id1)
    if id2 not in graph:
        raise Exc.PersonIdNotFoundExc(id2)
    if graph.has_edge(id1, id2):
        raise Exc.EqualRelationExc(id1, id2)
    graph.add_edge(id1, id2, value=value)
    print("Ok")


def qv_handler(cmd):
    id1 = int(cmd[1])
    id2 = int(cmd[2])
    if id1 not in graph:
        raise Exc.PersonIdNotFoundExc(id1)
    if id2 not in graph:
        raise Exc.PersonIdNotFoundExc(id2)
    if not graph.has_edge(id1, id2):
        raise Exc.RelationNotFoundExc(id1, id2)
    print(graph[id1][id2]['value'])


def cn_handler(cmd):
    id1 = int(cmd[1])
    id2 = int(cmd[2])
    if id1 not in graph:
        raise Exc.PersonIdNotFoundExc(id1)
    if id2 not in graph:
        raise Exc.PersonIdNotFoundExc(id2)
    name1 = graph.nodes[id1]['name']
    name2 = graph.nodes[id2]['name']
    if name1 > name2:
        print(">")
    elif name1 < name2:
        print("<")
    else:
        print("=")


def qnr_handler(cmd):
    ans = 1
    id = int(cmd[1])
    if id not in graph:
        raise Exc.PersonIdNotFoundExc(id)
    name = graph.nodes[id]['name']
    dic = graph._node
    for node in dic.values():
        if name > node['name']:
            ans += 1
    print(ans)


def qps_handler(cmd):
    print(len(graph._node))


def qci_handler(cmd):
    id1 = int(cmd[1])
    id2 = int(cmd[2])
    if id1 not in graph:
        raise Exc.PersonIdNotFoundExc(id1)
    if id2 not in graph:
        raise Exc.PersonIdNotFoundExc(id2)
    if graph.has_edge(id1, id2):
        print(1)
    else:
        print(0)


def qbs_handler(cmd):
    print(nx.number_connected_components(graph))


def ag_handler(cmd):
    id = int(cmd[1])
    if id in group_dic:
        raise Exc.EqualGroupIdExc(id)
    group_dic[id] = {}
    print("Ok")


def atg_handler(cmd):
    person_id = int(cmd[1])
    group_id = int(cmd[2])
    if group_id not in group_dic:
        raise Exc.GroupIdNotFoundExc(group_id)
    if person_id not in graph:
        raise Exc.PersonIdNotFoundExc(person_id)
    if person_id in group_dic[group_id]:
        raise Exc.EqualPersonIdExc(person_id)
    if len(group_dic >= 1111):
        return
    group_dic[group_id][person_id] = {}
    group_dic[group_id][person_id] = graph.nodes[person_id]
    print("Ok")


def qgs_handler(cmd):
    print(str(len(group_dic)))


def qgps_handler(cmd):
    id = int(cmd[1])
    if id not in group_dic:
        raise Exc.GroupIdNotFoundExc(id)
    print(len(group_dic[id]))


def qgvs_handler(cmd):
    ans = 0
    id = int(cmd[1])
    if id not in group_dic:
        raise Exc.GroupIdNotFoundExc(id)
    for id1 in group_dic:
        for id2 in group_dic:
            if graph.has_edge(id1, id2):
                ans += graph[id1][id2]['value']
    print(ans)


def qgam_handler(cmd):
    ans = 0
    id = int(cmd[1])
    if id not in group_dic:
        raise Exc.GroupIdNotFoundExc(id)
    if len(group_dic[id]) == 0:
        print(0)
    else:
        for person in group_dic[id].values():
            ans += person['age']
        ans //= len(group_dic[id])
        print(ans)


def qgav_handler(cmd):
    ans = 0
    id = int(cmd[1])
    if id not in group_dic:
        raise Exc.GroupIdNotFoundExc(id)
    if len(group_dic[id]) == 0:
        print(0)
    else:
        mean = 0
        for person in group_dic[id].values():
            mean += person['age']
        mean //= len(group_dic[id])
        for person in group_dic[id].values():
            age = person['age']
            ans += (age - mean) ** 2
        ans //= len(group_dic[id])
        print(ans)


def dfg_handler(cmd):
    person_id = int(cmd[1])
    group_id = int(cmd[2])
    if group_id not in group_dic:
        raise Exc.GroupIdNotFoundExc(group_id)
    if person_id not in graph:
        raise Exc.PersonIdNotFoundExc(person_id)
    group = group_dic[group_id]
    if person_id not in group:
        raise Exc.EqualPersonIdExc(person_id)
    del group[person_id]
    print("Ok")


def am_handler(cmd):
    message_id = int(cmd[1])
    socialValue = int(cmd[2])
    type = int(cmd[3])
    id1 = int(cmd[4])
    id2 = int(cmd[5])
    if type == 0:
        if id1 not in graph or id2 not in graph:
            print("The person with this number does not exist")
            return
    else:
        if id2 not in group_dic:
            print("Group does not exist")
            return
        if id1 not in graph:
            print("The person with this number does not exist")
            return
    if message_id in message_dic:
        raise Exc.EqualMessageIdExc(message_id)
    if type == 0 and id1 == id2:
        raise Exc.EqualPersonIdExc(id1)
    message_dic[message_id] = {}
    if type == 0:
        message_dic[message_id]['id'] = message_id
        message_dic[message_id]['person1'] = graph.nodes[id1]
        message_dic[message_id]['person2'] = graph.nodes[id2]
        message_dic[message_id]['type'] = type
        message_dic[message_id]['socialValue'] = socialValue
    else:
        message_dic[message_id]['id'] = message_id
        group = group_dic[id2]
        message_dic[message_id]['person1'] = graph.nodes[id1]
        message_dic[message_id]['group'] = group
        message_dic[message_id]['type'] = type
        message_dic[message_id]['socialValue'] = socialValue
    print("Ok")


def sm_handler(cmd):
    id = int(cmd[1])
    if id not in message_dic:
        raise Exc.MessageIdNotFoundExc(id)
    message = message_dic[id]
    type = message['type']
    socialValue = message['socialValue']
    if type == 0:
        person1_id = message['person1']['id']
        person2_id = message['person2']['id']
        if not graph.has_edge(person1_id, person2_id):
            raise Exc.RelationNotFoundExc(person1_id, person2_id)
        graph.nodes[person1_id]['socialValue'] += socialValue
        graph.nodes[person2_id]['socialValue'] += socialValue
        graph.nodes[person2_id]['messages'].append(message)

    if type == 1:
        group = message['group']
        person_id = message['person1']['id']
        if person_id not in group:
            raise Exc.PersonIdNotFoundExc(person_id)
        for dst_id in group:
            graph.nodes[dst_id]['socialValue'] += socialValue
    del message_dic[id]
    print("Ok")


def qsv_handler(cmd):
    id = int(cmd[1])
    if not id in graph:
        raise Exc.PersonIdNotFoundExc(id)
    print(graph.nodes[id]['socialValue'])


def qrm_handler(cmd):
    id = int(cmd[1])
    if id not in graph:
        raise Exc.PersonIdNotFoundExc(id)
    messages = graph.nodes[id]['messages']
    if len(messages) == 0:
        print("None")
        return
    else:
        for i in range(min(len(messages), 4)):
            if i == min(len(messages), 4) - 1:
                print("Ordinary message", end='')
            else:
                print("Ordinary message", end= '; ')
        print()



def main():
    file = open('data.txt','r')
    instr_list = file.readlines()
    file.close()
    # instr_list = ["ap 1 jack 100", "ap 2 mark 100", "ar 1 2 100", "qv 1 2", "ag 1", "atg 1 1"]
    # instr_list = read()
    # instr_list = ['ap 1 jack 100','ap 2 mark 100','ar 1 2 100','qnr 1','qbs']
    # instr_list = ['ap 1 jack 100','ap 2 mark 100','ap 3 tark 100','ar 1 2 100','am 1 100 0 1 2','sm 1','qsv 1','qrm 2','qrm 3']
    # instr_list = ['ap 1 jack 1', 'ap 2 mark 10', 'ap 3 adda 100', 'ag 1','ar 1 2 999',
    #               'atg 1 1', 'atg 2 1', 'atg 3 1', 'am 1 10000 1 1 1', 'sm 1',
    #              'am 1 100 0 2 1','sm 1']
    # instr_list = ['ap 4 su 10','qsv 3','qgs','ap 5 utn 73','qv 4 590','ap 6 oy 22','ap 7 zyp 19']
    for instr in instr_list:
        instr = instr.replace('\n','')
        cmd = instr.split(" ")
        if cmd[0] == "ap":
            try:
                ap_handler(cmd)
            except Exc.EqualPersonIdExc as e:
                e.print()
        elif cmd[0] == "ar":
            try:
                ar_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
            except Exc.EqualRelationExc as e:
                e.print()
        elif cmd[0] == "qv":
            try:
                qv_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
            except Exc.RelationNotFoundExc as e:
                e.print()
        elif cmd[0] == "cn":
            try:
                cn_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qnr":
            try:
                qnr_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qps":
            qps_handler(cmd)
        elif cmd[0] == "qci":
            try:
                qci_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qbs":
            qbs_handler(cmd)
        elif cmd[0] == "ag":
            try:
                ag_handler(cmd)
            except Exc.EqualGroupIdExc as e:
                e.print()
        elif cmd[0] == "atg":
            try:
                atg_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
            except Exc.PersonIdNotFoundExc as e:
                e.print()
            except Exc.EqualPersonIdExc as e:
                e.print()
        elif cmd[0] == "qgs":
            qgs_handler(cmd)
        elif cmd[0] == "qgps":
            try:
                qgps_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qgvs":
            try:
                qgvs_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qgam":
            try:
                qgam_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qgav":
            try:
                qgav_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "dfg":
            try:
                dfg_handler(cmd)
            except Exc.GroupIdNotFoundExc as e:
                e.print()
            except Exc.PersonIdNotFoundExc as e:
                e.print()
            except Exc.EqualPersonIdExc as e:
                e.print()
        elif cmd[0] == "am":
            try:
                am_handler(cmd)
            except Exc.EqualMessageIdExc as e:
                e.print()
            except Exc.EqualPersonIdExc as e:
                e.print()
        elif cmd[0] == "sm":
            try:
                sm_handler(cmd)
            except Exc.MessageIdNotFoundExc as e:
                e.print()
            except Exc.RelationNotFoundExc as e:
                e.print()
            except Exc.PersonIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qsv":
            try:
                qsv_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()
        elif cmd[0] == "qrm":
            try:
                qrm_handler(cmd)
            except Exc.PersonIdNotFoundExc as e:
                e.print()


if __name__ == "__main__":
    main()

