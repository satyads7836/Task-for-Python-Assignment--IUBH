import sqlalchemy as db
import sqlite3 as sql
from sqlalchemy import create_engine, Table, Column, MetaData
import pandas as pd
import numpy as np
import glob
import os


def main():
   
    df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('',"*.csv"))), ignore_index=True)
    #print (df)

    #conn = sqlite3.connect('test.db')
    #print(conn)

    try:
        #engine = create_engine('sqlite:///satya.db', echo=True)
        conn = sql.connect('satya.db')
        df.to_sql('satya_table',conn)
    except:
        print("Failed to create engine.")

    cn = sql.connect('satya.db')
    nug_df = pd.read_sql('select * from satya_table where Y1="YYY1"', cn)
    print(nug_df)

    #SQLalchemy time
    #df.to_sql('nug_table', con=engine, index=True, index_label='id', if_exists='replace')

  
if __name__ == '__main__':
    main()