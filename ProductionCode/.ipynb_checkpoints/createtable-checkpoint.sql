DROP TABLE IF EXISTS mammals_table;
CREATE TABLE mammals_table (
 id int,
  observed_on timestamp,
  lattitude double precision,
  longitude double precision,
  common_name text,
  iconic_taxon text,
  place_guess text,
  observer text,
  url text
);