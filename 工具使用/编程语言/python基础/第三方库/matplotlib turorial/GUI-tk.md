### Button
1. Button = tk.Button(window, text = , bg = , fg = , width= , height=,command= )
### Label

1. Label = tk.Label(window, text= or textvaribale=, bg = "green", fg, bont=, width= , height=)
### Entry

1. E = tk.Entry(window, show=""or None)
2. A = E.get()
### Insert
1. End, insert, x.y
### Listbox
1. Lb = tk.Listbox(window, listvariable=var1)
2. var1.set()
3. lb.insert("end", item) or (item, "end")
4. lb.delete(item)
### Radiobutton

1. Radiobutton = tk.Radiobutton(window, text = , variable= var1, value=, command=)
    

### Scale

1. Scale = tk.Scale(window, label = ,from_= , to = , orient = tk.HORIZONTAL, length = , showvalue=0, tickinterval = ,resolution= , command
    

### Checkbutton

1. tk.Checkbutton(window,text=, variable=var1, onvalue=, offvalue=, command=)
    

### canvas画布

1. Canvas = tk.Canvas(window, bg= , width= , height=)
    
2. image_file = tk.PhotoImage(file="")
    
3. Image = tk.canvas.create_image(10,10, anchor=, image=)
    
4. Line = tk.canvae.Create_line(x0, y0, x, y)【直接输入坐标值，不用写x= 】
    
5. Oval = ~(x~, fill="red")
    
6. Arc = ~(~, start= , end= 180)
    
7. Rectangle =
    
8. 移动 canvas.move(arc, x, y)【点击一次移动x，y】
    

### 菜单栏

- Menubar = tk.Menu(window)
    
- Filemenu = tk.Menu(menubar, tearoff=0)
    
- menubar.add_cascade(label="", menu=filemenu)
    
- filemenu.add_command(label="", command=)
    
- filemenu.add_separator()
    
- Subfilemenu = tk.Menu(filemenu)
    
- filemenu.add_cascade(label=, menu= ,underline = )
    
- subfilemenu.add_command()
    

  

### frame框架

- Frm = tk.Frame(window)
    
- Frm.pack(window)
    
- frm1 = tk.Frame(Frm)
    
- frm1.pack(side="left")
    

### Messagebox(弹窗）

1. tk.messagebox.showinfo(title=, message=)
    
2. tk.messagebox.showerror()
    
3. tk.messagebox.showwarning()
    
4. tk.messagebox.askquestion()
    
5. tk.messagebox.asktrycancel()
    
6. tk.messagebox.askyesno()
    
7. tk.messagebox.askokcancel
    

### 放置位置

1. pack(): 参数：pack(side=) ;or x= ,y =
    
2. grind(): 参数：grind(row=, column= , padx=, pady=)
    
3. place(): 参数：place(x=, y=)