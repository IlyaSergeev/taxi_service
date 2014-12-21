BEGIN;

CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
CREATE INDEX django_admin_log_417f1b1c ON "django_admin_log" ("content_type_id");
CREATE INDEX django_admin_log_e8701ad4 ON "django_admin_log" ("user_id");

CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
CREATE INDEX auth_permission_417f1b1c ON "auth_permission" ("content_type_id");
CREATE INDEX auth_group_permissions_0e939a4f ON "auth_group_permissions" ("group_id");
CREATE INDEX auth_group_permissions_8373b171 ON "auth_group_permissions" ("permission_id");
CREATE INDEX auth_user_groups_e8701ad4 ON "auth_user_groups" ("user_id");
CREATE INDEX auth_user_groups_0e939a4f ON "auth_user_groups" ("group_id");
CREATE INDEX auth_user_user_permissions_e8701ad4 ON "auth_user_user_permissions" ("user_id");
CREATE INDEX auth_user_user_permissions_8373b171 ON "auth_user_user_permissions" ("permission_id");

CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE TABLE "django_content_type__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type__new" ("model", "app_label", "id", "name") SELECT "model", "app_label", "id", "name" FROM "django_content_type";
DROP TABLE "django_content_type";
ALTER TABLE "django_content_type__new" RENAME TO "django_content_type";

CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX django_session_de54fa62 ON "django_session" ("expire_date");



CREATE TABLE "TaxiService_car" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "brand" varchar(64) NULL, "model" varchar(64) NULL, "color" varchar(64) NOT NULL, "reg_number" varchar(16) NOT NULL UNIQUE);
CREATE TABLE "TaxiService_driver" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "account_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"), "car_id" integer NOT NULL UNIQUE REFERENCES "TaxiService_car" ("id"));
CREATE TABLE "TaxiService_ride" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fromAddress" varchar(256) NOT NULL, "toAddress" varchar(256) NOT NULL, "date" datetime NOT NULL, "car_id" integer NOT NULL REFERENCES "TaxiService_car" ("id"));
CREATE INDEX TaxiService_ride_cf8b1f8d ON "TaxiService_ride" ("car_id");

COMMIT;
