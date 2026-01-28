import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)

sheet = client.open("linkned post").sheet1   
data = sheet.get_all_records() 
counter = 1
#pp(data)

post = 'This is a test post from python script'
status = 'READY'

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
            break
        else:
            row += 1
            


def post_to_sheet(row):
    insertRow = [post,status]
    sheet.insert_row(insertRow,row)
   
    

if __name__ == "__main__":
    main()