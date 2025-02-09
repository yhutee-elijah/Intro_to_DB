-- Select the correct database
USE alx_book_store;

-- Get full details of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books' AND TABLE_SCHEMA = DATABASE();
