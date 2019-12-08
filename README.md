# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Getting Started
Windows 10 users, please install WSL on your system. Linux or Mac users can directly start from step 1.

Step 1: Install Visual Studio Code and open it. Run terminal in Visual Studio Code by pressing Shift + ‘~’. 
[Note: Windows 10 users are required to run WSL on the terminal before implementing Step 2]

Step 2: Install Python3 and pip: sudo apt install python3 python3-pip ipython3

Step 3: Install django: sudo apt install django

Step 4: Install virtual environment: sudo apt install virtualenv

Step 5: Create a virtual environment: virtualenv ENV

Step 6: Activate your virtual environment: source /ENV/bin/activate

Step 7: Copy repository from git: git clone this repo

Step 8: Navigate to HH directory to run requirement.txt file. This will install all the other extensions and shells required to run the code.(sudo apt install -r requirement.txt)

Step 9: Install postgres sql for database server: sudo apt-get install postgres or sudo -u postgres psql 

Step 10: Start postgres: 
On Mac: pg_ctl -D /usr/local/var/postgres start
On Windows: pg_ctl -D "C:\Program Files\PostgreSQL\9.6\data" start
On Linux: sudo service postgresql start

Step 11: Initiate migrations: python3 manage.py makemigrations (this should be done in the project folder)

Step 12: Run migrations: python3 manage.py migrate

Step  13: Run application: python3 manage.py runserver 



# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)
