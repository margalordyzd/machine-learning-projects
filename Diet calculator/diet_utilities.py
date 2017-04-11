import pandas as pd


def diet_calclator(weight,body_fat=.2,active=1,objective='fat_loss',weight_unit='kg'):
    df_values = pd.DataFrame({'1fat_loss': pd.Series([10,1,16,3]),'1muscle_gain': pd.Series([18,1,12,7])})
    Plan=pd.DataFrame()
    magic_protein = .14
    if weight_unit== 'kg':
        weight=weight*2.2
    match=str(active)+objective
    diet = df_values[match]*weight
    meal = diet.iloc[1]*magic_protein
    print 'Debes comer ' + str(diet.iloc[0]) + ' calorias'
    print 'Debes comer ' + str(diet.iloc[1]) + 'g de proteinas'
    meal1=meal-float(df_values[match].iloc[2])
    meal1 = meal1*28.3495
    meal2 = df_values[match].iloc[2]*28.3495
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
    print '- skip or black coffe / plain tea'
    print '********************************************'
    print 'LUNCH:'
    print '- '+str(meal1) + 'g of animal protein'
    print '- non-starchy vegetables'
    print '- 1 piece whole fruit and/or 1 serving whole food fats'
    print '********************************************'
    print 'LUNCH:'
    print '- '+str(meal2) + 'g of animal protein'
    print '- non-starchy vegetables'
    print '- ' + str(df_values[match].iloc[3]) + ' servings starchy carbohydrate (i.e. ' + str(df_values[match].iloc[3]) + ' cup rice or potato/sweet potato)'
    print '********************************************'
    
    
    