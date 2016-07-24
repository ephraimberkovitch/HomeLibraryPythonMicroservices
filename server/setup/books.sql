create table books(BookId integer primary key autoincrement, writers text,title text,series text, copies integer,
volumes integer,date_created datetime default current_timestamp);