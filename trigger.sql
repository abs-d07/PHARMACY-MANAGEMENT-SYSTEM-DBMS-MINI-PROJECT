delimiter //
CREATE TRIGGER drugs_before_insert BEFORE INSERT
ON drug
FOR EACH ROW
IF NEW.Dr_DOE < CURDATE() +7 THEN
SIGNAL SQLSTATE '50001' SET MESSAGE_TEXT = 'The drug you are trying to add to the database has a near expiry within 7 days.Kindly return or exchange it from the distributor ';
END IF; 
//
delimiter ;
INSERT INTO drug VALUES ('Glycomet GP 2','D60','2022-10-12','2022-11-20','190','150','Tablet','Sugar','3','8','123');


DELIMITER //

CREATE FUNCTION no_of_years(date1 date) RETURNS int DETERMINISTIC
BEGIN
 DECLARE date2 DATE;
  Select current_date()into date2;
  RETURN year(date1)-year(date2);
END 

//

DELIMITER ;

Select Dr_id, dr_name, Dr_MRP, no_of_years(Dr_DOE) as 'years_remaining' from drug;