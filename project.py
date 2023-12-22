print("   CBSE PROJECT OF INFORMATICS PRACTICES BY MANAN SHARMA")
print("   SOURCE:- Information & PR Department UT of Jammu & Kashmir")
print("   LINK:- https://twitter.com/diprjk/status/1558432400773767168")
print("   This project has been created by Manan Sharma of 12th D KV.no1 Udhampur")
print("   Data shown for illustrative purposes only")
print("   Data as of 13th August 2022")
print("   Lisenced Under GPL 3.0")
print("   An Open Source Project")
print("************************************************************************************************************************")
print("                       COVID ANALYSIS SYSTEM")
print("                       _____________________")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def creditfunc():
  print("           **********************************************************")
  print("           *  Created By Manan Sharma                               *")
  print('           *  Class:- 12th D                                        *')
  print('           *  Roll.no:- 15                                          *') 
  print('           *  Subject:- Informatics Practices                       *')
  print('           *  School:- Kendriya Vidyalaya No.1 Udhampur             *')
  print("           **********************************************************")

def showData():
  df=pd.read_csv("covid_19.csv")
  print(df)
  input("Press any key to continue....")

def dataNoIndex():
  df=pd.read_csv("covid_19.csv",index_col=0)
  print(df)
  input("Press any key to continue...")

def data_sorted():
  df=pd.read_csv('covid_19.csv')
  print(df.sort_values(by=['Confirmed']))
  
def write_data():
  print("Insert data of particular districts in list form:")
  di=eval(input("Enter Districts:"))
  con_cases=eval(input("Enter no. of confirmed cases:"))
  rec=eval(input("Enter no. of recovered cases:"))
  deaths=eval(input("Enter deaths:"))
  active=eval(input("Enter active cases:"))
  d={'Districts':di,'Confirmed':con_cases,'Recovered':rec,'Deaths':deaths,'Active':active}
  df=pd.DataFrame(d)
  df.to_csv('covid_19.csv', mode='a', index=False, header=False)
  print("Data has been added.")
  input("Press any key to continue...")

def edit_data():
  df=pd.read_csv("covid_19.csv")
  di=input("Enter district to edit:")
  col=input("Enter column name to update:")
  val=input("Enter new value")
  df.loc[df[df['Districts']==di].index.values,col]=val
  df.to_csv("covid_19.csv",index=False)
  print("Record has been updated...")
  input("Press any key to continue...")

def delete_data():
  di=input("Enter district to delete data:")
  df=pd.read_csv("covid_19.csv")
  df=df[df.Districts!=di]
  df.to_csv('covid_19.csv',index=False)
  print("Record deleted...")

  
def line_chart():
  df=pd.read_csv('covid_19.csv')
  District=df["Districts"]
  Confirmed=df["Confirmed"]
  Recovered=df["Recovered"]
  Deaths=df["Deaths"]
  Active=df["Active"]
  plt.xlabel("Districts")
  plt.xticks(rotation=90)
  Y=0
  while Y!=6:
      print("                                                   ")
      print("                             Line Graph Menu")
      print("                     ******************************")
      print("1.District wise Confirmed Cases ")
      print("2.District wise Recovered Cases ")
      print("3.District wise Death Cases")
      print("4.District wise Active Cases")
      print("5.All data")
      print("6.Return to main menu.")
      Y = int(input("Enter your choice to get line graph: "))
      if Y == 1:
          plt.ylabel("Confirmed Cases")
          plt.title("Districts Wise Confirmed Cases as on 13-8-2022")
          plt.plot(District, Confirmed, color='b')
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 2:
          plt.ylabel("Recovered Cases")
          plt.title("Districts Wise Recovered Cases as on 13-8-2022")
          plt.plot(District, Recovered, color='g')
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 3:
          plt.ylabel("Death Cases")
          plt.title("Districts Wise Death Cases as on 13-8-2022")
          plt.plot(District, Deaths, color='r')
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 4:
          plt.ylabel("Active Cases")
          plt.title("Districts Wise Active Cases as on 13-8-2022")
          plt.plot(District, Active, color='purple')
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 5:
          plt.ylabel("Number of cases")
          plt.title('Data as on 13-8-2022')
          plt.plot(District, Confirmed, color='b', label = "Districts Wise Confirmed Cases")
          plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
          plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
          plt.plot(District, Active, color='purple', label = "Districts Wise Active Cases")
          plt.legend()
          plt.xticks(rotation=90)
          plt.show()
      elif Y==6:
          print("Line Graph Closed.....")
          main_menu()
      else:
          print("Sorry!! Invalid Option! Try Again!!!")
          main_menu()
  
