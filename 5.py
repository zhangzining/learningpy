from urllib import parse

response = parse.urlparse('https://www.baidu.com/s?wd=python%E8%A3%85%E9%A5%B0%E5%99%A8&rsv_spt=1&rsv_iqid=0x84010d820004e223&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=14&rsv_sug1=21&rsv_sug7=100&rsv_t=f285wZexjG9u%2FfjpampzkuZr%2BHxC%2BxXk%2FL5L4d%2B3Yy2enSGCuRPaFxCltu1JST6wSpAk')
print(type(response),response)
print(parse.urlunparse(response))


part = {
    'name':'assdf',
    'age':18
}
base_url='http://www.baidu.com?'
url= base_url+parse.urlencode(part)
print(url)