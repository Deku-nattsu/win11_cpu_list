from bs4 import BeautifulSoup
import requests

def main():
    try:
        print("getting supported cpus list....")
        with open("supported-amd.txt", "w") as f:
            print("writing supported amd list..")
            f.writelines(line + '\n' for line in cpu_list(0))
            print("done.")
        with open("supported-intel.txt", "w") as f:
            print("writing supported intel list..")
            f.writelines(line + '\n' for line in cpu_list(1))
            print("done.")
        with open("supported-qcom.txt", "w") as f:
            print("writing supported qcom list..")
            f.writelines(line + '\n' for line in cpu_list(2))
            print("done.")
    except ConnectionError:
        print("Connection Error please try later")

def cpu_list(type : int) -> list:
    if(type == 0):
        url = "https://docs.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-amd-processors"
    elif(type == 1):
        url = "https://docs.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors"
    else:
        url = "https://docs.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-qualcomm-processors"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    tbody = soup.find('tbody')
    tr = tbody.findChildren("tr")
    j = [str(cpu).strip('<tr>').replace('<td>','').replace('</td>','').split('\n') for cpu in tr]
    return [cpu[2] + " " + cpu[3] for cpu in j]

if __name__ == "__main__":
    main()