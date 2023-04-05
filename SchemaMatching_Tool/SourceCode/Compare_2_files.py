import math
try:
		NewTable = open("Out\Dst_TableSchema_File.csv",'r')
		BaseTable = open("Out\Base_TableSchema_File.csv",'r')
		OutputFile=open("Out\Output_File.csv",'w')		
		NewTable_lines = NewTable.readlines()
		BaseTable_lines = BaseTable.readlines()
		BaseTable_list=''
		NewTable_list=''
		#print(BaseTable_list,NewTable_list) 
		if 1==1:
					OutputFile.write('src_Table.ColumnName,src_DefaultValue,src_IsNullable,src_DataType,src_Length,src_Precesion,dst_Table.ColumnName,dst_DefaultValue,dst_IsNullable,dst_DataType,dst_Length,dst_Precesion,Comment\n')
					for i in range(len(BaseTable_lines)):
						BaseTable_list=BaseTable_lines[i]
						BaseTable_list=BaseTable_list[1:]
						BaseTable_list=BaseTable_list[:-1]
						#BaseTable_list=BaseTable_list[:-1]					
						BaseTable_list=BaseTable_list.split()						
						Indicator=0
						for j in range (len(NewTable_lines)):
							NewTable_list=NewTable_lines[j]
							NewTable_list=NewTable_list[1:]
							#NewTable_list=NewTable_list[:-1]
							#NewTable_list=NewTable_list[:-1]
							NewTable_list=NewTable_list.split()
							# cnct here cmp_b=baseTable_list([0]+[1])	as it is for dst table	
							#print(BaseTable_list[0]+'.'+BaseTable_list[1])	
							bo_cnct=BaseTable_list[0]
							bo_cnct=bo_cnct[:-1]
							bo_cnct=bo_cnct[:-1]
							b1_cnct=BaseTable_list[1]
							b1_cnct=b1_cnct[1:]
							bo_cnct=bo_cnct+'.'+b1_cnct
							#print(bo_cnct)
							do_cnct=NewTable_list[0]
							do_cnct=do_cnct[:-1]
							do_cnct=do_cnct[:-1]
							d1_cnct=NewTable_list[1]
							d1_cnct=d1_cnct[1:]
							do_cnct=do_cnct+'.'+d1_cnct
							#print(do_cnct)							
							#print(b1_cnct)
							#print(bo_cnct)	
							# print(bo_cnct)
							#print(BaseTable_list[0],BaseTable_list[1])	
							#print(BaseTable_list[6])
							if (bo_cnct==do_cnct):									
									if BaseTable_lines[i]!=NewTable_lines[j]:			
										OutputFile.write('\''+bo_cnct+str(BaseTable_list[2])+BaseTable_list[3]+BaseTable_list[4]+BaseTable_list[5]+BaseTable_list[6]+","+'\''+do_cnct+NewTable_list[2]+NewTable_list[3]+NewTable_list[4]+NewTable_list[5]+NewTable_list[6]+",Column mismatch")
										OutputFile.write('\n')
									Indicator=1
						if(Indicator==0):
							OutputFile.write('\''+bo_cnct+str(BaseTable_list[2])+BaseTable_list[3]+BaseTable_list[4]+BaseTable_list[5]+BaseTable_list[6]+",,,,,,,"+"Missing column\n")
					for i in range(len(NewTable_lines)):
						NewTable_list=NewTable_lines[i]
						NewTable_list=NewTable_list[1:]
						NewTable_list=NewTable_list[:-1]
						#NewTable_list=NewTable_list[:-1]
						NewTable_list=NewTable_list.split()
						Indicator=0
						for j in range (len(BaseTable_lines)):
							BaseTable_list=BaseTable_lines[j]
							BaseTable_list=BaseTable_list[1:]
							#BaseTable_list=BaseTable_list[:-1]
							#BaseTable_list=BaseTable_list[:-1]
							BaseTable_list=BaseTable_list.split()
							do_cnct=NewTable_list[0]
							do_cnct=do_cnct[:-1]
							do_cnct=do_cnct[:-1]
							d1_cnct=NewTable_list[1]
							d1_cnct=d1_cnct[1:]
							do_cnct=do_cnct+'.'+d1_cnct		
							#destination concat
							bo_cnct=BaseTable_list[0]
							bo_cnct=bo_cnct[:-1]
							bo_cnct=bo_cnct[:-1]
							b1_cnct=BaseTable_list[1]
							b1_cnct=b1_cnct[1:]
							bo_cnct=bo_cnct+'.'+b1_cnct
												
							if (bo_cnct==do_cnct):
									Indicator=1
						if(Indicator==0):
							OutputFile.write(",,,,,,"+'\''+do_cnct+NewTable_list[2]+NewTable_list[3]+NewTable_list[4]+NewTable_list[5]+NewTable_list[6]+",Extra column\n")
		if(1==1):
			OutputFile.close()
			OutputFile=open("Out\Output_File.csv",'r+')
			Out_len=OutputFile.readlines()
			#print (len(Out_len))
			if(len(Out_len)==1):
				OutputFile.write("\n,!!Both schema is same!!")  
							
except:
	OutputFile.writelines("Something went wrong\nClose output file from everywhere and run tool again")	
finally:
	NewTable.close()
	BaseTable.close()
	OutputFile.close()
