#Khởi tạo biến chứa đường dẫn tới file dữ liệu
path = 'amibroker_all_data.txt'

#Đọc file chứa dữ liệu
file = open(path, 'r')
data = file.readlines()
file.close()

title = data[0]
data = data[1:]
res = []
#Với từng biến (line) thuộc dữ liệu
for line in data:
    #Tách line (str) theo dấu ',' để lọc dữ liệu từ năm 2011 đến hết năm 2020
    #Tạo list mới là s chứa line thỏa mãn điều kiện
    #Định dạng ngày tháng, sau đó thêm dữ liệu (s) đã được định dạng vào list res
    if 2021> int(line.split(',')[1][:4]) >= 2011:
        s = line.split(',')
        date = s[1]
        #Chia dữ liệu thời gian thành năm, tháng, ngày, ngăn cách bởi '/'
        s[1] = f'{date[:4]}/{date[4:6]}/{date[6:8]}'
        res.append(','.join(s))

#Khởi tạo dictionary với tên là dic
dic = {}
#Với biến (line) trong list res
for line in res:
    #Tách theo dấu ',' và lấy giá trị ở cột đầu tiên
    key = line.split(',')[0]
    key = key[1:] if line.startswith('^') else key
    #Với giá trị key (tên mã chứng khoán) chưa có trong dic
    #Thêm key mới, thêm dòng giá trị (line) tương ứng với key đó
    if key not in dic:
        dic[key] = []
    dic[key].append(line)

#Tách file dữ liệu tổng thành từng file con theo tên của mã chứng khoán    
for key in dic:
    file = open(f'txts\\{key}.txt', 'w+')
    file.write(title)
    file.writelines(dic[key])
    file.close()
    print(f'wrote {key}')
print('done')


