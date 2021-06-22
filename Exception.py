PIdNF = {}
PIdNFcnt = 0
GIdNF = {}
GIdNFcnt = 0
MIdNF = {}
MIdNFcnt = 0
EIdNF = {}
EIdNFcnt = 0

EPId = {}
EPIdcnt = 0
EGId = {}
EGIdcnt = 0
EMId = {}
EMIdcnt = 0
EEId = {}
EEIdcnt = 0


RNF = {}
RNFcnt = 0
ER = {}
ERcnt = 0


def PersonIdNotFoundExc(id, out):
    global PIdNF
    global PIdNFcnt

    PIdNFcnt += 1

    cnt = PIdNF.setdefault(id, 0)
    PIdNF[id] = cnt + 1

    out.write('pinf-{0}, {1}-{2}\n'.format(PIdNFcnt, id, PIdNF[id]))


def GroupIdNotFoundExc(id, out):
    global GIdNF
    global GIdNFcnt

    GIdNFcnt += 1

    cnt = GIdNF.setdefault(id, 0)
    GIdNF[id] = cnt + 1

    out.write('ginf-{0}, {1}-{2}\n'.format(GIdNFcnt, id, GIdNF[id]))


def MessageIdNotFoundExc(id, out):
    global MIdNF
    global MIdNFcnt

    MIdNFcnt += 1

    cnt = MIdNF.setdefault(id, 0)
    MIdNF[id] = cnt + 1

    out.write('minf-{0}, {1}-{2}\n'.format(MIdNFcnt, id, MIdNF[id]))


def EmojiIdNotFoundExc(id, out):
    global EIdNF
    global EIdNFcnt

    EIdNFcnt += 1

    cnt = EIdNF.setdefault(id, 0)
    EIdNF[id] = cnt + 1

    out.write('einf-{0}, {1}-{2}\n'.format(EIdNFcnt, id, EIdNF[id]))


def EqualPersonIdExc(id, out):
    global EPId
    global EPIdcnt

    EPIdcnt += 1

    cnt = EPId.setdefault(id, 0)
    EPId[id] = cnt + 1

    out.write('epi-{0}, {1}-{2}\n'.format(EPIdcnt, id, EPId[id]))


def EqualGroupIdExc(id, out):
    global EGId
    global EGIdcnt

    EGIdcnt += 1

    cnt = EGId.setdefault(id, 0)
    EGId[id] = cnt + 1

    out.write('egi-{0}, {1}-{2}\n'.format(EGIdcnt, id, EGId[id]))


def EqualMessageIdExc(id, out):
    global EMId
    global EMIdcnt

    EMIdcnt += 1

    cnt = EMId.setdefault(id, 0)
    EMId[id] = cnt + 1

    out.write('emi-{0}, {1}-{2}\n'.format(EMIdcnt, id, EMId[id]))


def EqualEmojiIdExc(id, out):
    global EEId
    global EEIdcnt

    EEIdcnt += 1

    cnt = EEId.setdefault(id, 0)
    EEId[id] = cnt + 1

    out.write('eei-{0}, {1}-{2}\n'.format(EEIdcnt, id, EEId[id]))


def RelationNotFoundExc(id1, id2, out):
    global RNF
    global RNFcnt

    RNFcnt += 1

    cnt1 = RNF.setdefault(id1, 0)
    RNF[id1] = cnt1 + 1

    cnt2 = RNF.setdefault(id2, 0)
    RNF[id2] = cnt2 + 1

    out.write(
        'rnf-{0}, {1}-{2}, {3}-{4}\n'.format(
            RNFcnt,
            min(int(id1), int(id2)), RNF[str(min(int(id1), int(id2)))],
            max(int(id1), int(id2)), RNF[str(max(int(id1), int(id2)))]
        )
    )


def EqualRelationExc(id1, id2, out):
    global ER
    global ERcnt

    ERcnt += 1

    if id1 != id2:
        cnt1 = ER.setdefault(id1, 0)
        ER[id1] = cnt1 + 1
    cnt2 = ER.setdefault(id2, 0)
    ER[id2] = cnt2 + 1

    out.write(
        'er-{0}, {1}-{2}, {3}-{4}\n'.format(
            ERcnt,
            min(int(id1), int(id2)), ER[str(min(int(id1), int(id2)))],
            max(int(id1), int(id2)), ER[str(max(int(id1), int(id2)))]
        )
    )


def clearAll():
    global PIdNF
    global PIdNFcnt
    global GIdNF
    global GIdNFcnt
    global MIdNF
    global MIdNFcnt
    global EIdNF
    global EIdNFcnt

    global EPId
    global EPIdcnt
    global EGId
    global EGIdcnt
    global EMId
    global EMIdcnt
    global EEId
    global EEIdcnt

    global RNF
    global RNFcnt
    global ER
    global ERcnt

    global exist_person_id
    global exist_group_id
    global exist_message_id
    global exist_emoji_id

    global person_id_order
    global group_id_order
    global message_id_order
    global emoji_id_order

    PIdNF = {}
    PIdNFcnt = 0
    GIdNF = {}
    GIdNFcnt = 0
    MIdNF = {}
    MIdNFcnt = 0
    EIdNF = {}
    EIdNFcnt = 0

    EPId = {}
    EPIdcnt = 0
    EGId = {}
    EGIdcnt = 0
    EMId = {}
    EMIdcnt = 0
    EEId = {}
    EEIdcnt = 0

    RNF = {}
    RNFcnt = 0
    ER = {}
    ERcnt = 0

    exist_person_id = []
    exist_group_id = []
    exist_message_id = []
    exist_emoji_id = []

    person_id_order = 1
    group_id_order = 1
    message_id_order = 1
    emoji_id_order = 1
