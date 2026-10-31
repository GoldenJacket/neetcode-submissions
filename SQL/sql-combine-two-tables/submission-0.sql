-- Write your query below
Select first_name,last_name, city, state
from person
left join address on address.person_id = person.person_id;