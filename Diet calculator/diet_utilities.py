import pandas as pd
df =pd.DataFrame({'1fat_loss': pd.Series([10,1,4,.02,9,4])})
def diet_calclator(weight,body_fat=.2,active=1,objective='fat_loss',weight_unit='kg'):
    Plan=pd.DataFrame()
    magic_protein = .14
    if weight_unit== 'kg':
        weight=weight*2.2
    match=str(active)+objective
    diet = df[match]*weight
    meal = diet.iloc[1]*magic_protein
    print 'Debes comer ' + str(diet.iloc[0]) + ' calorias'
    print 'Debes comer ' + str(diet.iloc[1]) + 'g de proteinas'
    meal1=meal-16.
    meal1 = meal1*28.3495
    meal2 = 16*28.3495
    protein_cal = 4*diet.iloc[1]
    fat_cal = diet.iloc[0] *.2
    fat_gr = fat_cal/9.
    carb_cal = diet.iloc[0] - protein_cal - fat_cal
    carb_gr = carb_cal/4.
    Plan['Calories']=[diet.iloc[0]]
    Plan['Protein_gr']=[diet.iloc[1]]
    Plan['Carbs_gr']=[carb_gr]
    Plan['Fat_gr']=[fat_gr]
    print '********************************************'
    print Plan
    print '********************************************'
    print 'BREAKFAST:'
    print ''
    print '- skip'
    print '********************************************'
    print 'LUNCH:'
    print '- '+str(meal1) + 'g of animal protein'
    print '- non-starchy vegetables'
    print '- 1 piece whole fruit and/or 1 serving whole food fats'
    print '********************************************'
    print 'LUNCH:'
    print '- '+str(meal2) + 'g of animal protein'
    print '- non-starchy vegetables'
    print '- 3 servings starchy carbohydrate (i.e. cup rice or 24oz potato/sweet potato)'
    print '********************************************'
    
    
    