# Второе задание 
В одной таблице хранятся имена файлов без расширения. В другой хранятся имена файлов с
расширением. Одинаковых названий с разными расширениями быть не может, количество
расширений не определено, помимо wav и mp3 может встретиться что угодно.
Нам необходимо минимальным количеством запросов к СУБД перенести данные о статусе из
таблицы short_names в таблицу full_names.
___
## Решение
Вариант 1:
```sql
-- Обновление статуса в таблице full_names с использованием подзапроса
UPDATE full_names
SET status = s.status
FROM short_names s
WHERE full_names.name = s.name;
```
Вариант 2:
```sql
-- Создание временной таблицы и обновление статуса
CREATE TEMPORARY TABLE temp_table AS 
SELECT full_names.name, short_names.status 
FROM full_names 
JOIN short_names ON full_names.name = short_names.name;

UPDATE full_names 
SET status = temp_table.status 
FROM temp_table 
WHERE full_names.name = temp_table.name;

-- Удаление временной таблицы
DROP TABLE temp_table;
```
