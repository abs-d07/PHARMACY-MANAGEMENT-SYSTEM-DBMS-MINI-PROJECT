/* GENERATE NAMES OF ALL USERS AND CUSTOMERS*/
SELECT u_name FROM user
UNION
SELECT c_name FROM customer;


/* LIST all the drug names which havent been sold*/
SELECT DR_NAME FROM drug
EXCEPT
SELECT DR_NAME FROM drug where dr_id IN(
SELECT dr.dr_id FROM Drug AS dr
INNER JOIN
buys_or_generates as bog
ON dr.dr_id=bog.dr_id);


/*generate drug_name and dr_id of all the medicines tat were sold*/
SELECT DR_NAME,dr_id FROM drug where dr_id IN(
SELECT dr_id FROM drug INTERSECT SELECT dr_id FROM buys_or_generates);