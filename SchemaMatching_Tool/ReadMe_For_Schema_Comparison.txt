#####----- step should be followed for desired output-------####


***"setup.txt" must be followed as mention below
Step:

    A>ServerName --> first line must be servername "without any space" for example-> ServerName:YJAIN9
    B>DatabaseName --> Second line must be database name "without any space" for example-> DbName:CoreIssueArchival_primary


***"Parameter.txt" Will contain all the table name(Every table should be in newline without any space) for which you want to generate schema


### Execution must be as it is mentioned

1> First run the "BaseTable_Schema.exe" file
2> Second run the "NewTable_Schema.exe" file
  A> above file(NewTable_Schema.exe) will call "Compare_2_files.exe" file and it will generate the "Output_File.csv" 
3> See "Output_File.csv" file for verification -> Which is present in "Out" folder


