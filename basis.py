"""hashlib模块"""
import hashlib
def pwd_md5(pwd):
    md5_obj = hashlib.md5()
    md5_obj.update(pwd.encode('utf-8'))
var = '宝塔镇河妖'
md5_obj.update(val.encode('utf-8'))
pwd = md5_obj.hexdigest()
return pwd

"""sys模块（与python解释器交互）"""
# 获取当前的python解释器的环境变量
sys.path
# 将当前项目添加到环境变量中
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
# 获取cmd终端命令，以空格分割，返回列表
print(sys.argv)

"""os模块（与操作系统交互）"""
# 获取当前文件（或文件夹）所在的路径
CUR_PATH = os.path.dirname(__file__)
# 路径拼接：拼接文件的’绝对路径‘
TEST_PATH = os.path.join(CUR_PATH,'test.txt')
# 判断文件或文件夹是否存在
res = os.path.exists(TEST_PATH)
# 判断文件夹是否存在
res = os.path.isdir(TEST_PATH})
# 创建文件夹
os.mkdir(DIR_PATH)
# 删除文件夹
os.rmdir(DIR_PATH)
# 删除文件
os.remove(file_name)
# 获取指定文件夹下面的所有文件夹名和文件名
os.listdir(DIR_PATH)


"""random模块"""
import random
# 随机从1-9中返回一个整数
res = random.int(1,9)
# 返回0-1之间的浮点数
res = random.random()
# shuffle（洗牌）有索引的可变可迭代对象
my_list = [1, 2, 3, 3, 7]
random.shuffle(my_list)
print(my_list)
# choice（随机选择）有索引的可迭代对象
my_str =  'yyh NO.1'
random.choice(my_str)
# 例题：生成随机验证码
def random_code(n):
    char_range = [chr(i) for i in range(65, 91)] + \
                 [chr(i) for i in range(97, 123)] + \
                 [str(i) for i in range(10)]
    result = ''
    for i in range(n):
        result += random.choice(char_range)
    return result

print(random_code(6))


"""datetime模块"""
# 1、获取当前年月日
print(datetime.date.today())
# ==>2019-11-16
# 2、获取当前年月日时分秒
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow()) # 格林尼治时间
# ==>2019-11-16 14:54:34.496536
# ==>2019-11-16 14:54:34.496536
# ==>2019-11-16 06:54:34.496536

# 日期/时间的计算
#	日期时间 = 日期时间 + - 时间对象
current_time = datetime.datetime.now()
time_obj = date.timedelta(days=7)
later_time = current_time + time_obj
#	时间对象 = 日期时间 + - 日期时间
current_time = datetime.datetime.now()
later_time = datetime.datetime.utcnow()
time_obj = later_time - current_time


"""time模块
python中的三种时间表示形式
1、时间戳
- 自1970-01-01 00：00：00到当前时间，单位为秒
2、格式化时间
- 返回的是时间的字符串
3、格式化时间对象(struct_time)
- 9个值分别代表：年、月、日、时、分、秒、一周中第几天、一年中的第几天、夏令时"""

# 1、获取时间戳
now_time = time.time()
#==>1573885266.3314579
# 2、获取格式化时间
now_time = time.strftime('%Y-%m-%d %H:%M:%S')
==>2019-11-16 14:21:06
# 3、获取时间对象
time_obj = time.localtime()
print(time_obj.tm_year)
print(time_obj.tm_mon)
print(time_obj.tm_mday)
print(time_obj.tm_hour)
print(time_obj.tm_min)
print(time_obj.tm_sec)
# 4、时间对象-->字符串格式化时间
time_str=time.strftime('%Y-%m-%d %H:%M:%S',time_obj)
# 5、字符串格式化的时间-->时间对象
time_boj = time.strptime('2019-01-01','%Y-%m-%d')