class EqualGroupIdExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in EqualGroupIdExc.cnt_manager:
            EqualGroupIdExc.cnt_manager[self.id] = 1
        info = "egi-{}, {}-{}".format(EqualGroupIdExc.exc_cnt, self.id, EqualGroupIdExc.cnt_manager[self.id])
        print(info)
        EqualGroupIdExc.cnt_manager[self.id] += 1
        EqualGroupIdExc.exc_cnt += 1


class EqualMessageIdExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in EqualMessageIdExc.cnt_manager:
            EqualMessageIdExc.cnt_manager[self.id] = 1
        info = "emi-{}, {}-{}".format(EqualMessageIdExc.exc_cnt, self.id, EqualMessageIdExc.cnt_manager[self.id])
        print(info)
        EqualMessageIdExc.cnt_manager[self.id] += 1
        EqualMessageIdExc.exc_cnt += 1


class EqualPersonIdExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in EqualPersonIdExc.cnt_manager:
            EqualPersonIdExc.cnt_manager[self.id] = 1
        info = "epi-{}, {}-{}".format(EqualPersonIdExc.exc_cnt, self.id, EqualPersonIdExc.cnt_manager[self.id])
        print(info)
        EqualPersonIdExc.cnt_manager[self.id] += 1
        EqualPersonIdExc.exc_cnt += 1


class EqualRelationExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def print(self):
        if (self.id1 == self.id2):
            if not self.id1 in EqualRelationExc.cnt_manager:
                EqualRelationExc.cnt_manager[self.id1] = 1
            info = "er-{}, {}-{}, {}-{}".format(EqualRelationExc.exc_cnt, self.id1,
                                                EqualRelationExc.cnt_manager[self.id1],
                                                self.id1, EqualRelationExc.cnt_manager[self.id1])
            print(info)
            EqualRelationExc.cnt_manager[self.id1] += 1
            EqualRelationExc.exc_cnt += 1
        else:
            first = min(self.id1, self.id2)
            second = max(self.id1, self.id2)
            if not first in EqualRelationExc.cnt_manager:
                EqualRelationExc.cnt_manager[first] = 1
            if not second in EqualRelationExc.cnt_manager:
                EqualRelationExc.cnt_manager[second] = 1
            info = "er-{}, {}-{}, {}-{}".format(EqualRelationExc.exc_cnt, first,
                                                EqualRelationExc.cnt_manager[first],
                                                second, EqualRelationExc.cnt_manager[second])
            print(info)
            EqualRelationExc.cnt_manager[first] += 1
            EqualRelationExc.cnt_manager[second] += 1
            EqualRelationExc.exc_cnt += 1


class GroupIdNotFoundExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in GroupIdNotFoundExc.cnt_manager:
            GroupIdNotFoundExc.cnt_manager[self.id] = 1
        info = "ginf-{}, {}-{}".format(GroupIdNotFoundExc.exc_cnt, self.id, GroupIdNotFoundExc.cnt_manager[self.id])
        print(info)
        GroupIdNotFoundExc.cnt_manager[self.id] += 1
        GroupIdNotFoundExc.exc_cnt += 1


class MessageIdNotFoundExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in MessageIdNotFoundExc.cnt_manager:
            MessageIdNotFoundExc.cnt_manager[self.id] = 1
        info = "minf-{}, {}-{}".format(MessageIdNotFoundExc.exc_cnt, self.id, MessageIdNotFoundExc.cnt_manager[self.id])
        print(info)
        MessageIdNotFoundExc.cnt_manager[self.id] += 1
        MessageIdNotFoundExc.exc_cnt += 1


class PersonIdNotFoundExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id):
        self.id = id

    def print(self):
        if not self.id in PersonIdNotFoundExc.cnt_manager:
            PersonIdNotFoundExc.cnt_manager[self.id] = 1
        info = "pinf-{}, {}-{}".format(PersonIdNotFoundExc.exc_cnt, self.id, PersonIdNotFoundExc.cnt_manager[self.id])
        print(info)
        PersonIdNotFoundExc.cnt_manager[self.id] += 1
        PersonIdNotFoundExc.exc_cnt += 1


class RelationNotFoundExc(Exception):
    exc_cnt = 1
    cnt_manager = {}

    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def print(self):
        first = min(self.id1, self.id2)
        second = max(self.id1, self.id2)
        if not first in RelationNotFoundExc.cnt_manager:
            RelationNotFoundExc.cnt_manager[first] = 1
        if not second in RelationNotFoundExc.cnt_manager:
            RelationNotFoundExc.cnt_manager[second] = 1
        info = "rnf-{}, {}-{}, {}-{}".format(RelationNotFoundExc.exc_cnt,
                                             first, RelationNotFoundExc.cnt_manager[first],
                                             second, RelationNotFoundExc.cnt_manager[second])
        print(info)
        RelationNotFoundExc.cnt_manager[first] += 1
        RelationNotFoundExc.cnt_manager[second] += 1
        RelationNotFoundExc.exc_cnt += 1
