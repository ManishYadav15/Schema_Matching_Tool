import pyodbc 
Para_File=open("Parameters.txt",'r')
svrdbname=open("setup.txt",'r')
Para=Para_File.readlines()
svr=svrdbname.readlines()
serverName=str(svr[0])
serverName=serverName.split(':')
server=str(serverName[1])
server=server.strip()
databaseName=svr[1]
databaseName=databaseName.split(':')
databaseName=str(databaseName[1])
database=databaseName.strip()
svrdbname.close()
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
output_FP=open("Out\Base_TableSchema_File.csv",'w')
for tbl in (range(len(Para))):
    TableName=Para[tbl]
    TableName=TableName.strip()
    cursor = cnxn.cursor()
    cursor.execute("SELECT  TABLE_NAME,COLUMN_NAME,COLUMN_DEFAULT,IS_NULLABLE,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,NUMERIC_PRECISION FROM INFORMATION_SCHEMA.COLUMNS	WHERE TABLE_NAME =\'"+TableName+"\'")
    #output_FP.write('TableName,ColumnName,DefaultValue,Is_Nullable,DataType,Length,Precesion\n')
    for i in cursor:
        i=str(i)
        i=i[1:]
        i=i[:-1]
        output_FP.write(str(i)+'\n')
        


output_FP.close()
Para_File.close()
cnxn.close()


