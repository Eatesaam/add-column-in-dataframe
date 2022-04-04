import pandas as pd
from datetime import datetime

def get_max_date(row):
    added_in_org = datetime.strptime(row['Added to org'], '%d %b %Y')
    
    last_seen_in_jira = row['Last seen in Jira Software - vfg-m']
    
    if last_seen_in_jira == "Never accessed":
        last_seen_in_jira = datetime.strptime("1 Jan 2000", '%d %b %Y')
    else:
        last_seen_in_jira = datetime.strptime(last_seen_in_jira, '%d %b %Y')
        
    last_seen_in_confluence = row['Last seen in Confluence - vfg-m']
    
    if last_seen_in_confluence == "Never accessed":
        last_seen_in_confluence = datetime.strptime("1 Jan 2000", '%d %b %Y')
    else:
        last_seen_in_confluence = datetime.strptime(last_seen_in_confluence, '%d %b %Y')
    
    max_date =  max([added_in_org, last_seen_in_jira, last_seen_in_confluence])
    
    return max_date

def convert_date_str(row):
    return row["last logged in"].strftime("%d %b %Y")

def main():
    df = pd.read_csv("export-users (20).csv")
    df["last logged in"] = df.apply(lambda row: get_max_date(row), axis=1)
    df = df.sort_values(by="last logged in")
    df["last logged in"] = df.apply(lambda row: convert_date_str(row), axis=1)
    df.to_csv("export-users-output.csv", index=False)
    print(df)
    

if __name__ == "__main__":
    main()