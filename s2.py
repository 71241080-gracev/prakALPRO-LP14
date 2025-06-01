def konv_list_ke_set(data):
    print("Sebelum konversi(list): ", data)
    new=set(data)
    print("Sesudah konversi(set): ", new)
    return new

def konv_set_ke_list(data):
    print("Sebelum konversi(set): ", data)
    new=list(data)
    print("Sesudah konversi(list): ", new)
    return new

def konv_tuple_ke_set(data):
    print("Sebelum konversi(tuple): ", data)
    new=set(data)
    print("Sesudah konversi(set): ", new)
    return new

def konv_set_ke_tuple(data):
    print("Sebelum konversi(set): ", data)
    new=tuple(data)
    print("Sesudah konversi(tuple): ", new)
    return new

lst=[0,9,8,7,'a']
st={'a',90,'olaa'}
tpl=('hi', 9, 'wr', 100)

print("-------list ke set-------")
konv_list_ke_set(lst)
print("-------set ke list------")
konv_set_ke_list(st)
print("-------tuple ke set-------")
konv_tuple_ke_set(tpl)
print("-------set ke tuple-------")
konv_set_ke_tuple(st)