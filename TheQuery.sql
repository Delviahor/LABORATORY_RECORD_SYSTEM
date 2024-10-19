CREATE DATABASE CONTROL_LABORATORY_SYSTEM

CREATE TABLE tbl_administrator(
    id INT IDENTITY(1,1) PRIMARY KEY,
    admin_user VARCHAR(100) NOT NULL,
    admin_password VARCHAR(100) NOT NULL
);


INSERT INTO tbl_administrator(admin_user, admin_password) VALUES ('admin1', '12345678');


