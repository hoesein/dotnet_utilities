#!/usr/bin/env python3

service_file_content = """
[Unit]
Description={service_name}

[Service]
WorkingDirectory={working_directory}
ExecStart={dotnet_location} {dll_location}
Restart=always
RestartSec=10
KillSignal=SIGINT
SyslogIdentifier=dotnet-kestrel-service
User={user}
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false
Environment=ASPNETCORE_URLS=http://*:{port}

[Install]
WantedBy=multi-user.target
"""
service_name = input("Enter the service name: ")
working_directory = input("Enter the working directory for the service: ")
dotnet_location = input("Enter the dotnet location: ")
dll_location = input("Enter the dll location: ")

user = input("Enter the user for the service: ")
file_name = input("Enter file name: ")
port = input("Enter listen port: ")

service_file_content = service_file_content.format(
    service_name = service_name,
    working_directory = working_directory,
    dotnet_location = dotnet_location,
    dll_location = dll_location,
    user = user,
    port = port
)

with open(f"{file_name}.service", "w") as service_file:
    service_file.write(service_file_content)

print("Service file generated successfully!")
