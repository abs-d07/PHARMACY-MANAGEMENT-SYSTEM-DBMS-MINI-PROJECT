
---JOIN 1
--All the drugs distributed by Distributor with d_id=8
SELECT * FROM Drug AS dr
INNER JOIN
distributor as d 
ON d.d_id=dr.d_id AND dr.D_id='8';


--JOIN 2
--List all the Distributor name,d_id and drug name  who distributed Headache tablets 
SELECT d.D_Name,d.d_id,dr.Dr_Name FROM Distributor as d
INNER JOIN 
Drug AS dr
ON d.d_id=dr.d_id AND Dr_Use='Headache';


--JOIN 3 
/* List names of customers who have purchased fever tablets distributed by distributor_id=12*/
SELECT DISTINCT C_NAME FROM CUSTOMER WHERE C_ID IN (
SELECT C_ID FROM buys_or_generates where
dr_id IN(SELECT Dr_ID from DRUG join Distributor on Distributor.D_ID = drug.D_ID where Dr_Type= 'Tablet' and Dr_Use='Fever' AND distributor.d_id='12'));


--JOIN 4
/*DISPLAY ALL THE names of DRUGs which have been purchased by male customers*/
SELECT Dr_Name FROM drug where
drug.Dr_ID IN(SELECT Dr_ID from buys_or_generates join customer on buys_or_generates.C_ID = customer.C_ID where C_Gender= 'male');


--JOIN5
/*DISPLAY ALL THE DRUGS WITH THEIR MRP WHICH Were INVOLVED IN AN INVOICE WHERE the BILL AMOUNT WAS >50*/
SELECT Dr_Name,dr_mrp from drug as dr
INNER JOIN
buys_or_generates as bog 
ON dr.Dr_ID = bog.Dr_ID
INNER JOIN
invoice as i
ON bog.i_no = i.i_no
where I.I_Bill_Amount>50;


--JOIN 6
/*LIST ALL THE CUSTOMERS NAME AND THEIR CUSTOMER ID WHO PURCHASED drugs distributed by the distributor with d_id='8' */
SELECT c.C_Name, c.C_ID FROM customer AS c 
INNER JOIN 
buys_or_generates as bog 
ON bog.c_id = c.C_ID
INNER JOIN 
drug as dr
ON dr.Dr_ID = bog.Dr_ID
INNER JOIN 
Distributor as d
ON d.d_id = dr.d_id
WHERE d.d_id='16';



