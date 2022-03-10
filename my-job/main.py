# ! My jobs :
# ? 1-Mashg'ulot
otam = {
    'ism':'azimjon',
    'yosh':51,
    'yil':1971,
    'kasb':'sotuvchi'}
print(f"\nBu mening otam, ismlari {otam['ism'].title()}, \
{otam['yil']}-yilda tug'ilganlar, \
yoshlari {otam['yosh']} da, ")

onam = {
    'ism':'nargiza',
    'yosh':48,
    'yil':1974,
    'kasb':'uy bekasi'}
print(f"\nBu mening onam, ismlari {onam['ism'].title()}, \
{onam['yil']}-yilda tug'ilganlar, \
yoshlari {onam['yosh']} da, ")

akam = {
    'ism':'jahongir',
    'yosh':28,
    'yil':1994,
    'kasb':'sotuvchi'}
print(f"\nBu mening akam, ismlari {akam['ism'].title()}, \
{akam['yil']}-yilda tug'ilganlar, \
yoshlari {akam['yosh']} da, ")
# ? 2-Mashg'ulot
taomlar = {
    'vali':'osh',
    'ali':'shashlik',
    'husan':'sho\'rva',
    'hasan':'qozonkabop',
    'men':'moshxorda'
}
name = input('Kimning sevimli taomi kerak?>>> ')
print(f"{name.title()}ning sevimli taomi {taomlar[name]}")
# ? 3-Mashg'ulot
keys = {
    'intager':'intager butun son',
    'float':'float o\'nlik sonlar',
    'boolean':'True va False',
    'string':'string matnlar',
    'list':'ro\'yhatlar',
    'tuple':'o\'zgarmaslar'
}
key = input('bitta type yozing\n>>> ')
print(f"{keys[key]}")
# ? 4-Mashg'ulot
types = {
    'intager':'intager so\'zi butun son deb tarjima qilinadi.',
    'float':'float so\'zi o\'nlik son deb tarjima qilinadi.',
    'boolean':'boolean so\'zi True va Falseni anglatadi.',
    'string':'string matn deb tarjima qilinadi.',
    'list':'list so\'zi ro\'yhat deb tarjima qilinadi.',
    'tuple':'tuple so\'zi o\'zgarmas deb tarjima qilinadi.'
}
i = input('bitta type yozing\n>>> ')
print(f"{types[i]}")
# ? 5-Mashg'ulot
types = {
    'intager':'intager so\'zi butun son deb tarjima qilinadi.',
    'float':'float so\'zi o\'nlik son deb tarjima qilinadi.',
    'boolean':'boolean so\'zi True va Falseni anglatadi.',
    'string':'string matn deb tarjima qilinadi.',
    'list':'list so\'zi ro\'yhat deb tarjima qilinadi.',
    'tuple':'tuple so\'zi o\'zgarmas deb tarjima qilinadi.'
}
i = input('bitta type yozing:\n>>> ').lower()
aniq = types.get(i)
if aniq == None:
    print('Bunday qiymat yo\'q.')
else:
    print(types[i])
