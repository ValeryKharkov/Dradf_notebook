s = 'valera'
dict_ = {}
for now in s:
    if now not in dict_:
        dict_[now] = 0
    dict_[now] += 1



print(dict_)

max_ = max(dict_.values())
