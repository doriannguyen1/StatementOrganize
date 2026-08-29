import csv              

def cleanC1(row):
    del (row[1])
    del (row[1])
    del (row[2])
    del (row[3])
    row[1], row[2] = row[2], row[1]
    return row

def cleanChase(row):
    del (row[1])
    del (row[2])
    del (row[2])
    del (row[3])
    row[1], row[2] = row[2], row[1]
    try:
        row[1] = str(float(row[1]) * -1)
    except:
        pass
    return row

def cleanBilt(row):
    try:
        row[1] = str(float(row[1]) * -1)
    except:
        pass
    del (row[2])
    del (row[2])
    return row

def cleanAmex(self, row):
    
    return row

