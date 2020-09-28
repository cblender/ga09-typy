BEGIN;

CREATE TABLE notes(
    id integer NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    date text NOT NULL
);

INSERT INTO notes (id, name, author, date)
VALUES(1, 'README', 'Chris Blendermann', '9/28/2020');

ALTER TABLE ONLY notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (name);

COMMIT;

ANALYZE notes;