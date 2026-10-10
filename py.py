import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",passwd="VK@18",user="root",database="tms")
if mycon.is_connected():
    print("""Connection established to database
          WELCOME TO TEXTILE MANAGEMENT SYSTEM 2025""")
cursor=mycon.cursor()

#FUNCTION FOR BUYER MODULE(INSERTING DETAILS)
def buyer_details_insert():
    buyid=input("enter the buyer id:")
    buyname=input("enter the name of the buyer:")
    shipadds=input("enter the shipping address:")
    emid=input("enter the email-id of the buyer:")
    gstno=input("enter the gst no of the buyer:")
    cno=input("enter the contact number of the buyer:")
    st='''insert into BUYER_DETAILS(BUYER_ID,BUYER_NAME,SHIPPING_ADDRESS,EMAIL_ID,GST_NUMBER,BUYER_CONTACT_INFORMATION)
       values('{}','{}','{}','{}','{}','{}')'''.format(buyid,buyname,shipadds,emid,gstno,cno)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def buyer_details_update():
    buyid=input("enter the buyer id:")
    buyname=input("enter the name of the buyer:")
    shipadds=input("enter the shipping address:")
    emid=input("enter the email-id of the buyer:")
    gstno=input("enter the gst no of the buyer:")
    cno=input("enter the contact number of the buyer:")
    st="""UPDATE BUYER_DETAILS SET BUYER_NAME='{}',SHIPPING_ADDRESS='{}',EMAIL_ID='{}',GST_NUMBER='{}',BUYER_CONTACT_INFORMATION='{}'
        WHERE BUYER_ID='{}'""".format(buyname,shipadds,emid,gstno,cno,buyid)
    print("DATA UPDATED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def buyer_details_delete():
    buyid=input("enter the buyer id:")
    st="DELETE from BUYER_DETAILS where BUYER_ID='{}'".format(buyid)
    print("RECORD DELETED SUCCESFULLY")
    cursor.execute(st)
    mycon.commit()
    print(cursor.rowcount,"Records deleted")

def buyer_details_view():
    cursor.execute("SELECT*FROM BUYER_DETAILS")
    records=cursor.fetchall()
    for row in records:
        print(records)
    print("DATA RETRIEVED SUCESSFULLY")

#CODE FOR SEARCHING A PARTICULAR RECORD
def buyer_details_search():
    buyid=input("enter the buyer id to be searched for:")
    cursor.execute("SELECT* FROM BUYER_DETAILS WHERE BUYER_ID='{}'".format(buyid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION FOR SUPPLIER MODULE
def supplier_details_insert():
    supid=input("enter the supplier id:")
    supname=input("enter the name of the supplier:")
    cpname=input("enter the contact person name of the supplier:")
    cpno=input("enter the contact number of the supplier:")
    add=input("enter the address of the supplier:")
    paytms=input("enter the payment terms of the supplier:")
    suprat=int(input("enter the rating of the supplier:"))
    st='''insert into SUPPLIER_DETAILS(SUPPLIER_ID,SUPPLIER_NAME,CONTACT_PERSON_NAME,CONTACT_PERSON_NUMBER,ADDRESS,PAYMENT_TERMS,
        SUPPLIER_RATING)values('{}','{}','{}',{},'{}','{}',{})'''.format(supid,supname,cpname,cpno,add,paytms,suprat)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_details_update():
    supid=input("enter the supplier id:")
    supname=input("enter the name of the supplier:")
    cpname=input("enter the contact person name of the supplier:")
    cpno=input("enter the contact number of the supplier:")
    add=input("enter the address of the supplier:")
    paytms=input("enter the payment terms of the supplier:")
    suprat=int(input("enter the rating of the supplier:"))
    st="""UPDATE SUPPLIER_DETAILS SET SUPPLIER_NAME='{}',CONTACT_PERSON_NAME='{}',CONTACT_PERSON_NUMBER='{}',ADDRESS='{}',PAYMENT_TERMS='{}',
        SUPPLIER_RATING={} WHERE SUPPLIER_ID='{}'""".format(supname,cpname,cpno,add,paytms,suprat,supid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_details_delete():
    supid=input("enter the supplier id:")
    st="DELETE from SUPPLIER_DETAILS where SUPPLIER_ID='{}'".format(supid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_details_view():
    cursor.execute("SELECT* FROM SUPPLIER_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def supplier_details_search():
    supid=input("enter the supplier id:")
    cursor.execute("SELECT* FROM SUPPLIER_DETAILS WHERE SUPPLIER_ID='{}'".format(supid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION FOR INVENTORY MODULE
def inventory_details_insert():
    prid=input("enter the product id:")
    prname=input("enter the product name:")
    descr=eval(input("enter the weight of the product"))
    catgry=input("enter the category of the product:")
    size=input("enter the size of the product:")
    mat=input("enter the material of the product:")
    fbtype=input("enter the fabric type of the product:")
    pat=input("enter the pattern on the product:")
    st='''insert into INVENTORY(PRODUCT_ID,PRODUCT_NAME,DESCRIPTION,CATEGORY,SIZE,MATERIAL,FABRIC_TYPE,PATTERN)values('{}','{}','{}'
       ,'{}','{}','{}','{}','{}')'''.format(prid,prname,descr,catgry,size,mat,fbtype,pat)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def inventory_details_update():
    prid=input("enter the product id:")
    prname=input("enter the product name:")
    descr=eval(input("enter the weight of the product"))
    catgry=input("enter the category of the product:")
    size=input("enter the size of the product:")
    mat=input("enter the material of the product:")
    fbtype=input("enter the fabric type of the product:")
    pat=input("enter the pattern on the product:")
    st="""UPDATE INVENTORY SET PRODUCT_NAME='{}',DESCRIPTION='{}',CATEGORY='{}',SIZE='{}',MATERIAL='{}',FABRIC_TYPE='{}',
       PATTERN='{}' WHERE PRODUCT_ID='{}'""".format(prname,descr,catgry,size,mat,fbtype,pat,prid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def inventory_details_delete():
    prid=input("enter the product id:")
    st="DELETE from INVENTORY where PRODUCT_ID='{}'".format(prid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def inventory_details_view():
    cursor.execute("SELECT* FROM INVENTORY")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def inventory_details_search():
    prid=input("enter the product id:")
    cursor.execute("SELECT* FROM INVENTORY WHERE PRODUCT_ID='{}'".format(prid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION  FOR ORDERS MODULE
def orders_details_insert():
    orid=input("enter the order id:")
    buyid=input("enter the buyer id:")
    buyname=input("enter the buyer name:")
    ordate=input("enter the order date:")
    orst=input("enter the order status:")
    cno=int(input("enter the contact number:"))
    prid=input("enter the product id:")
    qty=int(input("enter the quantity:"))
    size=input("enter the size:")
    mat=input("enter the material:")
    fbtype=input("enter the fabric type:")
    pat=input("enter the pattern:")
    totpr=float(input("enter the total price:"))
    shipadds=input("enter the shipping address:")
    trno=input("enter the tracking number:")
    st='''insert into ORDER_DETAILS(ORDER_ID,BUYER_ID,BUYER_NAME,ORDER_DATE,ORDER_STATUS,CONTACT_INFORMATION,PRODUCT_ID,QUANTITY,SIZE,
       MATERIAL,FABRIC_TYPE,PATTERN,TOTAL_PRICE,SHIPPING_ADDRESS,TRACKING_NUMBER)values('{}','{}','{}'
       ,'{}','{}',{},'{}',{},'{}','{}','{}','{}',{},'{}','{}')'''.format(orid,buyid,buyname,ordate,orst,cno,prid,qty,
       size,mat,fbtype,pat,totpr,shipadds,trno)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def orders_details_update():
    orid=input("enter the order id:")
    buyid=input("enter the buyer id:")
    buyname=input("enter the buyer name:")
    ordate=input("enter the order date:")
    orst=input("enter the order status:")
    cno=int(input("enter the contact number:"))
    prid=input("enter the product id:")
    qty=int(input("enter the quantity:"))
    size=input("enter the size:")
    mat=input("enter the material:")
    fbtype=input("enter the fabric type:")
    pat=input("enter the pattern:")
    totpr=float(input("enter the total price:"))
    shipadds=input("enter the shipping address:")
    trno=input("enter the tracking number:")
    st="""UPDATE ORDER_DETAILS SET BUYER_ID='{}',BUYER_NAME='{}',ORDER_DATE='{}',ORDER_STATUS='{}',CONTACT_INFORMATION={},PRODUCT_ID='{}'
      ,QUANTITY='{}',SIZE='{}',MATERIAL='{}',FABRIC_TYPE='{}',PATTERN='{}',TOTAL_PRICE={},SHIPPING_ADDRESS='{}',
       TRACKING_NUMBER='{}' WHERE ORDER_ID='{}'""".format(buyid,buyname,ordate,orst,cno,prid,qty,size,mat,fbtype,pat,totpr,shipadds,
       trno,orid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def orders_details_delete():
    orid=input("enter the order id:")
    st="DELETE from ORDER_DETAILS where ORDER_ID='{}'".format(orid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def orders_details_view():
    cursor.execute("SELECT* FROM ORDER_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def orders_details_search():
    orid=input("enter the order id:")
    cursor.execute("SELECT* FROM ORDER_DETAILS WHERE ORDER_ID='{}'".format(orid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION FOR SUPPLIER ORDERS MODULE
def supplier_order_details_insert():
    supid=input("enter the supplier id:")
    supname=input("enter the name of the supplier:")
    orid=input("enter the order id:")
    mat=input("enter the material:")
    fbtype=input("enter the fabric type:")
    size=input("enter the size:")
    qty=int(input("enter the quantity:"))
    totpr=float(input("enter the total price:"))
    pat=input("enter the pattern:")
    fine=int(input("enter the fine amount(if delayed):"))
    shipadds=input("enter the shipping address:")
    st='''insert into SUPPLIER_ORDER_DETAILS(SUPPLIER_ID,SUPPLIER_NAME,ORDER_ID,MATERIAL,FABRIC_TYPE,SIZE,QUANTITY,TOTAL_COST,PATTERN,
       FINE,SHIPPING_ADDRESS)values('{}','{}','{}' ,'{}','{}','{}',{},{},'{}',{},'{}')'''.format(supid,supname,orid,mat,fbtype,size,qty,totpr,pat,fine,shipadds)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_order_details_update():
    supid=input("enter the supplier id:")
    supname=input("enter the name of the supplier:")
    orid=input("enter the order id:")
    mat=input("enter the material:")
    fbtype=input("enter the fabric type:")
    size=input("enter the size:")
    qty=int(input("enter the quantity:"))
    totpr=float(input("enter the total price:"))
    pat=input("enter the pattern:")
    fine=int(input("enter the fine amount(if delayed):"))
    shipadds=input("enter the shipping address:")
    st="""UPDATE SUPPLIER_ORDER_DETAILS SET SUPPLIER_NAME='{}',ORDER_ID='{}',MATERIAL='{}',FABRIC_TYPE='{}',SIZE='{}',QUANTITY={},
       TOTAL_COST={},PATTERN='{}',FINE={},SHIPPING_ADDRESS='{}'WHERE SUPPLIER_ID='{}'""".format(supname,orid,mat,fbtype,size,qty,
        totpr,pat,fine,shipadds,supid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_order_details_delete():
    supid=input("enter the supplier id:")
    st="DELETE from SUPPLIER_ORDER_DETAILS where SUPPLIER_ID='{}'".format(supid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def supplier_order_details_view():
    cursor.execute("SELECT* FROM SUPPLIER_ORDER_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def supplier_order_details_search():
    supid=input("enter the supplier id:")
    cursor.execute("SELECT* FROM SUPPLIER_ORDER_DETAILS WHERE SUPPLIER_ID='{}'".format(supid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")


#FUNCTION FOR EMPLOYEE MODULE
def employee_details_insert():
    name=input("enter the name of the employee:")
    add=input("enter the residential address of the employee:")
    cno=input("enter the contact number of the employee:")
    email=input("enter the email-id of the employee:")
    empid=input("enter the employee-id of the employee:")
    dept=input("enter the department of the employee:")
    sal=float(input("enter the salary of the employee:"))
    hdate=input("enter the hiring date of the employee:")
    tdate=input("enter the termination date of the employee:")
    att=input("enter the attendence of the employee:")
    ovt=int(input("enter the overtime work data of the employee:"))
    st='''insert into EMPLOYEE_DETAILS(NAME,ADDRESS,CONTACT_INFORMATION,EMAIL,EMPLOYEE_ID,DEPARTMENT,SALARY,HIRE_DATE,TERMINATION_DATE,
          ATTENDENCE,OVERTIME)values('{}','{}','{}' ,'{}','{}','{}',{},'{}','{}','{}',{})'''.format(name,add,cno,email,empid,dept,sal,hdate,tdate,att,ovt)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def employee_details_update():
    name=input("enter the name of the employee:")
    add=input("enter the residential address of the employee:")
    cno=input("enter the contact number of the employee:")
    email=input("enter the email-id of the employee:")
    empid=input("enter the employee-id of the employee:")
    dept=input("enter the department of the employee:")
    sal=float(input("enter the salary of the employee:"))
    hdate=input("enter the hiring date of the employee:")
    tdate=input("enter the termination date of the employee:")
    att=input("enter the attendence of the employee:")
    ovt=int(input("enter the overtime work data of the employee:"))
    st="""UPDATE EMPLOYEE_DETAILS SET NAME='{}',ADDRESS='{}',CONTACT_INFORMATION='{}',EMAIL='{}',DEPARTMENT='{}',SALARY='{}',HIRE_DATE='{}',
       TERMINATION_DATE='{}',ATTENDENCE='{}',OVERTIME={} WHERE EMPLOYEE_ID='{}'""".format(name,add,cno,email,dept,sal,hdate,tdate,att,ovt,
       empid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def employee_details_delete():
    empid=input("enter the employee id:")
    st="DELETE from EMPLOYEE_DETAILS where EMPLOYEE_ID='{}'".format(empid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def employee_details_view():
    cursor.execute("SELECT* FROM EMPLOYEE_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def employee_details_search():
    empid=input("enter the employee id:")
    cursor.execute("SELECT* FROM EMPLOYEE_DETAILS WHERE EMPLOYEE_ID='{}'".format(empid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION FOR INSERTING SHIPPING DETAILS
def shipping_details_insert():
    orid=input("enter the order id:")
    buyid=input("enter the buyer id:")
    ordate=input("enter the order date:")
    orst=input("enter the order status:")
    itmsppd=input("enter the list of items shipped:")
    shipadds=input("enter the shipping address:")
    cno=input("enter the contact number of the buyer:")
    shipmthd=input("enter the method of shipping:")
    st='''insert into SHIPPING_DETAILS(ORDER_ID,BUYER_ID,ORDER_DATE,ORDER_STATUS,ITEMS_SHIPPED,SHIPPING_ADDRESS,BUYER_CONTACT_INFORMATION,
        SHIPPING_METHOD)values('{}','{}','{}' ,'{}','{}','{}','{}','{}')'''.format(orid,buyid,ordate,orst,itmsppd,shipadds,cno,shipmthd)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def shipping_details_update():
    orid=input("enter the order id:")
    buyid=input("enter the buyer id:")
    ordate=input("enter the order date:")
    orst=input("enter the order status:")
    itmsppd=input("enter the list of items shipped:")
    shipadds=input("enter the shipping address:")
    cno=input("enter the contact number of the buyer:")
    shipmthd=input("enter the method of shipping:")
    st="""UPDATE SHIPPING_DETAILS SET BUYER_ID='{}',ORDER_DATE='{}',ORDER_STATUS='{}',ITEMS_SHIPPED='{}',SHIPPING_ADDRESS='{}',
         BUYER_CONTACT_INFORMATION='{}',SHIPPING_METHOD='{}' WHERE ORDER_ID='{}'""".format(buyid,ordate,orst,itmsppd,shipadds,cno,shipmthd,orid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def shipping_details_delete():
    orid=input("enter the order id:")
    st="DELETE from SHIPPING_DETAILS where ORDER_ID='{}'".format(orid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def shipping_details_view():
    cursor.execute("SELECT* FROM SHIPPING_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def shipping_details_search():
    orid=input("enter the order id:")
    cursor.execute("SELECT* FROM SHIPPING_DETAILS WHERE ORDER_ID='{}'".format(orid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND")

#FUNCTION FOR INSERTING PAYMENT DETAILS
def payment_details_insert():
    orid=input("enter the order id:")
    ordate=input("enter the order date:")
    duedate=input("enter the due date:")
    totpr=float(input("enter the total price:"))
    rempay=float(input("enter the remaining payment left:"))
    paytrms=input("enter the payment method:")
    pystat=input("enter the payment status:")
    shipmthd=input("enter the method of shipping:")
    fine=int(input("enter the fine amount:"))
    st='''insert into PAYMENT_DETAILS(ORDER_ID,ORDER_DATE,DUE_DATE,TOTAL_AMOUNT,REMAINING_PAYMENT,PAYMENT_STATUS,PAYMENT_METHOD,SHIPPING_METHOD
        ,FINE)values('{}','{}','{}' ,{},'{}','{}','{}','{}',{})'''.format(orid,ordate,duedate,totpr,rempay,paytrms,pystat,shipmthd,fine)
    print("DATA ENTERED SUCCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def payment_details_update():
    orid=input("enter the order id:")
    ordate=input("enter the order date:")
    duedate=input("enter the due date:")
    totpr=int(input("enter the total price:"))
    rempay=int(input("enter the remaining payment left:"))
    paytrms=input("enter the payment method:")
    pystat=input("enter the payment status:")
    shipmthd=input("enter the method of shipping:")
    fine=int(input("enter the fine amount:"))
    st="""UPDATE PAYMENT_DETAILS SET ORDER_DATE='{}',DUE_DATE='{}',TOTAL_AMOUNT={},REMAINING_PAYMENT={},PAYMENT_METHOD='{}',
         PAYMENT_STATUS='{}',SHIPPING_METHOD='{}',FINE={} WHERE ORDER_ID='{}'""".format(ordate,duedate,totpr,rempay,paytrms,pystat,shipmthd,fine,orid)
    print("DATA UPDATED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def payment_details_delete():
    orid=input("enter the order id:")
    st="DELETE from PAYMENT_DETAILS where ORDER_ID='{}'".format(orid)
    print("RECORD DELETED SUCESSFULLY")
    cursor.execute(st)
    mycon.commit()

def payment_details_view():
    cursor.execute("SELECT* FROM PAYMENT_DETAILS")
    records=cursor.fetchall()
    for record in records:
        print(record)
    print("DATA VIEWED SUCESSFULLY")

def payment_details_search():
    orid=input("enter the order id:")
    cursor.execute("SELECT* FROM PAYMENT_DETAILS WHERE ORDER_ID='{}'".format(orid))
    records=cursor.fetchall()
    if records:
        for record in records:
            print(record)
    else:
        print("NO MORE RECORDS TO BE FOUND") 
#__________________________________________________________________________________________________________________________________________________________________
def main_menu():
    while True:
        print("\nTEXTILE MANAGEMENT MENU")
        print("1. Buyer Details") 
        print("2. Supplier Details")
        print("3. Inventory Details")
        print("4. Orders Details")
        print("5. Supplier Order Details")
        print("6. Employee Details")
        print("7. Shipping Details")
        print("8. Payment Details")
        print("9. Exit")

        choice=int(input("enter your choice:  "))

        if choice==1:
            buyer_menu()
        elif choice==2:
            supplier_menu()
        elif choice==3:
            inventory_menu()
        elif choice==4:
            orders_menu()
        elif choice==5:
            supplier_orders_menu()
        elif choice==6:
            employee_menu()
        elif choice==7:
            shipping_menu()
        elif choice==8:
            payment_menu()
        elif choice==9:
            print("Exiting program...")
            mycon.close()
            break
        else:
            print("Invalid choice , please try again.")

def buyer_menu():
    print("\nBUYER DETAILS MENU")
    print("1. Insert Buyer Details")
    print("2. Update Buyer Details")
    print("3. Delete Buyer Details")
    print("4. View Buyer Details")
    print("5. Search Buyer Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        buyer_details_insert()
    elif choice == 2:
        buyer_details_update()
    elif choice == 3:
        buyer_details_delete()
    elif choice == 4:
        buyer_details_view()
    elif choice == 5:
        buyer_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def supplier_menu():
    print("\nSUPPLIER DETAILS MENU")
    print("1. Insert Supplier Details")
    print("2. Update Supplier  Details")
    print("3. Delete Supplier  Details")
    print("4. View Supplier details")
    print("5. Search Supplier  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        supplier_details_insert()
    elif choice == 2:
        supplier_details_update()
    elif choice == 3:
        supplier_details_delete()
    elif choice == 4:
        supplier_details_view()
    elif choice == 5:
        supplier_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def inventory_menu():
    print("\nINVENTORY DETAILS MENU")
    print("1. Insert Inventory Details")
    print("2. Update Inventory Details")
    print("3. Delete Inventory  Details")
    print("4. View Inventory details")
    print("5. Search Inventory  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        inventory_details_insert()
    elif choice == 2:
        inventory_details_update()
    elif choice == 3:
        inventory_details_delete()
    elif choice == 4:
        inventory_details_view()
    elif choice == 5:
        inventory_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def orders_menu():
    print("\nORDERS DETAILS MENU")
    print("1. Insert Orders Details")
    print("2. Update Orders Details")
    print("3. Delete Orders  Details")
    print("4. View Orders details")
    print("5. Search Orders  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        orders_details_insert()
    elif choice == 2:
        orders_details_update()
    elif choice == 3:
        orders_details_delete()
    elif choice == 4:
        orders_details_view()
    elif choice == 5:
        orders_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def supplier_orders_menu():
    print("\nSUPPLIER ORDERS DETAILS MENU")
    print("1. Insert Supplier Orders Details")
    print("2. Update Supplier Orders Details")
    print("3. Delete Supplier Orders  Details")
    print("4. View Supplier Orders details")
    print("5. Search Supplier Orders  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        supplier_order_details_insert()
    elif choice == 2:
        supplier_order_details_update()
    elif choice == 3:
        supplier_order_details_delete()
    elif choice == 4:
        supplier_order_details_view()
    elif choice == 5:
        supplier_order_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def employee_menu():
    print("\nEMPLOYEE ORDERS DETAILS MENU")
    print("1. Insert Employee Details")
    print("2. Update Employee Details")
    print("3. Delete Employee  Details")
    print("4. View Employee details")
    print("5. Search Employee  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        employee_details_insert()
    elif choice == 2:
        employee_details_update()
    elif choice == 3:
        employee_details_delete()
    elif choice == 4:
        employee_details_view()
    elif choice == 5:
        employee_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def shipping_menu():
    print("\nSHIPPING MENU")
    print("1. Insert Shipping Details")
    print("2. Update Shipping Details")
    print("3. Delete Shipping  Details")
    print("4. View Shipping details")
    print("5. Search Shipping  Details")
    print("6.  Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        shipping_details_insert()
    elif choice == 2:
        shipping_details_update()
    elif choice == 3:
        shipping_details_delete()
    elif choice == 4:
        shipping_details_view()
    elif choice == 5:
        shipping_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

def payment_menu():
    print("\nPAYMENTS MENU")
    print("1. Insert Payment Details")
    print("2. Update Payment Details")
    print("3. Delete Payment  Details")
    print("4. View Payment details")
    print("5. Search Payment  Details")
    print("6. Return to Main Menu")

    choice=int(input("enter your choice:  "))
    if choice == 1:
        payment_details_insert()
    elif choice == 2:
        payment_details_update()
    elif choice == 3:
        payment_details_delete()
    elif choice == 4:
        payment_details_view()
    elif choice == 5:
        payment_details_search()
    elif choice == 6:
        return
    else:
        print("Invalid choice , please try again.")

 # Start The Program
main_menu()
    
    
    
    
    
    
    
                         
            



