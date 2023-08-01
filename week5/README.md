## 要求三：SQL CRUD
1.使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-1.png)
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-1-1.png)

2.使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-2.png)

3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-3.png)

4.使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄
位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-5.png)

6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-6.png)

7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改
成 test2。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/3-7.png)

## 要求四：SQL Aggregate Functions
1.取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/4-1.png)

2.取得 member 資料表中，所有會員 follower_count 欄位的總和。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/4-2.png)

3.取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/4-3.png)

## 要求五:SQL JOIN
1. 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以
下欄位設定:
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/5-1.png)
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/5-1-1.png)

2.使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/5-2.png)

3.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/5-3.png)

4.使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
![image](https://github.com/ismeleft/wehelp-stage1/blob/main/week5/%E6%AD%A5%E9%A9%9F%E6%88%AA%E5%9C%96/5-4.png)
   
