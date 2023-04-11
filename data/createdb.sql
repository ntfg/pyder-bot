CREATE TABLE "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"user_id"	INTEGER UNIQUE,
	"name"	TEXT,
	"age"	INTEGER,
	"photo"	TEXT,
	"description"	TEXT,
	"telegram"	TEXT UNIQUE,
	PRIMARY KEY("id")
);