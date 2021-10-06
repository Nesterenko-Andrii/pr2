var1 = 10
var2 = 11

bool1 = var1 < var2 and var2 < 100
bool2 = var1 > var2 and var2 < 100

print(bool1)
print(bool2)

print('\n')

bool1 = var1 == var2 or var2 > 100
bool2 = var1 > var2 or var2 < 100

print(bool1)
print(bool2)

print('\n')

var_str = 'test'
bool_str = var_str > '1'
print(bool_str)