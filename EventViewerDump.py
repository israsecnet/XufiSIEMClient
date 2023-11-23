import codecs
import os
import sys
import time
import traceback
import json
import win32.lib.win32con as win32con
import win32.win32evtlog as win32evtlog
import win32.lib.win32evtlogutil as win32evtlogutil
import win32.lib.winerror as winerror

#Saves windows security, application, and system events from event viewer to 3 separate json files

def get_event_logs(event_log_type, log_file, output_file):
    event_logs = []

    hand = win32evtlog.OpenEventLog(None, event_log_type)
    total_records = win32evtlog.GetNumberOfEventLogRecords(hand)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    
    for event in events:
        event_dict = {
            "Record Number": event.RecordNumber,
            "Time Generated": str(event.TimeGenerated),
            "Event Type": event.EventType,
            "Event Category": event.EventCategory,
            "Source Name": event.SourceName,
            "Event ID": event.EventID,
            "Computer Name": event.ComputerName,
            "Data": event.StringInserts
        }
        event_logs.append(event_dict)

    win32evtlog.CloseEventLog(hand)

    # Save event logs to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(event_logs, json_file, indent=4)

def main():
    log_file = "System"  # Name of the log file
    output_file = f"event_logs_{log_file}.json"  # JSON output file

    get_event_logs(log_file, log_file, output_file)
    print(f"Event logs from '{log_file}' saved to '{output_file}'")
    
      # You can change this to Security, System, etc.
    log_file = "Application"  # Name of the log file
    output_file = f"event_logs_{log_file}.json"  # JSON output file
    
    get_event_logs(log_file, log_file, output_file)
    print(f"Event logs from '{log_file}' saved to '{output_file}'")

    log_file = "Security"  # Name of the log file
    output_file = f"event_logs_{log_file}.json"  # JSON output file
    
    get_event_logs(log_file, log_file, output_file)
    print(f"Event logs from '{log_file}' saved to '{output_file}'")