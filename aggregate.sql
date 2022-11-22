--Query to find the average MRP of drug present in store 
SELECT AVG(Dr_MRP) AS AVERAGE_MRP FROM Drug;

--Query to find the average cost price of Headache tablets.
SELECT AVG(Dr_Cost_Price) AS AVERAGE_COST_PRICE FROM drug WHERE Dr_Use='Headache';

--query to find the cheapest fever tablet available
select * from drug where dr_mrp = (SELECT MIN(Dr_MRP) FROM DRUG WHERE Dr_Type='TABLET' AND DR_USE='FEVER');

--query to find the costliest BP tablet available
select * from drug where dr_mrp = (SELECT MAX(Dr_MRP) FROM DRUG WHERE Dr_Type='TABLET' AND DR_USE='BP');