import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from posts import POST_1, POST_2

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)

sheet = client.open("linkned post").sheet1   
data = sheet.get_all_records() 
counter = 1
#pp(data)

post = """"""
status = 'READY'
counter = 1

#insertRow = [post,status]
#sheet.insert_row(insertRow,counter)
#print("The row has been added")

# Posting to goggle sheet
def main ():
    # cell (2,1) is 2 row column 1
    row = 2
    column = 1
    print("Main function running")
    while True:
        if sheet.cell(row,column).value is None:
            print ("No post found")
            print (f"Posting in cell...{row},{column}")
            post_to_sheet(row)
            row += 1
            print (f"Posting in cell...{row},{column}")
            post_to_sheet(row)
            break
        else:
            row += 1
            


def post_to_sheet(row):
    global counter
    
    if counter == 1:
        post = POST_1
        counter += 1
    elif counter == 2:
        post = POST_2
        counter = 1

    insertRow = [post,status]
    sheet.insert_row(insertRow,row)
   
    

if __name__ == "__main__":
    main()