def bar_chart():
  df=pd.read_csv('covid_19.csv')
  District=df["Districts"]
  Confirmed=df["Confirmed"]
  Recovered=df["Recovered"]
  Deaths=df["Deaths"]
  Active=df["Active"]
  plt.xlabel("Districts")
  plt.xticks(rotation=90)
  print("                                                   ")
  print("                             Bar Graph Menu")
  print("                     ******************************")
  print("1. District Wise Confirmed Cases")
  print("2. District Wise Recovered Cases")
  print("3. District Wise Death Cases")
  print("4. District Wise Active Cases")
  print("5. All data")
  print("6. Combine Bar Graph")
  print("7. Return to main menu.")
  Y=0
  while Y!=5:
      Y = int(input("Enter your choice to get bar graph: "))
      if Y == 1:
          plt.ylabel("Confirmed Cases")
          plt.title("Districts Wise Confirmed Cases as Data as on 13-8-2022")
          plt.bar(District, Confirmed, color='blue', width = 0.5)
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 2:
          plt.ylabel("Recovered Cases")
          plt.title("Districts Wise Recovered Cases as Data as on 13-8-2022")
          plt.bar(District, Recovered, color='green', width = 0.5)
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 3:
          plt.ylabel("Death Cases")
          plt.title("Districts Wise Death Casesas Data as on 13-8-2022")
          plt.bar(District, Deaths, color='red', width = 0.5)
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 4:
          plt.ylabel("Active Cases")
          plt.title("Districts Wise Active Cases as Data as on 13-8-2022")
          plt.bar(District, Active, color='purple', width = 0.5)
          plt.xticks(rotation=90)
          plt.show()
      elif Y == 5:
          plt.bar(District, Confirmed, color='b', width = 0.5, label = "Districts Wise Confirmed Cases")
          plt.bar(District, Recovered, color='g', width = 0.5, label = "Districts Wise Recovered Cases")
          plt.bar(District, Deaths, color='r', width = 0.5, label = "Districts Wise Death Cases")
          plt.bar(District, Active, color='purple',width = 0.5, label = "Districts Wise Active Cases")
          plt.xticks(rotation=90)
          plt.legend()
          plt.show()
      elif Y == 6:
          D=np.arange(len(District))
          width=0.25
          plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
          plt.bar(D+0.25, Recovered, width, color='g', label = "Districts Wise Recovered Cases")
          plt.bar(D+0.50, Deaths, width, color='r', label = "Districts Wise Death Cases")
          plt.bar(D+0.75, Active ,width, color='purple', label = "Districts Wise Active Cases")
          plt.xticks(rotation=90)
          plt.legend()
          plt.show()
      elif Y==7:
        print("Bar Graph Closed.....")
        main_menu()
      else:
        print("Sorry!! Invalid Option! Try Again!!!")
        main_menu()

def main_menu():
  ch=0
  print("                                                   ")
  print("""                           [Main Menu]
                      [Created By Manan Sharma] """)
  while ch!=9:
    print("""
          0. Credits
          1. Show DataFrame
          2. Data without index
          3. Data in Ascending order of Confirmed cases
          4. Add district data into CSV
          5. Edit a record
          6. Delete a record
          7. Line Graph
          8. Bar Graph
          9. Exit
          """)
    ch=int(input("Enter your choice:"))
    if ch==0:
      creditfunc()
    elif ch==1:
      showData()
    elif ch==2:
      dataNoIndex()
    elif ch==4:
      write_data()
    elif ch==3:
      data_sorted()
    elif ch==5:
      edit_data()
    elif ch==6:
      delete_data()
    elif ch==7:
      line_chart()
    elif ch==8:
      bar_chart()
    elif ch==9:
      exit()
      break
main_menu()
