def generate_allurl(user_in_nub):

    url = 'http://gz.lianjia.com/ershoufang/pg{}/'

    for url_next in range(1,int(user_in_nub)):

        yield url.format(url_next)

			 

def main():

    user_in_nub = input('输入生成页数：')

    for i in generate_allurl(user_in_nub):

        print(i)

			 

if __name__ == '__main__':

    main()

