import tkinter as tk 
from tkinter import ttk,messagebox
class restaurantordermanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("restaurant management app")
        self.menuitems={"French fries":2,"pizza":3,"burger":4,"taco":2.5,"pasta":5,"drink":1}
        self.exchangerate=82
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="restaurant order management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menulabels={}
        self.menuquantities={}
        for i,(item,price) in enumerate(self.menuitems.items(),start=1):
            label=ttk.Label(frame,text=f"{item},(${price}):",font=("Arial",12))
            label.grid(row=1,column=0,padx=10,pady=5)
            self.menulabels[item]=label
            quantityentry=ttk.Entry(frame,width=5)
            quantityentry.grid(row=i,column=0,padx=10,pady=5)
            self.menuquantities[item]=quantityentry
        self.currencyvar=tk.StringVar()
        ttk.Label(frame,text="currency",font=("Arial",12)).grid(row=len(self.menuitems)+1,column=0,padx=10,pady=5)
        currencydropdown=ttk.Combobox(frame,textvariable=self.currencyvar,state="readonly",width=18,values=("USD","INR"))
        currencydropdown.grid(row=len(self.menuitems)+1,column=1,padx=10,pady=5)
        currencydropdown.current(0)
        self.currencyvar.trace("w",self.updatemenuprices)
        orderbutton=ttk.Button(frame,text="place order",command=self.placeorder)
        orderbutton.grid(row=len(self.menuitems)+2,columnspan=3,padx=10,pady=5)
    def setup_background(self,root):
        bgwidth,bgheight=800,600
        canvas=tk.Canvas(root,width=bgwidth,height=bgheight)
        canvas.pack()
        originalimage=tk.PhotoImage(file="food")
        backgroundimage=originalimage.subsample(originalimage.width()//bgwidth,originalimage.height()//bgheight)
        canvas.create_image(0,0,anchor=tk.NW,image=backgroundimage)
        def updatemenuprices(self,*args):
            currency=self.currencyvar.get()
            symbol="&" if currency=="INR"else "$"
            rate=self.exchangerate if currency=="INR" else 1
            for item, label in self.menulabels.items():
                price=self.menuitems[item]*rate
                label.config(text=f"{item}({symbol}{price}):")
    def placeorder(self):
        totalcost=0
        ordersummary="Order Summary\n"
        currency=self.currencyvar.get()
        symbol="&" if currency=="INR" else "$"
        rate=self.exchangerate if currency=="INR" else 1
        for item,entry in self.menuquantities.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.menuitems[item]*rate
                cost=quantity*price
                totalcost+=cost
                if quantity>0:
                    ordersummary+=f"{item}:{quantity}x{symbol}{price}={symbol}{cost}\n"
        if totalcost>0:
            ordersummary+=f"\nTotal Cost {symbol}{totalcost}"
            messagebox.showinfo("Order Placed",ordersummary)
        else:
            messagebox.showerror("Error","Please order at least one item")
if __name__=="__main__":
    root=tk.Tk()
    app=restaurantordermanagement(root)
    root.geometry("800x600")
    root.mainloop()