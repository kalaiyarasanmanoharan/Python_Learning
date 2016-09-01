entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
entry1_list = entry1.split()
entry2_list = entry2.split()
entry3_list = entry3.split()
entry4_list = entry4.split()
ipprefix_1 = entry1_list[1]
ipprefix_2 = entry2_list[1]
ipprefix_3 = entry3_list[1]
ipprefix_4 = entry4_list[1]
as_path_1_i = entry1_list[3:]
as_path_2_i = entry2_list[3:]
as_path_3_i = entry3_list[3:]
as_path_4_i = entry4_list[3:]
as_path1 = as_path_1_i.remove('i')
as_path2 = as_path_2_i.remove('i')
as_path3 = as_path_3_i.remove('i')
as_path4 = as_path_4_i.remove('i')
print '\n Parsed and Formated Output below:'
print '\n\n'
print '%-20s %-50s' % ('ip_prefix','as_path')
print '\n%-20s %-50s' % (ipprefix_1,as_path_1_i)
print '%-20s %-50s' % (ipprefix_2,as_path_2_i)
print '%-20s %-50s' % (ipprefix_3,as_path_3_i)
print '%-20s %-50s' % (ipprefix_4,as_path_4_i)
