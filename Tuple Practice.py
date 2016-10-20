n = '1', '2', '3', '4', '5'
print n

tup = tuple()
print tup

first = tuple ('Scott')
print first [0]

print first [3:5]

var1 = tuple("hey")
var2 = tuple("you")

temp = var1
var1 = var2
var2 = temp
print var1
print var2

date = 'Jan 15 2016'
month, day, year = date.split(' ')
print month
print day
print year

answer = divmod(1, 4)
print answer

t4 = (7, 5)
divmod(*t4)
print t4

one = 'Scott'
two = 'Shull'
zipped = zip(one, two)
print zipped

months = [('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5), ('June', 6)]
month_dict = dict(months)
print month_dict

words = ['blue', 'red', 'purple', 'white', 'black']


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
print sort_by_length(words)
