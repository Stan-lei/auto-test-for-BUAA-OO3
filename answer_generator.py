from PATH import *
from Exception import *
import networkx as nx


def genAnswer():
    G = nx.Graph()
    file = open(PATH + 'stdin.txt', 'r')
    out = open(OUT, 'w')
    group_dic = {}
    message_dic = {}
    emoji_dic = {}
    flag  = 0
    for line in file.readlines():
        split = line.split()
        ins = split[0]
        cmds = split[1:]
        if ins == 'ap':  # ap id name age
            if G.has_node(cmds[0]):
                EqualPersonIdExc(cmds[0], out)
            else:
                G.add_node(cmds[0],
                           id=cmds[0],
                           name=cmds[1], age=cmds[2],
                           socialValue=0,
                           messages=[],
                           money=0)
                G.add_edge(cmds[0], cmds[0], weight=0)
                out.write('Ok' + '\n')

        elif ins == 'ar':  # ar id1 id2 value
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif not G.has_node(cmds[1]):
                PersonIdNotFoundExc(cmds[1], out)
            elif G.has_edge(cmds[0], cmds[1]):
                EqualRelationExc(cmds[0], cmds[1], out)
            else:
                G.add_edge(cmds[0], cmds[1], weight=int(cmds[2]))
                out.write('Ok' + '\n')

        elif ins == 'qv':  # qv id1 id2
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif not G.has_node(cmds[1]):
                PersonIdNotFoundExc(cmds[1], out)
            elif not G.has_edge(cmds[0], cmds[1]):
                RelationNotFoundExc(cmds[0], cmds[1], out)
            else:
                out.write(str(G.get_edge_data(cmds[0], cmds[1])['weight']) + '\n')

        elif ins == 'cn':  # cn id1 id2
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif not G.has_node(cmds[1]):
                PersonIdNotFoundExc(cmds[1], out)
            else:
                if G.nodes[cmds[0]]['name'] < G.nodes[cmds[1]]['name']:
                    r = "<"
                elif G.nodes[cmds[0]]['name'] == G.nodes[cmds[1]]['name']:
                    r = "="
                else:
                    r = ">"
                out.write(r + '\n')

        elif ins == 'qnr':  # qnr id
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            else:
                rank = 0
                for item in G.nodes:
                    if G.nodes[cmds[0]]['name'] > G.nodes[item]['name']:
                        rank += 1
                out.write(str(rank + 1) + '\n')

        elif ins == 'qps':  # qps
            out.write(str(G.number_of_nodes()) + '\n')

        elif ins == 'qci':  # qci id1 id2
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif not G.has_node(cmds[1]):
                PersonIdNotFoundExc(cmds[1], out)
            else:
                if nx.has_path(G, cmds[0], cmds[1]):
                    out.write('1' + '\n')
                else:
                    out.write('0' + '\n')

        elif ins == 'qbs':  # qbs
            out.write(str(nx.number_connected_components(G)) + '\n')

        elif ins == 'ag':  # ag id
            if cmds[0] in group_dic:
                EqualGroupIdExc(cmds[0], out)
            else:
                group_dic[cmds[0]] = {}
                out.write('Ok' + '\n')

        elif ins == 'atg':  # atg pid gid
            if not cmds[1] in group_dic:
                GroupIdNotFoundExc(cmds[1], out)
            elif not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif cmds[0] in group_dic[cmds[1]]:
                EqualPersonIdExc(cmds[0], out)
            else:
                if len(group_dic) <= 1111:
                    group_dic[cmds[1]][cmds[0]] = {}
                    group_dic[cmds[1]][cmds[0]] = G.nodes[cmds[0]]
                out.write('Ok' + '\n')

        elif ins == 'qgs':  # qgs
            out.write(str(len(group_dic)) + '\n')

        elif ins == 'qgps':  # qgps id
            if not cmds[0] in group_dic:
                GroupIdNotFoundExc(cmds[0], out)
            else:
                out.write(str(len(group_dic[cmds[0]])) + '\n')

        elif ins == 'qgvs':  # qgvs id
            if not cmds[0] in group_dic:
                GroupIdNotFoundExc(cmds[0], out)
            else:
                ans = 0
                for id1 in group_dic[cmds[0]]:
                    for id2 in group_dic[cmds[0]]:
                        if G.has_edge(id1, id2):
                            ans += G[id1][id2]['weight']
                out.write(str(ans) + '\n')

        elif ins == 'qgam':  # qgam id
            if not cmds[0] in group_dic:
                GroupIdNotFoundExc(cmds[0], out)
            else:
                if len(group_dic[cmds[0]]) == 0:
                    out.write('0' + '\n')
                else:
                    ans = 0
                    for person in group_dic[cmds[0]].values():
                        ans += int(person['age'])
                    ans //= len(group_dic[cmds[0]])
                    out.write(str(ans) + '\n')
        elif ins == 'qgav':  # qgav id
            if not cmds[0] in group_dic:
                GroupIdNotFoundExc(cmds[0], out)
            else:
                if len(group_dic[cmds[0]]) == 0:
                    out.write('0' + '\n')
                else:
                    mean = 0
                    for person in group_dic[cmds[0]].values():
                        mean += int(person['age'])
                    mean //= len(group_dic[cmds[0]])
                    ans = 0
                    for person in group_dic[cmds[0]].values():
                        ans += (int(person['age']) - mean) ** 2
                    ans //= len(group_dic[cmds[0]])
                    out.write(str(ans) + '\n')

        elif ins == 'dfg':  # dfg pid gid
            if not cmds[1] in group_dic:
                GroupIdNotFoundExc(cmds[1], out)
            elif not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            elif not cmds[0] in group_dic[cmds[1]]:
                EqualPersonIdExc(cmds[0], out)
            else:
                del group_dic[cmds[1]][cmds[0]]
                out.write('Ok' + '\n')

        elif ins == 'am':  # am id socialValue type id1 id2|gid
            message_id = cmds[0]
            socialValue = int(cmds[1])
            type = cmds[2]
            id1 = cmds[3]
            id2 = cmds[4]
            if type == '0':
                if not G.has_node(id1) or not G.has_node(id2):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    elif id1 == id2:
                        EqualPersonIdExc(id1, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['person2'] = G.nodes[id2]
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = ""
                        message_dic[message_id]['socialValue'] = socialValue
                        message_dic[message_id]['kind'] = "Ordinary message"
                        out.write('Ok' + '\n')
            elif type == '1':
                if id2 not in group_dic:
                    out.write('Group does not exist\n')
                elif not G.has_node(id1):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        group = group_dic[id2]
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['group'] = group
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = ""
                        message_dic[message_id]['socialValue'] = socialValue
                        message_dic[message_id]['kind'] = "Ordinary message"
                        out.write('Ok' + '\n')
        elif ins == 'arem':  # arem id money type pid1 pid2|gid
            message_id = cmds[0]
            money = int(cmds[1])
            type = cmds[2]
            id1 = cmds[3]
            id2 = cmds[4]
            if type == '0':
                if not G.has_node(id1) or not G.has_node(id2):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    elif id1 == id2:
                        EqualPersonIdExc(id1, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['person2'] = G.nodes[id2]
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = money
                        message_dic[message_id]['socialValue'] = money * 5
                        message_dic[message_id]['kind'] = 'RedEnvelope: '
                        out.write('Ok' + '\n')
            elif type == '1':
                if id2 not in group_dic:
                    out.write('Group does not exist\n')
                elif not G.has_node(id1):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        group = group_dic[id2]
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['group'] = group
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = money
                        message_dic[message_id]['socialValue'] = money * 5
                        message_dic[message_id]['kind'] = 'RedEnvelope: '
                        out.write('Ok' + '\n')
        elif ins == 'anm':  # anm id string type pid1 pid2|gid
            message_id = cmds[0]
            notice = cmds[1]
            type = cmds[2]
            id1 = cmds[3]
            id2 = cmds[4]
            if type == '0':
                if not G.has_node(id1) or not G.has_node(id2):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    elif id1 == id2:
                        EqualPersonIdExc(id1, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['person2'] = G.nodes[id2]
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = notice
                        message_dic[message_id]['socialValue'] = len(notice)
                        message_dic[message_id]['kind'] = 'notice: '
                        out.write('Ok' + '\n')
            elif type == '1':
                if id2 not in group_dic:
                    out.write('Group does not exist\n')
                elif not G.has_node(id1):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        group = group_dic[id2]
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['group'] = group
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = notice
                        message_dic[message_id]['socialValue'] = len(notice)
                        message_dic[message_id]['kind'] = 'notice: '
                        out.write('Ok' + '\n')
        elif ins == 'aem':  # aem id eid type pid1 pid2|gid
            message_id = cmds[0]
            emojiNum = cmds[1]
            type = cmds[2]
            id1 = cmds[3]
            id2 = cmds[4]
            if type == '0':
                if not G.has_node(id1) or not G.has_node(id2):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    elif emojiNum not in emoji_dic:
                        EmojiIdNotFoundExc(emojiNum, out)
                    elif id1 == id2:
                        EqualPersonIdExc(id1, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['person2'] = G.nodes[id2]
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = emojiNum
                        message_dic[message_id]['socialValue'] = int(emojiNum)
                        message_dic[message_id]['kind'] = 'Emoji: '
                        out.write('Ok' + '\n')
            elif type == '1':
                if id2 not in group_dic:
                    out.write('Group does not exist\n')
                elif not G.has_node(id1):
                    out.write('The person with this number does not exist\n')
                else:
                    if message_id in message_dic:
                        EqualMessageIdExc(message_id, out)
                    elif emojiNum not in emoji_dic:
                        EmojiIdNotFoundExc(emojiNum, out)
                    else:
                        message_dic[message_id] = {}
                        message_dic[message_id]['id'] = message_id
                        group = group_dic[id2]
                        message_dic[message_id]['person1'] = G.nodes[id1]
                        message_dic[message_id]['group'] = group
                        message_dic[message_id]['type'] = type
                        message_dic[message_id]['attribute'] = emojiNum
                        message_dic[message_id]['socialValue'] = int(emojiNum)
                        message_dic[message_id]['kind'] = 'Emoji: '
                        out.write('Ok' + '\n')

        elif ins == 'sm':  # sm id
            if cmds[0] not in message_dic:
                MessageIdNotFoundExc(cmds[0], out)
            else:
                message = message_dic[cmds[0]]
                type = message['type']
                socialValue = message['socialValue']
                if type == '0':
                    person1_id = message['person1']['id']
                    person2_id = message['person2']['id']
                    if not G.has_edge(person1_id, person2_id):
                        RelationNotFoundExc(person1_id, person2_id, out)
                    else:
                        G.nodes[person2_id]['socialValue'] += socialValue
                        G.nodes[person2_id]['messages'].append(message)
                        del message_dic[cmds[0]]
                        if message['kind'] == 'RedEnvelope: ':
                            money = message['attribute']
                            G.nodes[person1_id]['money'] -= money
                            G.nodes[person2_id]['money'] += money
                        elif message['kind'] == 'Emoji: ':
                            emoji_id = message['attribute']
                            emoji_dic[emoji_id]['heat'] += 1
                        out.write("Ok" + '\n')
                elif type == '1':
                    group = message['group']
                    person_id = message['person1']['id']
                    if person_id not in group:
                        PersonIdNotFoundExc(person_id, out)
                    else:
                        for dst_id in group:
                            G.nodes[dst_id]['socialValue'] += socialValue
                        del message_dic[cmds[0]]
                        if message['kind'] == 'RedEnvelope: ':
                            money = message['attribute']
                            singleMoney = money // len(group)
                            G.nodes[person_id]['money'] -= singleMoney * (len(group) - 1)
                            for dst_id in group:
                                if dst_id != person_id:
                                    G.nodes[dst_id]['money'] += singleMoney
                        elif message['kind'] == 'Emoji: ':
                            emoji_id = message['attribute']
                            emoji_dic[emoji_id]['heat'] += 1
                        out.write("Ok" + '\n')

        elif ins == 'qsv':  # qsv id
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            else:
                out.write(str(G.nodes[cmds[0]]['socialValue']) + '\n')
        elif ins == 'qrm':  # qrm id
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            else:
                messages = G.nodes[cmds[0]]['messages']
                if len(messages) == 0:
                    out.write('None' + '\n')
                else:
                    i = min(len(messages) - 1, 3)
                    while i >= 0:
                        if i == 0:
                            out.write(messages[i]['kind'] + str(messages[i]['attribute']) + '\n')
                        else:
                            out.write(messages[i]['kind'] + str(messages[i]['attribute']) + '; ')
                        i -= 1

        elif ins == 'sei':  # sei id
            if cmds[0] in emoji_dic:
                EqualEmojiIdExc(cmds[0], out)
            else:
                emoji_dic[cmds[0]] = {}
                emoji_dic[cmds[0]]['heat'] = 0
                out.write('Ok' + '\n')

        elif ins == 'qp':  # qp id
            if cmds[0] not in emoji_dic:
                EmojiIdNotFoundExc(cmds[0], out)
            else:
                out.write(str(emoji_dic[cmds[0]]['heat']) + '\n')

        elif ins == 'dce':  # dce limit
            for eid in list(emoji_dic):
                if emoji_dic[eid]['heat'] < int(cmds[0]):
                    del emoji_dic[eid]

            for mid in list(message_dic):
                if message_dic[mid]['kind'] == 'Emoji: ' and message_dic[mid]['attribute'] not in emoji_dic:
                        del message_dic[mid]
            out.write(str(len(emoji_dic)) + '\n')

        elif ins == 'qm':  # qm id
            if not G.has_node(cmds[0]):
                PersonIdNotFoundExc(cmds[0], out)
            else:
                out.write(str(G.nodes[cmds[0]]['money']) + '\n')

        elif ins == 'sim':  # sim id
            id = cmds[0]
            if id not in message_dic \
                    or (id in message_dic and message_dic[id]['type'] == '1'):
                MessageIdNotFoundExc(id, out)
            else:
                message = message_dic[id]
                person1_id = message['person1']['id']
                person2_id = message['person2']['id']
                if not nx.has_path(G, person1_id, person2_id):
                    out.write('-1' + '\n')
                else:
                    del message_dic[id]
                    G.nodes[person1_id]['socialValue'] += message['socialValue']
                    G.nodes[person2_id]['socialValue'] += message['socialValue']
                    if message['kind'] == 'RedEnvelope: ':
                        money = message['attribute']
                        G.nodes[person1_id]['money'] -= money
                        G.nodes[person2_id]['money'] += money
                    elif message['kind'] == 'Emoji: ':
                        emoji_id = message['attribute']
                        emoji_dic[emoji_id]['heat'] += 1
                    G.nodes[person2_id]['messages'].append(message)
                    out.write(str(nx.dijkstra_path_length(G, person1_id, person2_id)) + '\n')

    file.close()
    out.close()

