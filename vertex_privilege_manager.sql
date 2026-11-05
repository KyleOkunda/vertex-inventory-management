-- This file is managed by the root user in mysql to control actions of user vertex_admin on the database vertex_db
CREATE USER "vertex_admin"@"localhost" IDENTIFIED BY "vertex_admin";
GRANT CREATE, SELECT, UPDATE, DELETE, EVENT, CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON vertex_db.* TO "vertex_admin"@"localhost";