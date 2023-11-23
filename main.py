import json, os, threading, time, requests, EventViewerDump, SecurityStance

SERVERURI = os.environ['LOGSERVERURI']
LOGSERVER = SERVERURI + "/logingestor/"
AGENTID = 2
headers = {'Content-Type': 'application/json'}
securitySettings = {}

def healthCheckPing():
    while True:
        response = requests.get(SERVERURI + "/healthcheck/?agentid=" + str(AGENTID), headers=headers)
        print(response.text)
        time.sleep(30)        
        
def refreshFunctionHelper(rate, func):
    while True:
        func
        time.sleep(rate)
        
def read_into_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    with open('agent_settings.json', 'r') as f:
        securitySettings = json.load(f)        
    threadSS = threading.Thread(target=refreshFunctionHelper, args=(securitySettings[0]["Log Collection Settings"]["SecurityStanceRefresh"], SecurityStance.main()))
    threadEVD = threading.Thread(target=refreshFunctionHelper, args=(securitySettings[0]["Log Collection Settings"]["EventViewerDumpRefresh"], EventViewerDump.main()))
    threadHP = threading.Thread(target=healthCheckPing, args=())
    threadSS.daemon, threadEVD.daemon, threadHP.daemon = True, True, True
    threadSS.start()
    threadEVD.start()
    threadHP.start()
    
    try:
        tmp = read_into_json('system_info.json')
        tmpea = read_into_json('event_logs_Application.json')
        tmpes = read_into_json('event_logs_Security.json')
        tmpesys = read_into_json('event_logs_System.json')
        tmpao = read_into_json('AgentOverview.json')
        tmpao["XUFIAGENTID"] = AGENTID
        tmpao["XUFILOGTYPE"] = "AgentOverview"
        response = requests.post(LOGSERVER, data=json.dumps(tmpao), headers=headers)
        tmp["XUFIAGENTID"] = AGENTID
        tmp["XUFILOGTYPE"] = "SystemInfo"
        for i in tmpea:
            i["XUFILOGTYPE"] = "EventViewerApplication"
            i["XUFIAGENTID"] = AGENTID
            response = requests.post(LOGSERVER, data=json.dumps(i), headers=headers)
        for i in tmpes:
            i["XUFILOGTYPE"] = "EventViewerSecurity"
            i["XUFIAGENTID"] = AGENTID
            response = requests.post(LOGSERVER, data=json.dumps(i), headers=headers)
        for i in tmpesys:
            i["XUFILOGTYPE"] = "EventViewerSystem"
            i["XUFIAGENTID"] = AGENTID
            response = requests.post(LOGSERVER, data=json.dumps(i), headers=headers)
        tmp2 = json.dumps(tmp)
        response = requests.post(LOGSERVER, data=tmp2, headers=headers)
        
        if response.status_code == 200:
            print('Request was successful')
            print(response.json())  # If the response is in JSON format
        else:
            print(f'Request failed with status code {response.status_code}')
            print(response.text)  # Print the response content for further debugging
            
    except KeyboardInterrupt:
        print("Shutting down client...")
            