import psycopg2 as connector


hostname='localhost'
database='demo'
username='postgres'
pwd='babai606'
port_id=5432

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host=hostname,dbname=database,user=username,password=pwd,port=port_id)
        query='''CREATE TABLE IF NOT EXISTS users (
                        ContactID       SERIAL PRIMARY KEY,
                        FirstName     varchar(200) NOT NULL,
                        LastName      varchar(200)NOT NULL,
                        Email         varchar(320),
                        PhoneNumber        varchar(14))'''
        cur=self.con.cursor()
        cur.execute(query)
        #print("Created")

    def insert_user(self,userid,FirstName,lastname,Email,phone):
        query="INSERT INTO users(ContactID,FirstName,LastName,Email,PhoneNumber) VALUES({},'{}','{}','{}','{}')".format(userid,FirstName,lastname,Email,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User save to Contact-Book")                  

    def fetch_all(self):
        query="select * from users;"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("ContactID :",row[0])
            print("FirstName :",row[1])
            print("LastName :",row[2])
            print("Email :",row[3])
            print("PhoneNumber :",row[4])            
            print()
            print()

    def fetch_one_by_id(self,userid):
        query="select * from users where ContactID={};".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("ContactID :",row[0])
            print("FirstName :",row[1])
            print("LastName :",row[2])
            print("Email :",row[3])
            print("PhoneNumber :",row[4])
            print()
            print() 

    def fetch_one_by_name(self,FirstName,LastName):
        query="select * from users where FirstName='{}' and LastName='{}';".format(FirstName,LastName)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("ContactID :",row[0])
            print("FirstName :",row[1])
            print("LastName :",row[2])
            print("Email :",row[3])
            print("PhoneNumber :",row[4]) 
            print()
            print()     

    def delete_user(self,userid):
        query="DELETE FROM users WHERE ContactID={}".format(userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Delete")  

    def  update_user_name(self,user_id,newfirstname,newlastname):
        
        query="UPDATE users SET FirstName='{}',LastName='{}' WHERE ContactID={}".format(newfirstname,newlastname,user_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")

    def  update_user_phone(self,user_id,newphone):
        
        query="UPDATE users SET PhoneNumber='{}' WHERE ContactID={}".format(newphone,user_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated") 

    def  update_user_email(self,user_id,newemail):
        
        query="UPDATE users SET Email='{}' WHERE ContactID={}".format(newemail,user_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")           


#helper = DBHelper()
#helper.insert_user(1,"Soumik","7362992606")
#helper.insert_user(2,"Ritika","9858662658")
#helper.delete_user(1)
#helper.fetch_all()

