import pandas as pd
df =pd.DataFrame({'1fat_loss': pd.Series([10,1])})
def diet_calclator(weight,body_fat=.2,active=1,objective='fat_loss',weight_unit='kg'):
    magic_protein = .14
    if weight_unit== 'kg':
        weight=weight*2.2
    match=str(active)+objective
    diet = df[match]*weight
    meal = diet.iloc[1]*magic_protein
    print 'debes comer ' + str(diet.iloc[0]) + ' calorias'
    print 'debes comer ' + str(diet.iloc[1]) + 'g de proteinas'
    meal1=meal-16
    meal1 = meal1*28.3495
    meal2 = 16*28.3495

    print 'Tu primera comida debe contener: ' + str(meal1) + 'g de carne'
    print 'Tu segunda comida debe contener: ' + str(meal2) + 'g de carne'
    return diet,meal
    
    
    
    