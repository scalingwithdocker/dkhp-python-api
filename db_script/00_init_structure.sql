

-- CREATE TABLE "students" -------------------------------------
CREATE TABLE "public"."students" (
	"id" SERIAL NOT NULL,
	"name" Text NOT NULL,
	"code" Text  UNIQUE,

	PRIMARY KEY ( "id" ) );
 ;
-- -------------------------------------------------------------

-- CREATE TABLE "courses" -----------------------------------------
CREATE TABLE "public"."courses" (
	"id" SERIAL NOT NULL,
	"name" Text NOT NULL,
	"code" Text  UNIQUE,
	PRIMARY KEY ( "id" ) );
 ;
-- -------------------------------------------------------------

-- CREATE TABLE "classes" -----------------------------------------
CREATE TABLE "public"."classes" (
	"id" SERIAL NOT NULL,
	"name" Text NOT NULL  ,
	"code" Text  UNIQUE,
	PRIMARY KEY ( "id" ) );
 ;
-- -------------------------------------------------------------

-- CREATE TABLE "student_course_resgitry" -----------------------------------------
CREATE TABLE "student_course_resgitry" (
	"id" SERIAL NOT NULL,
	"student_code" Text NOT NULL,
	"class_code" Text NOT NULL,

	PRIMARY KEY ( "id" ) ,
	FOREIGN KEY (student_code) REFERENCES students (code),
	FOREIGN KEY (class_code) REFERENCES classes (code))
 ;
-- -------------------------------------------------------------

