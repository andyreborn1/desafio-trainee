import os
import glob
from pathlib import Path
from pandas.io import json
import psycopg2
import pandas as pd
from sql_queries import *
from datetime import datetime


def process_song_file(cur, filepath):
    """Process song file.

    Args:
        cur: cusor of psycopg2.
        filepath: song file path (json).
    """

    # open song file
    song_file = pd.read_json(filepath, lines=True)

    # insert song record
    song_record = song_file[['song_id','title','artist_id','year','duration']].values.tolist()[0]
    
    cur.execute(song_table_insert, song_record)

    # insert artist record
    artist_record = song_file[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values.tolist()[0]

    cur.execute(artist_table_insert, artist_record)


def process_log_file(cur, filepath):
    """Process log file.

    Args:
        curL cusor of psycopg2.
        filepath: log file path (json).
    """

    # open log file
    log_file = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    log_file = log_file.loc[log_file["page"] == "NextSong"]

    # convert timestamp column to datetime
    time = pd.to_datetime(log_file["ts"], unit="ms")

    # insert time data records
    for value in time:
        time_table = [datetime.timestamp(value), value.hour, value.day, value.week, value.month, value.year, value.weekday()]
        cur.execute(time_table_insert,time_table)


    # load user table
    user_record = log_file[['userId','firstName','lastName','gender','level']].values.tolist()

    # insert user records
    for log in user_record:
        cur.execute(user_table_insert, log)

    # insert songplay records
    for index, row in log_file.iterrows():
        cur.execute(select_ids,(row['artist'],row['song']))
        ids = cur.fetchone()
        
        if ids:
            artist_id, song_id = ids
        else:
            artist_id, song_id = 'None', 'None'
        
        songplay_record = (row.ts, row.userId, row.level, song_id, artist_id, row.sessionId, row.location, row.userAgent)
        
        cur.execute(songplay_table_insert,songplay_record)


def process_data(cur, conn, filepath, func):
    """Process data.

    Args:
        cur: cursor of psycopg2.
        conn: connection of postgresql.
        filepath: directory path of data.
        func: function of processing.
    """
    
    # get all files matching extension from directory
    all_path = glob.glob(filepath + "/**/*.json", recursive=True)

    # get total number of files found
    total = len(all_path)

    # iterate over files and process
    for path in all_path:
        func(cur, path)

    conn.commit()


def main():
    conn = psycopg2.connect(
        database="sparkifydb",
        user="student",
        password="student",
        host="127.0.0.1",
        port="5432",
    )
    
    cur = conn.cursor()

    process_data(cur, conn, filepath="data/song_data", func=process_song_file)
    process_data(cur, conn, filepath="data/log_data", func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
