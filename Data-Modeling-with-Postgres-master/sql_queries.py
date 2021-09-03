# DROP TABLES
songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"


# CREATE TABLES
songplay_table_create = "create table songplays (songplay_id integer not null primary key, start_time bigint not null, user_id varchar(20) not null, level varchar(10) not null, song_id varchar(20), artist_id varchar(20), session_id integer not null, lcation varchar(100), user_agent varchar(255))"
user_table_create = "create table users (user_id varchar(20) not null primary key, first_name varchar(100) not null, last_name varchar(100) not null, gender varchar(1),level varchar(10) not null)"
song_table_create = "create table songs (song_id varchar(20) not null primary key,title varchar(100) not null,artist_id varchar(20) not null,year integer,duration double precision not null)"
artist_table_create = "create table artists (artist_id varchar(20) not null primary key,name varchar(100) not null,location varchar(100),latitude double precision,longitude double precision)"
time_table_create = "create table time (start_time bigint not null primary key, hour integer not null, day integer not null, week integer not null, month integer not null, year integer not null, weekday integer not null)"


# INSERT RECORDS


# FIND SONGS


# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
