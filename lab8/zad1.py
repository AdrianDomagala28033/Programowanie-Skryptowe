keys = ['a', 'b', 'c', 'd']
values = [1,2,3,4]

slownik = {k:v for k,v in zip(keys, values)}
slownik2 = {}
print(slownik)
# for i in range(len(keys)):
#     slownik[keys[i]] = values[i]
# print(slownik)
# slownik["e"] = sum(slownik.values())
# print(slownik)
# for i in slownik:
#     slownik[i] = pow(slownik.get(i), 2)
# print(slownik)
# for i in slownik:
#     if slownik.get(i) > 10:
#         slownik2[i] = slownik.get(i)
# print(slownik2)