DELIMITER $$
CREATE  PROCEDURE greaterthan10000()
BEGIN
select CUST_NAME, GRADE from customer
where OPENING_AMT+RECEIVE_AMT > 10000;
END; $$

CALL greaterthan10000; $$
