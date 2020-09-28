BEGIN;

DROP TABLE notes;

CREATE TABLE notes(
    id integer NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    date text NOT NULL
);

INSERT INTO notes (id, name, author, date)
VALUES(id=1, name='README', author='Chris Blendermann', date='9/28/2020');

ALTER TABLE ONLY notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (name);

COMMIT;

ANALYZE notes;