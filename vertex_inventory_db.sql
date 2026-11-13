-- This file is managed by the user vertex_admin, permissions of this user are controlled by root admin
CREATE DATABASE IF NOT EXISTS vertex_db;
USE vertdjango_migrationsex_db;

CREATE TABLE IF NOT EXISTS vertex_users(
	user_id varchar(36) primary key,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    phone_number varchar(10) not null,
    email varchar(50) not null,
    user_role varchar(30) not null,
    position varchar(30) not null,
    account_created_by varchar(36) not null,
    date_account_created datetime default now(),
    last_login datetime null,
    user_password varchar(60) not null
    );
    