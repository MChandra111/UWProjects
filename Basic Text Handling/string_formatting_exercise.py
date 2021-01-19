#Task 1
print("File_{:03d} : {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))

#Task 2
print("File_%03d : %.2f, %.2e, %.2e" % (2, 123.4567, 10000, 12345.67))

#Task 3
def formatter(t):
    form-string = "The {:d} numbers are: ".format(len(t))
    l = []
    for i in range(len(t)):
        if i < (len(t)-1):
            l.append("{:d}, ")
        else:
            l.append("{:d}")
    form_string = form_string + "".join(l)
    print(l)
    return form_string.format(*t)
