FROM mcr.microsoft.com/dotnet/aspnet:6.0
EXPOSE 8081
ENV ASPNETCORE_URLS=http://+:8081

COPY . ./{dir}
WORKDIR /{dir}
ENTRYPOINT ["dotnet", "{some_file}.Api.dll"]
