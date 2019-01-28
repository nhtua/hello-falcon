BEGIN;

-- CREATE TABLE "customer" -------------------------------------
CREATE TABLE "public"."customer" (
	"id" SERIAL NOT NULL,
	"name" Character Varying( 64 ) NOT NULL,
	"dob" Date NOT NULL,
	"meta" JSONB DEFAULT '{}'::jsonb NOT NULL,
	"created_at" Timestamp With Time Zone NOT NULL,
	"updated_at" Timestamp With Time Zone DEFAULT now(),
	PRIMARY KEY ( "id" ) );
 ;
-- -------------------------------------------------------------

-- CREATE TABLE "user" -----------------------------------------
CREATE TABLE "public"."user" (
	"id" SERIAL NOT NULL,
	"username" Character Varying( 64 ) NOT NULL,
	"password" Character Varying( 64 ) NOT NULL,
	"created_at" Timestamp With Time Zone NOT NULL,
	"updated_at" Timestamp With Time Zone DEFAULT now(),
	PRIMARY KEY ( "id" ) );
 ;
-- -------------------------------------------------------------

COMMIT;
