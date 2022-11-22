/*create a view to genearate ist of all the drugs that have been purchased */
CREATE VIEW purchased_drugs AS 
SELECT Dr_Name FROM drug where
drug.Dr_ID IN(SELECT Dr_ID from buys_or_generates join customer on buys_or_generates.C_ID = customer.C_ID);

select * from purchased_drugs;

/*query to list all information of drug that has been purchased*/
select * from drug where dr_name IN (select * from purchased_drugs);