DELIMITER $$
CREATE PROCEDURE findCUST(IN a1 VARCHAR(20))
BEGIN
select CUST_NAME from customer
where WORKING_AREA = a1;
END; $$


CALL findCust("Bangalore"); $$
