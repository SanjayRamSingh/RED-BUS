import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time
# kerala bus
lists_k=[]
df_k=pd.read_csv(r"D:\DATA SCIENCE\red\df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["routename"])
#Andhra bus
lists_A=[]
df_A=pd.read_csv(r"D:\DATA SCIENCE\red\df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["routename"])
#Telungana bus
lists_T=[]
df_T=pd.read_csv(r"D:\DATA SCIENCE\red\df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["routename"])
#Goa bus
lists_g=[]
df_G=pd.read_csv(r"D:\DATA SCIENCE\red\df_G.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["routename"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv(r"D:\DATA SCIENCE\red\df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["routename"])


# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv(r"D:\DATA SCIENCE\red\df_SB.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["routename"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv(r"D:\DATA SCIENCE\red\df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["routename"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv(r"D:\DATA SCIENCE\red\df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["routename"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv(r"D:\DATA SCIENCE\red\df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["routename"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv(r"D:\DATA SCIENCE\red\df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["routename"])
#setting up streamlit page
slt.set_page_config(layout="wide")
web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )
# Home page setting
if web=="Home":
    #slt.image("t_500x300.jpg",width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:]  Transportation")
    slt.subheader(":blue[Ojective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":blue[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed-by:]  sanjay")
# States and Routes page setting
if web == "📍States and Routes":
    S = slt.selectbox("Lists of States", ["Kerala", "Adhra Pradesh", "Telugana", "Goa", "Rajastan", 
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])
    col1,col2=slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME=slt.time_input("select the time")
    # Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{K}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    # Adhra Pradesh bus fare filtering
    if S == "Adhra Pradesh":
        A = slt.selectbox("List of routes",lists_A)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{A}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Telugana bus fare filtering
    if S == "Telugana":
        T = slt.selectbox("List of routes",lists_T)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{T}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Goa bus fare filtering
    if S == "Goa":
        G = slt.selectbox("List of routes",lists_g)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{G}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Rajastan bus fare filtering
    if S == "Rajastan":
        R = slt.selectbox("List of routes",lists_R)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{R}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #South Bengal bus fare filtering 
    if S == "South Bengal":
        SB = slt.selectbox("List of routes",lists_SB)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{SB}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Haryana bus fare filtering
    if S == "Haryana":
        H = slt.selectbox("List of routes",lists_H)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{H}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Assam bus fare filtering
    if S == "Assam":
        AS = slt.selectbox("List of routes",lists_AS)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{AS}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #Utrra Pradesh bus fare filtering
    if S == "Utrra Pradesh":
        UP = slt.selectbox("List of routes",lists_UP)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{UP}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)
    #West Bengal bus fare filtering
    if S == "West Bengal":
        WB = slt.selectbox("List of routes",lists_WB)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
                
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                    SELECT * FROM bus_details 
                    WHERE Price BETWEEN {fare_min} AND {fare_max}
                    AND routename = "{WB}"
                    AND bus_type={bus_type_condition} AND Start_time>='{TIME}'
                    ORDER BY Price and Start_time DESC
                '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                    "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                    "Price", "Seats_Available", "Ratings", "routename", "routelink"
                ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)