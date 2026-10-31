-- Write your query below
select name
from customers
left JOIN orders on orders.customer_id = customers.id
where orders.id is null;
