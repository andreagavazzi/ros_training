
| File Commands | |
| --- | --- |
|ls | Directory listing |
|ls -F | List files in current directory and indicate the file type |
|ls -al | Formatted listing with hidden files |
|cd dir | Change directory to dir |
|mkdir dir | Create a directory dir |
|pwd | Show current directory |
|rm name | Remove a file or directory called name |
|rm -r dir | Delete directory dir |
|rm -f file | Force remove file |
|rm -rf dir | Force remove an entire directory dir and all it’s included files and subdirectories  |
|cp file1 file2 | Copy file1 to file2 |
|cp -r dir1 dir2 | Copy dir1 to dir2; create dir2 if it doesn't exist |
|cp file /home/dirname | Copy the filename called file to the /home/dirname directory |
|mv file /home/dirname | Move the file called filename to the /home/dirname directory |
|mv file1 file2 | Rename or move file1 to file2; if file2 is an existing directory, moves file1 |into directory file2 |
|touch file |Create or update file |
|cat file | Display the file called file |


#### File Permissions
chmod octal file – Change the permissions of file to octal, which can be found separately for user, group, and world by adding: 4 – read (r), 2 
– write (w), 1 – execute (x)
Examples:
chmod 777 – read, write, execute for all
chmod 755 – rwx for owner, rx for group and world
For more options, see man chmod.

#### User Administration
adduser accountname – Create a new user call accountname
passwd accountname – Give accountname a new password
su – Log in as superuser from current login
exit – Stop being superuser and revert to normal user

#### SSH
ssh user@host – Connect to host as user
ssh -p port user@host – Connect to host on port port as user
ssh-copy-id user@host – Add your key to host for user to enable a keyed or passwordless login

#### System Info
date – Show the current date and time
cal – Show this month's calendar
uptime – Show current uptime
w – Display who is online
whoami – Who you are logged in as
finger user – Display information about user
uname -a – Show kernel information
cat /proc/cpuinfo – CPU information
cat /proc/meminfo – Memory information
df -h – Show disk usage
du – Show directory space usage
free – Show memory and swap usage

#### Searching
grep pattern files – Search for pattern in files
grep -r pattern dir – Search recursively for pattern in dir
command | grep pattern – Search for pattern in the output of command
locate file – Find all instances of file
find / -name filename – Starting with the root directory, look for the file called filename
find / -name ”*filename*” – Starting with the root directory, look for the file containing the string filename
locate filename – Find a file called filename using the locate command; this assumes you have already used the command updatedb (see 
next)
updatedb – Create or update the database of files on all file systems attached to the Linux root directory
which filename – Show the subdirectory containing the executable file  called filename
grep TextStringToFind /dir – Starting with the directory called dir, look for and list all files containing TextStringToFind

#### Network
ifconfig – List IP addresses for all devices on the local machine
iwconfig – Used to set the parameters of the network interface which are specific to the wireless operation (for example: the frequency)
iwlist – used to display some additional information from a wireless network interface that is not displayed by iwconfig
ping host – Ping host and output results
whois domain – Get whois information for domain
dig domain – Get DNS information for domain
dig -x host – Reverse lookup host
wget file – Download file
wget -c file – Continue a stopped download

#### Process Management
ps – Display your currently active processes
top – Display all running processes
kill pid – Kill process id pid
killall proc – Kill all processes named proc (use with extreme caution)
bg – Lists stopped or background jobs; resume a stopped job in the background
fg – Brings the most recent job to foreground
fg n – Brings job n to the foreground

#### Stopping & Starting
shutdown -h now – Shutdown the system now and do not reboot
halt – Stop all processes - same as above
shutdown -r 5 – Shutdown the system in 5 minutes and reboot
shutdown -r now – Shutdown the system now and reboot
reboot – Stop all processes and then reboot - same as above
startx – Start the X system

#### Installation from source
./configure
make
make install
dpkg -i pkg.deb – install a DEB package (Debian / Ubuntu / Linux Mint)
rpm -Uvh pkg.rpm – install a RPM package (Red Hat / Fedora)

___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=300)
