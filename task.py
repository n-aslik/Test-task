class Foods:
    def __init__(self):
        self.foods=[]
    def add_to_list(self,val):
        try:
            self.foods.append(val)
            print(self.foods)
        except Exception as ex:
            print(ex)
    def update_list_values(self,id,txt):
        try:
            for i in self.foods:
                i[id]=txt
                print(f"Обновлённый список:\n{i}")
        except  Exception as ex:
            print(ex)
    def delete_list_values(self,id):
        try:
            for i in self.foods:
                popdata=i.pop(id)
                print(f"Список после удаления:\n{i}")
        except Exception as ex:
            print(ex)
    def sumprice(self):
        total=0
        try:
            for i in self.foods:
                for j in i:
                    j=j.replace("\n","")
                    if "-" in j :
                        listpart=j.split("-")
                        if listpart[-1].isdigit():
                            total+=int(listpart[-1])
                print(f"Общая сумма:{total}\n")
        except Exception as ex:
            print(ex)
                
lst=Foods()
array=[]
times=int(input("Введите кол-во записей:"))
with open("foods.txt","w",encoding="UTF-8") as file:
    for i in range(times):
        text=input("Введите новую запись:").lower()
        file.write(f"{text}\n")
    file.close()
with open("foods.txt",encoding="UTF-8") as file:
    array=file.readlines()
    lst.add_to_list(array)
    index_u=int(input("Введите id для изменения:"))
    val_u=(input("Введите новое значение:"))
    lst.update_list_values(index_u,val_u)
    index_d=int(input("Введите id для удаления:"))
    lst.delete_list_values(index_d)
    lst.sumprice()
    file.close()
   
    


   

    



        
               
