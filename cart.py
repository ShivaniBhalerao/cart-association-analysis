dataset=[["Bread","Milk","Beer"],
        ["Bread","Diapers","Egg"],
        ["Milk","Diapers","Beer","Cola"],
        ["Bread","Milk","Diapers","Beer"],
        ["Bread","Milk","Cola"]]

import pandas as pd  
from mlxtend.preprocessing import TransactionEncoder   
from mlxtend.frequent_patterns import apriori    

te=TransactionEncoder() 
te=te.fit(dataset)  
te_ary=te.transform(dataset)

df=pd.DataFrame(te_ary,columns=te.columns_)

frequent_itemsets=apriori(df,min_support=0.6,use_colnames=True)

#to apply association rules
from mlxtend.frequent_patterns import association_rules

rules=association_rules(frequent_itemsets,metric='support',min_threshold=0.6)

cartItem=[]
init=input("1.Beer\t2.Bread\t3.Cola\t4.Diapers 5.Egg 6.Milk.\n What do you wish to buy? ")
init=init.capitalize()
cartItem=cartItem+[init]
permission='y'

checklist=['Beer','Bread','Cola','Diapers','Egg','Milk']

while(len(cartItem)<6):
    print("Your cart contains: ")
    for i in cartItem:
        print(i)
    
    permission=input("Do you wish to continue?")
    if(permission=='n' or permission=='N'):
        break
    else:
        predict=rules[rules["antecedants"].apply(lambda x: set(cartItem).issubset(set(x)))].sort_values(['support'])  
        question=print("Enter what you wish to buy:")
        
        print("Suggested items:")
        mylist=[list(x) for x in predict['consequents']]
        
        for j in mylist:
            for i in j:
                print (i)
        
     
        
        predict_list=predict['consequents']
        
        init1=input()
        init1=init1.capitalize()
            
        if(init1 in cartItem):
            continue
        if(init1 not in checklist):
            print("Sorry item not present!")
        else:
            cartItem=cartItem+[init1]
if(len(cartItem)<=6):
    print("Your cart item contains:")
for i in cartItem:
    print(i)

if(len(cartItem)>6):
    print("Sorry your cart is full")



