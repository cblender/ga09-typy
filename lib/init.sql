BEGIN;

CREATE TABLE notes(
    id integer NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    date timestamptz NOT NULL
);

COPY notes (id, name, author, date) FROM stdin;
1   README  Chris Blendermann   SELECT NOW()
2   TODO LIST   Somebody    SELECT NOW()
\.

ALTER TABLE ONLY notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (name);

COMMIT;

ANALYZE notes;