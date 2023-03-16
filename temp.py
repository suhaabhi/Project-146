from tkinter import*
root = Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")

input = Entry(root)
label_series = Label(root,text="Fibonacci Series: ")
label_sum = Label(root)

def Fibonacci():
    num = int(input.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    while(counter<=num):
        sum2 = sum2 + sum
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        counter = counter+1
        label_series["text"] += str(sum) + ""
        label_sum["text"] = "Fibonacci Sum: " + str(sum2) + ""
        
btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci, bg = 'pink') 
btn.pack()  
input.pack()
label_series.pack()
label_sum.pack()
mainloop()     