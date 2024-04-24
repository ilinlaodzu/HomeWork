DELIMITER //
CREATE FUNCTION format_seconds(sec INT)
RETURNS VARCHAR(255)
deterministic
BEGIN
    DECLARE days INT;
    DECLARE hours INT;
    DECLARE minutes INT;
    DECLARE seconds INT;
    DECLARE result VARCHAR(255);
    SET days = FLOOR(sec / 86400);
    SET sec = sec - days * 86400;
    SET hours = FLOOR(sec / 3600);
    SET sec = sec - hours * 3600;
    SET minutes = FLOOR(sec / 60);
    SET seconds = sec - minutes * 60;
    SET result = CONCAT(days, ' days ', hours, ' hours ', minutes, ' minutes ', seconds, ' seconds');
    RETURN result;
END //times
DELIMITER ;

select  format_seconds(123)

SELECT * FROM (
    SELECT 1 AS number UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10
) AS numbers
WHERE number % 2 = 0;

