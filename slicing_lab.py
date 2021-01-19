#Kind of a scam way of exchanging first and last cause it changes the type
def exchange_first_last_scam(seq):
    new_seq = list(seq)
    first = seq[0]
    last = seq[-1]
    new_seq[0] = last
    new_seq[-1] = first
    listToStr = ''.join([str(elem) for elem in new_seq])
    print(listToStr)

#exchanges first and last items
def exchange_first_last(seq):
    i = 0
    while i < len(seq):
        if i == 0:
            print(seq[-1], end='')
        elif i == (len(seq) - 1):
            print(seq[0], end='')
        else:
            print(seq[i], end='')
        i += 1

#every other item gone
def every_other_gone(seq):
    for i in range(len(seq)):
        if i % 2 == 0:
            print(seq[i])
        else:
            i += 1

#first four removed, last four removed, every other in remaining removed
def ff_lf_eo(seq):
    for i in range(len(seq)):
        if i < 4:
            i += 1
        elif i > (len(seq)-5):
            i += 1
        elif i % 2 == 0:
            print(seq[i], end='')
        else:
            i += 1

#reversed
def reverse(seq):
    print(seq[::-1])
