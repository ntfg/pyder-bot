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

CREATE TABLE "matches" (
	"id"	INTEGER NOT NULL UNIQUE,
	"send"	INTEGER,
	"receive"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);