# PLATFORM SURVEILLANCE SYSTEM

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

#---------------Email Sender Credentials-----------------------------
SENDER_EMAIL="152004.sanika@gmail.com"
SENDER_PASSWARD="tebybbjxecsgeqpa"

#---------------------Create Log File--------------------------------
def CreateLog(Folder_name, ReceiverEmail):
    print("\nGenerating system report at :", time.ctime())

    if not os.path.exists(Folder_name):
        os.mkdir(Folder_name)
        print("Folder created successfully",Folder_name)
    else:
        print("Folder already exists :",Folder_name)

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(Folder_name,f"Marvellous_{timestamp}.log")
    print("Log file will be created as :", FileName)

    fobj=open(FileName,"w")

    Border="-"*60
    fobj.write(Border + "\n")
    fobj.write("Platform Surveillance System\n")
    fobj.write("Log Created At : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    # Process Scan
    Data= Process_Scan()

    total_process=len(Data)
    print("Total running processes :",total_process)

    top_memory=sorted(Data, key=lambda x: x["memory_percent"], reverse=True)[:10]
    top_cpu=sorted(Data, key=lambda x: x["cpu_percent"], reverse=True)[:5]
    top_threads=sorted(Data, key=lambda x: x["threads"], reverse=True)[:5]
    top_files=sorted(Data, key=lambda x: x["open_files"], reverse=True)[:5]

    fobj.write(f"\nTotal Process : {total_process}\n")
    fobj.write(Border + "\n")

    # Write process details
    for info in Data:
        fobj.write(f"PID : {info['pid']}\n")
        fobj.write(f"Name : {info['name']}\n")
        fobj.write(f"Threads : {info['threads']}\n")

        if info['open_files'] == -1:
            fobj.write("Open Files : Access Denied\n")
        else:
            fobj.write(f"Open Files : {info['open_files']}\n")

        fobj.write(f"RSS Memory : {info['rss']}\n")
        fobj.write(f"VMS Memory : {info['vms']}\n")
        fobj.write(f"Memory Percent : {info['memory_percent']:.2f}\n")
        fobj.write(Border + "\n")

    fobj.close()

    # send email report
    Send_mail(FileName,ReceiverEmail, total_process, top_cpu, top_memory, top_threads, top_files)

# Process Monitoring
def Process_Scan():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["pid","name"])

            # CPU and Memory 
            info["cpu_percent"]=proc.cpu_percent(interval=0.1)
            info["memory_percent"]=proc.memory_percent()

            mem=proc.memory_info()
            info["rss"]=round(mem.rss / (1024 * 1024),2)
            info["vms"]=round(mem.vms / (1024 * 1024),2)

            # Thread Count
            info["threads"]=proc.num_threads()

            # Open files count
            try:
                info["open_files"]=len(proc.open_files())
            except psutil.AccessDenied:
                info["open_files"]=-1
            except:
                info["open_files"]=0

            listprocess.append(info)

        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue

    return listprocess

# Email Sending Function
def Send_mail(FileName,ReceiverEmail, total_process, top_cpu, top_memory, top_threads, top_files):

    print("Preparing to send email report...")
    try:
        
        msg=EmailMessage()
        msg["Subject"]="System Monitoring Report"
        msg["From"]=SENDER_EMAIL
        msg["To"]=ReceiverEmail

        body=f"""System Monitorig Report
        Total Processes : {total_process}
        """
        msg.set_content(body)
        # Attach file 
        with open(FileName,"rb") as f:
            file_data= f.read()

            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=os.path.basename(FileName))

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWARD)
            smtp.send_message(msg)

        print("Email Sent Successfully to :", ReceiverEmail)

    except Exception as e:
        print("Email Sending Failed :",e)

def main():

    if len(sys.argv) != 4:
        print("Usage :")
        print('Python surveillance.py "FolderName" "ReceiverEmail", TimeInterval')
        return
    
    FolderName=sys.argv[1]
    ReceiverEmail=sys.argv[2]
    TimeInterval=int(sys.argv[3])

    schedule.every(TimeInterval).minutes.do(CreateLog, FolderName, ReceiverEmail)

    print("Surveillance System Started...")
    print("Monitoring started at :",time.ctime())
    print("Time interval (Minutes) :",TimeInterval)
    print("Logs will be stored in :",FolderName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()
        