-- Delimiter $$
Delimiter $$
CREATE PROCEDURE getdetails()
BEGIN
   DECLARE finished INT DEFAULT 0;
   DECLARE grade1 decimal DEFAULT 0;
   DECLARE cust_name1 VARCHAR(255) DEFAULT "";
   DECLARE city1 VARCHAR(255) DEFAULT "";
   DECLARE Country1 VARCHAR(255) DEFAULT "";
   DECLARE cur CURSOR FOR
   SELECT GRADE,CUST_CITY, CUST_NAME,CUST_COUNTRY FROM customer;
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
   OPEN cur;
   label:LOOP
   FETCH cur INTO grade1,cust_name1,city1,Country1;
   IF done = 1 THEN LEAVE label;
   END IF;
   SELECT grade1,cust_name1,city1,Country1;
   END LOOP label;
   CLOSE cur;
END $$
call getdetails(); $$



