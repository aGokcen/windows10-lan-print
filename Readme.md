## Windows 10 Printer Share Issue Solver

## How it Works?
The aim of the script is to print files from client PCs in Local Area Network(LAN). 
The script listens to a specific folder and seeks for PDF files. If the PDF file exists in the folder, script prints it. 
Clients have to put their files in the location which is listened by server, for this reason **Microsoft Print to PDF** virtual printer can be used to print files as a PDF.

The printing process of the client is almost the same as using a normal printer. 

## How to Use 

The program has to be run in pc (**Server**) which the printer is physically connected via USB or LPT etc.

A folder has to be shared in **Server** which write permission is given to Everyone. This folder will be used by clients.

The clients have to print file as a PDF document with using **Microsoft Print to PDF** virtual printer to the **Server** shared folder.  

The config file has to be configured before running.

```bash 
//How to run//
  python Server.py

```

## Config File

The config.ini file includes printer name and shared folder location, you have to edit this file to use your printer.


| Parameter | Type     | Value                |
| :-------- | :------- | :------------------------- |
| `printer_name` | `string` | **Required**. Name of the printer |
| `file_path` | `string` | **Required**. Path of the shared folder |
