list_of_cars=["toyota","ford", "BMW", "audi", "benz"]
list_of_models=["Camry", "F150", "18", "A4" , "5550"]

car={"make" : list_of_cars, "model" : list_of_models, "years" : [2010,2017,2020,2006,2020]}

for key in car:
    #print(key)
    pass

car_years= car["years"]
print(car_years)
"""
for year in years:
    sum+=year
return sum/len(years)
"""
def av_year(years):
    return int(sum(years)/len(years))

print(av_year(car["years"]))


car_colors=["red", "blue", "black", "blue" ,"silver"]

car["num_in_stock"]=[3,5,6,1,3]

for key in car:
    print(key)

for value in car.values():
    print(value)

inventory=car["num_in_stock"]
inventory=sum(car["num_in_stock"])
#print(f"We have {sum(car["num_in_stock"])} cars in stock!")
print(sum(car["num_in_stock"]))
print(f"We have {inventory} cars in stock!")
car["Dealers"]=["Amy","BOB", "Charlie","Dylan","Elaphant"]

for value in car.values():
    print (value)

for key in car:
    print(key)

print(car)
print("\n we 're going to close our dealership'")
car.clear() # erase the contents of the dictionary
print(car)
del car # delete the whole dictionary
# print(car)
