--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: project; Type: TABLE; Schema: public; Owner: airportyh; Tablespace: 
--

CREATE TABLE project (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE project OWNER TO airportyh;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: airportyh
--

CREATE SEQUENCE project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE project_id_seq OWNER TO airportyh;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: airportyh
--

ALTER SEQUENCE project_id_seq OWNED BY project.id;


--
-- Name: project_uses_tech; Type: TABLE; Schema: public; Owner: airportyh; Tablespace: 
--

CREATE TABLE project_uses_tech (
    project_id integer NOT NULL,
    tech_id integer NOT NULL
);


ALTER TABLE project_uses_tech OWNER TO airportyh;

--
-- Name: tech; Type: TABLE; Schema: public; Owner: airportyh; Tablespace: 
--

CREATE TABLE tech (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE tech OWNER TO airportyh;

--
-- Name: tech_id_seq; Type: SEQUENCE; Schema: public; Owner: airportyh
--

CREATE SEQUENCE tech_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tech_id_seq OWNER TO airportyh;

--
-- Name: tech_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: airportyh
--

ALTER SEQUENCE tech_id_seq OWNED BY tech.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: airportyh
--

ALTER TABLE ONLY project ALTER COLUMN id SET DEFAULT nextval('project_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: airportyh
--

ALTER TABLE ONLY tech ALTER COLUMN id SET DEFAULT nextval('tech_id_seq'::regclass);


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: airportyh
--

COPY project (id, name) FROM stdin;
1	Coffee Store
2	Draw Together
3	Wiki
4	Tic Tac Toe
5	Todo List Angular
6	RPG Game
7	Memory Game
8	Rate the Throne
9	Sentimotion
10	Sportakus
11	Job Press
12	Whiteboarding
13	Basketball
\.


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: airportyh
--

SELECT pg_catalog.setval('project_id_seq', 13, true);


--
-- Data for Name: project_uses_tech; Type: TABLE DATA; Schema: public; Owner: airportyh
--

COPY project_uses_tech (project_id, tech_id) FROM stdin;
1	2
1	3
1	4
1	6
1	8
1	9
1	10
1	11
1	12
2	11
2	12
2	2
2	3
2	4
2	13
3	12
3	11
3	2
3	3
3	4
4	1
4	2
4	3
4	4
5	2
5	3
5	4
5	9
6	5
7	1
7	2
7	3
7	4
8	1
8	2
8	3
8	4
8	9
8	10
9	2
9	3
9	4
9	9
9	10
10	1
10	2
10	3
10	4
10	9
10	10
11	2
11	3
11	4
11	9
11	10
8	14
\.


--
-- Data for Name: tech; Type: TABLE DATA; Schema: public; Owner: airportyh
--

COPY tech (id, name) FROM stdin;
1	jQuery
2	JavaScript
3	HTML
4	CSS
5	Python
6	MongoDB
7	PostgreSQL
8	Mongoose
9	AngularJS
10	Bootstrap
11	Node.js
12	Express
13	Socket.IO
14	Animate.css
15	Ruby
16	Ruby on Rails
17	Java
18	C++
\.


--
-- Name: tech_id_seq; Type: SEQUENCE SET; Schema: public; Owner: airportyh
--

SELECT pg_catalog.setval('tech_id_seq', 18, true);


--
-- Name: project_pkey; Type: CONSTRAINT; Schema: public; Owner: airportyh; Tablespace: 
--

ALTER TABLE ONLY project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: project_uses_tech_pkey; Type: CONSTRAINT; Schema: public; Owner: airportyh; Tablespace: 
--

ALTER TABLE ONLY project_uses_tech
    ADD CONSTRAINT project_uses_tech_pkey PRIMARY KEY (project_id, tech_id);


--
-- Name: tech_pkey; Type: CONSTRAINT; Schema: public; Owner: airportyh; Tablespace: 
--

ALTER TABLE ONLY tech
    ADD CONSTRAINT tech_pkey PRIMARY KEY (id);


--
-- Name: project_uses_tech_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: airportyh
--

ALTER TABLE ONLY project_uses_tech
    ADD CONSTRAINT project_uses_tech_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: project_uses_tech_tech_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: airportyh
--

ALTER TABLE ONLY project_uses_tech
    ADD CONSTRAINT project_uses_tech_tech_id_fkey FOREIGN KEY (tech_id) REFERENCES tech(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: airportyh
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM airportyh;
GRANT ALL ON SCHEMA public TO airportyh;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

