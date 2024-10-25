times=int(input("Введите кол-во записей:"))
file=open("foods.txt","w",encoding="UTF-8")
for i in range(times):
    text=input("Введите новую запись:").lower()
    file.write(f"{text}\n")
file.close()
class Foods:
    def add_to_list(filename):
        global row
        fileread=open(filename,encoding="UTF-8")
        row=fileread.readlines()
        print(row)
        fileread.close()
    def update_data(id,txt,filename):
        file=open(filename,"w",encoding="UTF-8")
        file.write(f"Обновлённый список:\n")
        row[id]=txt
        print(row)
        for i in row:
            file.write(f"{i}\n")
        file.close()
    def delete_data(id,filename):
        file=open(filename,"w",encoding="UTF-8")
        file.write(f"Список после удаления:\n")
        popdata=row.pop(id)
        print(row)
        for i in row:
            file.write(f"{i}\n")
        file.close()
    def sumprice(filename):
        total=0
        for i in row:
            i=i.replace("\n","")
            if "-" in i :
                listpart=i.split("-")
                if listpart[-1].isdigit():
                    total+=int(listpart[-1])
        print(f"Общая сумма:{total}")
        file=open(filename,"w",encoding="UTF-8")
        file.write(f"Общая сумма:\n{total}\n")
        file.close()
        
        
     
lst=Foods
lst.add_to_list("foods.txt")
index_u=int(input("Введите id для изменения:"))
val_u=(input("Введите новое значение:"))
lst.update_data(index_u,val_u,"foods.txt")
index_d=int(input("Введите id для удаления:"))
lst.delete_data(index_d,"foods.txt")
lst.sumprice("foods.txt")

    



        
               
