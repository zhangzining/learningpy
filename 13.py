import requests
import re

text = 'RegExr v3 was created by gskinner.com'
result = re.match('^Reg.*com$',text)
print(result.group())
html = '''<html>
 <head></head>
 <body>
  <div class="hd ">
   <span data-res-id="210281" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">1</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=210281"><b title="心动">心
        <div class="soil">
         按基维文
        </div>动</b></a><span data-res-id="210281" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:50</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="210281" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="210281" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="210281" data-res-type="18" data-res-action="share" data-res-name="心动" data-res-author="陈洁仪" data-res-pic="http://p1.music.126.net/4TEo0Z2Qn0evADoBg-bDQw==/109951163123371649.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="210281" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陈洁仪">
   <span title="陈洁仪"><a class="" href="/artist?id=7439" hidefocus="true">陈
     <div class="soil">
      向月报规必
     </div>洁仪</a></span>
  </div>
  <div class="text">
   <a href="/album?id=21364" title="重译">重
    <div class="soil">
     鋉
    </div>译</a>
  </div>
  <div class="hd ">
   <span data-res-id="133998" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">2</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=133998"><b title="老街">老
        <div class="soil">
         糼鲣祵氟
        </div>街</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:18</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="133998" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="133998" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="133998" data-res-type="18" data-res-action="share" data-res-name="老街" data-res-author="李荣浩" data-res-pic="http://p1.music.126.net/fZFrplIVrHMx4lvgdqiIHQ==/42880953496261.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="133998" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="李荣浩">
   <span title="李荣浩"><a class="" href="/artist?id=4292" hidefocus="true">李
     <div class="soil">
      崭聖贫抹
     </div>荣浩</a></span>
  </div>
  <div class="text">
   <a href="/album?id=13140" title="小黄">小
    <div class="soil">
     原你
    </div>黄</a>
  </div>
  <div class="hd ">
   <span data-res-id="188177" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">3</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=188177"><b title="天天想你">天
        <div class="soil">
         黖谌钘
        </div>天想你</b></a><span data-res-id="188177" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:16</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="188177" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="188177" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="188177" data-res-type="18" data-res-action="share" data-res-name="天天想你" data-res-author="张雨生" data-res-pic="http://p1.music.126.net/8X5fw5G6M4FjtR6sQixdnA==/111050674406314.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="188177" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张雨生">
   <span title="张雨生"><a class="" href="/artist?id=6459" hidefocus="true">张
     <div class="soil">
      生高受
     </div>雨生</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19058" title="天天想你">天
    <div class="soil">
     带那小
    </div>天想你</a>
  </div>
  <div class="hd ">
   <span data-res-id="25643291" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">4</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=25643291"><b title="需要人陪">需要
        <div class="soil">
         机太
        </div>人陪</b></a><span data-res-id="25643291" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:11</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="25643291" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="25643291" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="25643291" data-res-type="18" data-res-action="share" data-res-name="需要人陪" data-res-author="王力宏" data-res-pic="http://p1.music.126.net/Eoql80OnsZAvZ0UASHo6zQ==/109951163421419702.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="25643291" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="王力宏">
   <span title="王力宏"><a class="" href="/artist?id=5346" hidefocus="true">王
     <div class="soil">
      规任
     </div>力宏</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2263059" title="十八般武艺">十八
    <div class="soil">
     采内查器
    </div>般武艺</a>
  </div>
  <div class="hd ">
   <span data-res-id="185700" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">5</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=185700"><b title="思念是一种病">思
        <div class="soil">
         锶悒
        </div>念是一种病</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:19</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="185700" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="185700" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="185700" data-res-type="18" data-res-action="share" data-res-name="思念是一种病" data-res-author="张震岳/蔡健雅" data-res-pic="http://p1.music.126.net/N61oLy0iLfEkZTHD2j87iA==/18693896697392706.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="185700" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张震岳/蔡健雅">
   <span title="张震岳/蔡健雅"><a class="" href="/artist?id=6453" hidefocus="true">张
     <div class="soil">
      西基史光照
     </div>震岳</a>/<a class="" href="/artist?id=7214" hidefocus="true">蔡
     <div class="soil">
      速三院需
     </div>健雅</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18878" title="OK">O
    <div class="soil">
     AxQ
    </div>K</a>
  </div>
  <div class="hd ">
   <span data-res-id="287035" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">6</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=287035"><b title="遇见">遇
        <div class="soil">
         话产许交民
        </div>见</b></a><span data-res-id="287035" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:30</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="287035" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="287035" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="287035" data-res-type="18" data-res-action="share" data-res-name="遇见" data-res-author="孙燕姿" data-res-pic="http://p1.music.126.net/ZpcOx5dbNTRK94vSIM20PQ==/768558627827568.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="287035" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="孙燕姿">
   <span title="孙燕姿"><a class="" href="/artist?id=9272" hidefocus="true">孙
     <div class="soil">
      竣韟
     </div>燕姿</a></span>
  </div>
  <div class="text">
   <a href="/album?id=28519" title="经典全纪录(主打精华版)">经典全纪录(
    <div class="soil">
     骡鴠
    </div>主打精华版)</a>
  </div>
  <div class="hd ">
   <span data-res-id="188674" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">7</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=188674"><b title="情书">情
        <div class="soil">
         化是保
        </div>书</b></a><span data-res-id="188674" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:06</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="188674" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="188674" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="188674" data-res-type="18" data-res-action="share" data-res-name="情书" data-res-author="张学友" data-res-pic="http://p1.music.126.net/4EKzVVjcVOwq_QamSKLR5w==/65970697682613.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="188674" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张学友">
   <span title="张学友"><a class="" href="/artist?id=6460" hidefocus="true">张
     <div class="soil">
      蹙拆淳
     </div>学友</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19093" title="友情歌&nbsp;1995-2000世纪情歌金选">友情歌&nbsp;
    <div class="soil">
     Rc2E
    </div>1995-2000世纪情歌金选</a>
  </div>
  <div class="hd ">
   <span data-res-id="25714352" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">8</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=25714352"><b title="空白格 - (电影《一生一世》片尾曲)">空
        <div class="soil">
         惥碈瘄坿
        </div>白格</b></a><span title="电影《一生一世》片尾曲" class="s-fc8"> - (电影《
       <div class="soil">
        犜氄雍綖
       </div>一生一世》片尾曲)</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:45</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="25714352" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="25714352" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="25714352" data-res-type="18" data-res-action="share" data-res-name="空白格" data-res-author="杨宗纬" data-res-pic="http://p1.music.126.net/s2rrkEZ6S7UVAJI-D1M4lA==/2258396883454110.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="25714352" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="杨宗纬">
   <span title="杨宗纬"><a class="" href="/artist?id=6066" hidefocus="true">杨
     <div class="soil">
      少节毛局十
     </div>宗纬</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2290034" title="我是歌手第一季&nbsp;第5期">我是歌手第一季
    <div class="soil">
     uT
    </div>&nbsp;第5期</a>
  </div>
  <div class="hd ">
   <span data-res-id="110397" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">9</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=110397"><b title="冰雨(Live)&nbsp;-&nbsp;live">冰雨(Live)
        <div class="soil">
         Ms
        </div>&nbsp;-&nbsp;live</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:51</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="110397" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="110397" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="110397" data-res-type="18" data-res-action="share" data-res-name="冰雨(Live) - live" data-res-author="刘德华" data-res-pic="http://p1.music.126.net/NcVf7w7gtyvmfw0OGI8W6A==/888405395243414.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="110397" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="刘德华">
   <span title="刘德华"><a class="" href="/artist?id=3691" hidefocus="true">刘
     <div class="soil">
      昫
     </div>德华</a></span>
  </div>
  <div class="text">
   <a href="/album?id=10918" title="你是我的骄傲演唱会">你是我的
    <div class="soil">
     绫祕
    </div>骄傲演唱会</a>
  </div>
  <div class="hd ">
   <span data-res-id="473164022" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">10</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=473164022"><b title="梦呓">梦
        <div class="soil">
         櫼氓棎
        </div>呓</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:56</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="473164022" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="473164022" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="473164022" data-res-type="18" data-res-action="share" data-res-name="梦呓" data-res-author="陈百强" data-res-pic="http://p1.music.126.net/VpTkmDMLxYr6inINjGfFuA==/18233201323949414.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="473164022" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陈百强">
   <span title="陈百强"><a class="" href="/artist?id=2115" hidefocus="true">陈
     <div class="soil">
      灟燆
     </div>百强</a></span>
  </div>
  <div class="text">
   <a href="/album?id=35404908" title="Elegance&nbsp;&amp;&nbsp;Charm&nbsp;文质翩翩">Elegance&nbsp;&amp;&nbsp;Charm&nbsp;
    <div class="soil">
     已步值活者
    </div>文质翩翩</a>
  </div>
  <div class="hd ">
   <span data-res-id="150520" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">11</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=150520"><b title="Melody">M
        <div class="soil">
         n0v9
        </div>elody</b></a><span data-res-id="150520" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:29</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="150520" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="150520" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="150520" data-res-type="18" data-res-action="share" data-res-name="Melody" data-res-author="陶喆" data-res-pic="http://p1.music.126.net/HMhU9tbNP_Qyel369htWzw==/18516875325082773.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="150520" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陶喆">
   <span title="陶喆"><a class="" href="/artist?id=5196" hidefocus="true">陶
     <div class="soil">
      动放受
     </div>喆</a></span>
  </div>
  <div class="text">
   <a href="/album?id=15189" title="Ultrasound&nbsp;乐之路&nbsp;1997-2003">Ul
    <div class="soil">
     C
    </div>trasound&nbsp;乐之路&nbsp;1997-2003</a>
  </div>
  <div class="hd ">
   <span data-res-id="1294910319" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">12</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=1294910319"><b title="脆弱一分钟 - (电视剧《爱情进化论》片头曲)">脆弱一
        <div class="soil">
         藝返
        </div>分钟</b></a><span title="电视剧《爱情进化论》片头曲" class="s-fc8"> - (电视
       <div class="soil">
        済
       </div>剧《爱情进化论》片头曲)</span><span data-res-id="1294910319" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:12</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1294910319" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="1294910319" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="1294910319" data-res-type="18" data-res-action="share" data-res-name="脆弱一分钟" data-res-author="林宥嘉" data-res-pic="http://p1.music.126.net/tTpgtOYQhkXy710yYb1-qg==/109951163436434768.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="1294910319" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="林宥嘉">
   <span title="林宥嘉"><a class="" href="/artist?id=3685" hidefocus="true">林
     <div class="soil">
      萗浃疢
     </div>宥嘉</a></span>
  </div>
  <div class="text">
   <a href="/album?id=72070692" title="爱情进化论&nbsp;电视剧原声带">爱情进化论&nbsp;电视剧原
    <div class="soil">
     科三
    </div>声带</a>
  </div>
  <div class="hd ">
   <span data-res-id="30621680" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">13</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=30621680"><b title="宁夏">宁
        <div class="soil">
         俀趗
        </div>夏</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:22</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="30621680" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="30621680" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="30621680" data-res-type="18" data-res-action="share" data-res-name="宁夏" data-res-author="梁静茹" data-res-pic="http://p1.music.126.net/05AFocB_OqIaoJkPxreF9A==/3242459792261081.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="30621680" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="梁静茹">
   <span title="梁静茹"><a class="" href="/artist?id=8325" hidefocus="true">梁
     <div class="soil">
      靛儀憿嫜
     </div>静茹</a></span>
  </div>
  <div class="text">
   <a href="/album?id=3080406" title="梦想星搭档&nbsp;第二季">梦想星搭
    <div class="soil">
     瓺崤戄
    </div>档&nbsp;第二季</a>
  </div>
  <div class="hd ">
   <span data-res-id="189323" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">14</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=189323"><b title="断点">断
        <div class="soil">
         搨敫疺戤
        </div>点</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:29</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="189323" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="189323" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="189323" data-res-type="18" data-res-action="share" data-res-name="断点" data-res-author="张敬轩" data-res-pic="http://p1.music.126.net/-hO_dxCQ4yl5OikwAt-FvQ==/45079976755863.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="189323" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张敬轩">
   <span title="张敬轩"><a class="" href="/artist?id=6462" hidefocus="true">张
     <div class="soil">
      闘苸
     </div>敬轩</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19148" title="My&nbsp;Way">My&nbsp;
    <div class="soil">
     MTxa
    </div>Way</a>
  </div>
  <div class="hd ">
   <span data-res-id="185726" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">15</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=185726"><b title="再见">再
        <div class="soil">
         鐚巷
        </div>见</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:03</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="185726" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="185726" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="185726" data-res-type="18" data-res-action="share" data-res-name="再见" data-res-author="张震岳" data-res-pic="http://p1.music.126.net/ovYzwC_wSPz9EZ18xBDSZA==/100055558139763.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="185726" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张震岳">
   <span title="张震岳"><a class="" href="/artist?id=6453" hidefocus="true">张
     <div class="soil">
      青于王青里
     </div>震岳</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18881" title="再见">再
    <div class="soil">
     图一活
    </div>见</a>
  </div>
  <div class="hd ">
   <span data-res-id="287749" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">16</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=287749"><b title="天黑黑">天
        <div class="soil">
         湣鈜綔开
        </div>黑黑</b></a><span data-res-id="287749" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:57</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="287749" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="287749" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="287749" data-res-type="18" data-res-action="share" data-res-name="天黑黑" data-res-author="孙燕姿" data-res-pic="http://p1.music.126.net/p_5BNWuwtBJ_Fl5gClx5Pg==/101155069756398.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="287749" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="孙燕姿">
   <span title="孙燕姿"><a class="" href="/artist?id=9272" hidefocus="true">孙
     <div class="soil">
      赳働
     </div>燕姿</a></span>
  </div>
  <div class="text">
   <a href="/album?id=28562" title="yanzi&nbsp;同名专辑">ya
    <div class="soil">
     7
    </div>nzi&nbsp;同名专辑</a>
  </div>
  <div class="hd ">
   <span data-res-id="490602750" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">17</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=490602750"><b title="越过山丘 - (致李宗盛)">越
        <div class="soil">
         该酸应包团
        </div>过山丘</b></a><span title="致李宗盛" class="s-fc8"> - (致
       <div class="soil">
        明状利张利
       </div>李宗盛)</span><span data-res-id="490602750" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:53</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="490602750" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="490602750" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="490602750" data-res-type="18" data-res-action="share" data-res-name="越过山丘" data-res-author="杨宗纬" data-res-pic="http://p1.music.126.net/iKJz-iaybHIRk2QKe80pog==/19195273997955269.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="490602750" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="杨宗纬">
   <span title="杨宗纬"><a class="" href="/artist?id=6066" hidefocus="true">杨
     <div class="soil">
      济加且上
     </div>宗纬</a></span>
  </div>
  <div class="text">
   <a href="/album?id=35757233" title="越过山丘">越过
    <div class="soil">
     极查方
    </div>山丘</a>
  </div>
  <div class="hd ">
   <span data-res-id="188384" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">18</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=188384"><b title="樱花树下">樱花
        <div class="soil">
         褹
        </div>树下</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:12</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="188384" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="188384" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="188384" data-res-type="18" data-res-action="share" data-res-name="樱花树下" data-res-author="张敬轩" data-res-pic="http://p1.music.126.net/WZY0jAKYiRd0tL7wyJn7zg==/38482906984309.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="188384" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张敬轩">
   <span title="张敬轩"><a class="" href="/artist?id=6462" hidefocus="true">张
     <div class="soil">
      大是
     </div>敬轩</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19073" title="P.S.&nbsp;I&nbsp;Love&nbsp;You&nbsp;新歌+精选">P.S.
    <div class="soil">
     wk
    </div>&nbsp;I&nbsp;Love&nbsp;You&nbsp;新歌+精选</a>
  </div>
  <div class="hd ">
   <span data-res-id="5267256" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">19</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=5267256"><b title="爱很简单">爱很
        <div class="soil">
         名日积什
        </div>简单</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:31</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="5267256" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="5267256" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="5267256" data-res-type="18" data-res-action="share" data-res-name="爱很简单" data-res-author="陶喆" data-res-pic="http://p1.music.126.net/q-y_2Ey9hNn4PpxhvlwczA==/98956046517104.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="5267256" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陶喆">
   <span title="陶喆"><a class="" href="/artist?id=5196" hidefocus="true">陶
     <div class="soil">
      局被研线
     </div>喆</a></span>
  </div>
  <div class="text">
   <a href="/album?id=512781" title="闭上眼睛去旅行&nbsp;2">闭上眼睛去旅行
    <div class="soil">
     T
    </div>&nbsp;2</a>
  </div>
  <div class="hd ">
   <span data-res-id="316498" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">20</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=316498"><b title="勇">
        <div class="soil">
         条听层
        </div>勇</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:41</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="316498" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="316498" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="316498" data-res-type="18" data-res-action="share" data-res-name="勇" data-res-author="杨千嬅" data-res-pic="http://p1.music.126.net/jTjlHs4c_E7dV4O-S4hcMQ==/39582418616753.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="316498" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="杨千嬅">
   <span title="杨千嬅"><a class="" href="/artist?id=10204" hidefocus="true">杨
     <div class="soil">
      受表
     </div>千嬅</a></span>
  </div>
  <div class="text">
   <a href="/album?id=31350" title="千嬅盛放">千
    <div class="soil">
     慝
    </div>嬅盛放</a>
  </div>
  <div class="hd ">
   <span data-res-id="60263" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">21</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=60263"><b title="他一定很爱你">他一定
        <div class="soil">
         贾卲蛊碦
        </div>很爱你</b></a><span data-res-id="60263" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:34</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="60263" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="60263" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="60263" data-res-type="18" data-res-action="share" data-res-name="他一定很爱你" data-res-author="阿杜" data-res-pic="http://p1.music.126.net/3lrUXI96dmlEi2UgeIhOHg==/109951163076301483.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="60263" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="阿杜">
   <span title="阿杜"><a class="" href="/artist?id=1876" hidefocus="true">阿
     <div class="soil">
      潄裚葵
     </div>杜</a></span>
  </div>
  <div class="text">
   <a href="/album?id=5863" title="天黑">天
    <div class="soil">
     受准维
    </div>黑</a>
  </div>
  <div class="hd ">
   <span data-res-id="187051" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">22</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=187051"><b title="仲夏夜之梦">仲
        <div class="soil">
         民全日没里
        </div>夏夜之梦</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">02:40</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="187051" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="187051" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="187051" data-res-type="18" data-res-action="share" data-res-name="仲夏夜之梦" data-res-author="张雨生" data-res-pic="http://p1.music.126.net/4vuaCmNxbFl1GVJfiSwyrw==/86861418607098.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="187051" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张雨生">
   <span title="张雨生"><a class="" href="/artist?id=6459" hidefocus="true">张
     <div class="soil">
      釴鱷
     </div>雨生</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18966" title="如燕盘旋而来的思念">如燕盘旋
    <div class="soil">
     该节器但
    </div>而来的思念</a>
  </div>
  <div class="hd ">
   <span data-res-id="26113988" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">23</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=26113988"><b title="泡沫">泡
        <div class="soil">
         好铁色提
        </div>沫</b></a><span data-res-id="26113988" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:19</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="26113988" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="26113988" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="26113988" data-res-type="18" data-res-action="share" data-res-name="泡沫" data-res-author="G.E.M.邓紫棋" data-res-pic="http://p1.music.126.net/W9wg627_ia4NMwlKSRLcsw==/109951163432573570.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="26113988" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="G.E.M.邓紫棋">
   <span title="G.E.M.邓紫棋"><a class="" href="/artist?id=7763" hidefocus="true">G.E.M
     <div class="soil">
      Maw
     </div>.邓紫棋</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2389401" title="The&nbsp;Best&nbsp;of&nbsp;G.E.M.&nbsp;2008-2012">The&nbsp;Best&nbsp;of&nbsp;G.E.M
    <div class="soil">
     k
    </div>.&nbsp;2008-2012</a>
  </div>
  <div class="hd ">
   <span data-res-id="108478" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">24</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=108478"><b title="醉赤壁 - (网游《赤壁Online》主题曲)">醉
        <div class="soil">
         百十米他
        </div>赤壁</b></a><span title="网游《赤壁Online》主题曲" class="s-fc8"> - (网游《赤壁On
       <div class="soil">
        ZJBv
       </div>line》主题曲)</span><span data-res-id="108478" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:41</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="108478" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="108478" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="108478" data-res-type="18" data-res-action="share" data-res-name="醉赤壁" data-res-author="林俊杰" data-res-pic="http://p1.music.126.net/s6zFxvXe5kOxub4_x4rZhQ==/109951163052847567.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="108478" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="林俊杰">
   <span title="林俊杰"><a class="" href="/artist?id=3684" hidefocus="true">林
     <div class="soil">
      囕竖掇薏
     </div>俊杰</a></span>
  </div>
  <div class="text">
   <a href="/album?id=10770" title="JJ陆">J
    <div class="soil">
     6
    </div>J陆</a>
  </div>
  <div class="hd ">
   <span data-res-id="139392" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">25</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=139392"><b title="那些花儿(吉他版)">那些花
        <div class="soil">
         鉋町
        </div>儿(吉他版)</b></a><span data-res-id="139392" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:02</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="139392" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="139392" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="139392" data-res-type="18" data-res-action="share" data-res-name="那些花儿(吉他版)" data-res-author="朴树" data-res-pic="http://p1.music.126.net/QYI8P7bfmwUKxH3Kll95LQ==/18878614649179588.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="139392" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="朴树">
   <span title="朴树"><a class="" href="/artist?id=4721" hidefocus="true">朴
     <div class="soil">
      山府
     </div>树</a></span>
  </div>
  <div class="text">
   <a href="/album?id=13892" title="我去2000年">我去20
    <div class="soil">
     w
    </div>00年</a>
  </div>
  <div class="hd ">
   <span data-res-id="191232" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">26</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=191232"><b title="遥远的她">遥
        <div class="soil">
         之着其交统
        </div>远的她</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:19</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="191232" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="191232" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="191232" data-res-type="18" data-res-action="share" data-res-name="遥远的她" data-res-author="张学友" data-res-pic="http://p1.music.126.net/rxyLRMZdqzHdxyP5cl8qQA==/43980465112095.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="191232" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张学友">
   <span title="张学友"><a class="" href="/artist?id=6460" hidefocus="true">张
     <div class="soil">
      瞎
     </div>学友</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19316" title="遥远的她.Amour">遥远
    <div class="soil">
     虸
    </div>的她.Amour</a>
  </div>
  <div class="hd ">
   <span data-res-id="5279696" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">27</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=5279696"><b title="我的未来不是梦">我的
        <div class="soil">
         以图示革
        </div>未来不是梦</b></a><span data-res-id="5279696" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:13</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="5279696" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="5279696" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="5279696" data-res-type="18" data-res-action="share" data-res-name="我的未来不是梦" data-res-author="张雨生" data-res-pic="http://p1.music.126.net/qVUJ9aDeRop5pj3QDixIsQ==/109951163353510177.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="5279696" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张雨生">
   <span title="张雨生"><a class="" href="/artist?id=6459" hidefocus="true">张
     <div class="soil">
      针凣
     </div>雨生</a></span>
  </div>
  <div class="text">
   <a href="/album?id=513560" title="惊世记录Ⅱ">惊世记
    <div class="soil">
     嚼蛶
    </div>录Ⅱ</a>
  </div>
  <div class="hd ">
   <span data-res-id="29723021" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">28</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=29723021"><b title="太想爱&nbsp;(国)">太想爱
        <div class="soil">
         Ht
        </div>&nbsp;(国)</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:24</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="29723021" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="29723021" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="29723021" data-res-type="18" data-res-action="share" data-res-name="太想爱 (国)" data-res-author="刘德华" data-res-pic="http://p1.music.126.net/-6osWky_WObfAydYYiTvpA==/3236962232773608.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="29723021" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="刘德华">
   <span title="刘德华"><a class="" href="/artist?id=3691" hidefocus="true">刘
     <div class="soil">
      陣
     </div>德华</a></span>
  </div>
  <div class="text">
   <a href="/album?id=3066282" title="Wonderful&nbsp;World&nbsp;香港演唱会&nbsp;2007">Wonderful&nbsp;Wo
    <div class="soil">
     9dB
    </div>rld&nbsp;香港演唱会&nbsp;2007</a>
  </div>
  <div class="hd ">
   <span data-res-id="505451285" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">29</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=505451285"><b title="青春住了谁">青春
        <div class="soil">
         贂泶
        </div>住了谁</b></a><span data-res-id="505451285" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:30</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="505451285" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="505451285" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="505451285" data-res-type="18" data-res-action="share" data-res-name="青春住了谁" data-res-author="杨丞琳" data-res-pic="http://p1.music.126.net/f8I94rzjMCzZJ0q1fR0ftw==/109951163023754735.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="505451285" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="杨丞琳">
   <span title="杨丞琳"><a class="" href="/artist?id=10199" hidefocus="true">杨
     <div class="soil">
      經纮
     </div>丞琳</a></span>
  </div>
  <div class="text">
   <a href="/album?id=36165421" title="青春住了谁">青春住
    <div class="soil">
     入社江你
    </div>了谁</a>
  </div>
  <div class="hd ">
   <span data-res-id="25640392" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">30</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=25640392"><b title="淋雨一直走">淋雨一
        <div class="soil">
         低约
        </div>直走</b></a><span data-res-id="25640392" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:24</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="25640392" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="25640392" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="25640392" data-res-type="18" data-res-action="share" data-res-name="淋雨一直走" data-res-author="张韶涵" data-res-pic="http://p1.music.126.net/cf_rfWB9QO2Q_bd5S4085w==/559651418577639.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="25640392" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张韶涵">
   <span title="张韶涵"><a class="" href="/artist?id=10562" hidefocus="true">张
     <div class="soil">
      设学
     </div>韶涵</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2262033" title="有形的翅膀">有形
    <div class="soil">
     还义学列
    </div>的翅膀</a>
  </div>
  <div class="hd ">
   <span data-res-id="65956" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">31</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=65956"><b title="烟雨凄迷">烟雨
        <div class="soil">
         鱾鍧奴迷
        </div>凄迷</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:26</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="65956" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="65956" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="65956" data-res-type="18" data-res-action="share" data-res-name="烟雨凄迷" data-res-author="陈百强" data-res-pic="http://p1.music.126.net/VF7PpL62WYKSBgRPu5YGcg==/18740076185819731.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="65956" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陈百强">
   <span title="陈百强"><a class="" href="/artist?id=2115" hidefocus="true">陈
     <div class="soil">
      样单道
     </div>百强</a></span>
  </div>
  <div class="text">
   <a href="/album?id=6463" title="神仙也移民">神仙
    <div class="soil">
     风安
    </div>也移民</a>
  </div>
  <div class="hd ">
   <span data-res-id="518904283" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">32</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=518904283"><b title="永恒的印记">永恒的
        <div class="soil">
         麲
        </div>印记</b></a><span data-res-id="518904283" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:07</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="518904283" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="518904283" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="518904283" data-res-type="18" data-res-action="share" data-res-name="永恒的印记" data-res-author="张信哲/张艾嘉" data-res-pic="http://p1.music.126.net/0XQcTtpc3TKOpaO3fbTCgw==/109951163064458275.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="518904283" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张信哲/张艾嘉">
   <span title="张信哲/张艾嘉"><a class="" href="/artist?id=6454" hidefocus="true">张
     <div class="soil">
      美公
     </div>信哲</a>/<a class="" href="/artist?id=10564" hidefocus="true">张
     <div class="soil">
      列根
     </div>艾嘉</a></span>
  </div>
  <div class="text">
   <a href="/album?id=36811083" title="永恒的印记">永恒的
    <div class="soil">
     醼莠噼宺
    </div>印记</a>
  </div>
  <div class="hd ">
   <span data-res-id="187374" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">33</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=187374"><b title="我">
        <div class="soil">
         片机矿次
        </div>我</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:44</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="187374" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="187374" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="187374" data-res-type="18" data-res-action="share" data-res-name="我" data-res-author="张国荣" data-res-pic="http://p1.music.126.net/Sbhanu6TSPEOq655lj34Gg==/98956046505532.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="187374" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张国荣">
   <span title="张国荣"><a class="" href="/artist?id=6457" hidefocus="true">张
     <div class="soil">
      单务交科特
     </div>国荣</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19003" title="大热">大
    <div class="soil">
     与利克政导
    </div>热</a>
  </div>
  <div class="hd ">
   <span data-res-id="186560" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">34</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=186560"><b title="过火">过
        <div class="soil">
         人代别带
        </div>火</b></a><span data-res-id="186560" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:02</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="186560" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="186560" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="186560" data-res-type="18" data-res-action="share" data-res-name="过火" data-res-author="张信哲" data-res-pic="http://p1.music.126.net/BbtqIF_OYpDk21lqTKROCQ==/638816255750141.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="186560" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张信哲">
   <span title="张信哲"><a class="" href="/artist?id=6454" hidefocus="true">张
     <div class="soil">
      到各对真最
     </div>信哲</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18947" title="选哲">选
    <div class="soil">
     儿全林准
    </div>哲</a>
  </div>
  <div class="hd ">
   <span data-res-id="22740077" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">35</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=22740077"><b title="左边">左
        <div class="soil">
         今集
        </div>边</b></a><span data-res-id="22740077" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:35</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="22740077" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="22740077" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="22740077" data-res-type="18" data-res-action="share" data-res-name="左边" data-res-author="杨丞琳" data-res-pic="http://p1.music.126.net/Bs1QSZie0p1yM6hH_eqw-w==/758663023207500.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="22740077" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="杨丞琳">
   <span title="杨丞琳"><a class="" href="/artist?id=10199" hidefocus="true">杨
     <div class="soil">
      月价治空
     </div>丞琳</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2088097" title="Whimsical&nbsp;World&nbsp;Collection">Whim
    <div class="soil">
     yZx
    </div>sical&nbsp;World&nbsp;Collection</a>
  </div>
  <div class="hd ">
   <span data-res-id="205449" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">36</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=205449"><b title="失恋无罪">失恋
        <div class="soil">
         濴盻醕瓩
        </div>无罪</b></a><span data-res-id="205449" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:06</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="205449" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="205449" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="205449" data-res-type="18" data-res-action="share" data-res-name="失恋无罪" data-res-author="A-Lin" data-res-pic="http://p1.music.126.net/mOyWKb751UIr8YeemHQqYg==/80264348833691.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="205449" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="A-Lin">
   <span title="A-Lin"><a class="" href="/artist?id=7063" hidefocus="true">A
     <div class="soil">
      H
     </div>-Lin</a></span>
  </div>
  <div class="text">
   <a href="/album?id=20846" title="失恋无罪">失
    <div class="soil">
     伺絉呡
    </div>恋无罪</a>
  </div>
  <div class="hd ">
   <span data-res-id="186699" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">37</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=186699"><b title="共同渡过">共同
        <div class="soil">
         领维资
        </div>渡过</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:23</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="186699" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="186699" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="186699" data-res-type="18" data-res-action="share" data-res-name="共同渡过" data-res-author="张国荣" data-res-pic="http://p1.music.126.net/UI_5fJZa9AHRfJ1AywjSog==/78065325577772.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="186699" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张国荣">
   <span title="张国荣"><a class="" href="/artist?id=6457" hidefocus="true">张
     <div class="soil">
      放性
     </div>国荣</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18959" title="钟情张国荣">钟情
    <div class="soil">
     提由
    </div>张国荣</a>
  </div>
  <div class="hd ">
   <span data-res-id="29723019" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">38</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=29723019"><b title="男人哭吧不是罪&nbsp;(国)">男人哭
        <div class="soil">
         千毛是样
        </div>吧不是罪&nbsp;(国)</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">06:20</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="29723019" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="29723019" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="29723019" data-res-type="18" data-res-action="share" data-res-name="男人哭吧不是罪 (国)" data-res-author="刘德华" data-res-pic="http://p1.music.126.net/-6osWky_WObfAydYYiTvpA==/3236962232773608.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="29723019" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="刘德华">
   <span title="刘德华"><a class="" href="/artist?id=3691" hidefocus="true">刘
     <div class="soil">
      照特关一素
     </div>德华</a></span>
  </div>
  <div class="text">
   <a href="/album?id=3066282" title="Wonderful&nbsp;World&nbsp;香港演唱会&nbsp;2007">Wonderful&nbsp;World
    <div class="soil">
     Ln
    </div>&nbsp;香港演唱会&nbsp;2007</a>
  </div>
  <div class="hd ">
   <span data-res-id="254191" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">39</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=254191"><b title="可惜不是你">可惜
        <div class="soil">
         众局生
        </div>不是你</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:45</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="254191" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="254191" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="254191" data-res-type="18" data-res-action="share" data-res-name="可惜不是你" data-res-author="梁静茹" data-res-pic="http://p1.music.126.net/JwUTCEySzPijv-qtzeScPQ==/109951163240621579.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="254191" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="梁静茹">
   <span title="梁静茹"><a class="" href="/artist?id=8325" hidefocus="true">梁
     <div class="soil">
      本断确
     </div>静茹</a></span>
  </div>
  <div class="text">
   <a href="/album?id=25394" title="丝路">丝
    <div class="soil">
     选适照红
    </div>路</a>
  </div>
  <div class="hd ">
   <span data-res-id="5251209" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">40</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=5251209"><b title="承诺(香港版)">承
        <div class="soil">
         定
        </div>诺(香港版)</b></a><span data-res-id="5251209" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:49</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="5251209" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="5251209" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="5251209" data-res-type="18" data-res-action="share" data-res-name="承诺(香港版)" data-res-author="郑融/林子祥/梁汉文/莫文蔚/梁咏琪/钟镇涛/郑欣宜/侧田/汪明荃/at17/方大同/许志安/谭咏麟/苏永康/曾志伟/容祖儿/泰迪罗宾/杨千嬅/王菀之/陈奕迅/肥妈/刘德华/张学友/林依伦/黄家强/李克勤/罗家英" data-res-pic="http://p1.music.126.net/gtem-77q-H1Su04EVEo5zw==/62672162800292.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="5251209" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="郑融/林子祥/梁汉文/莫文蔚/梁咏琪/钟镇涛/郑欣宜/侧田/汪明荃/at17/方大同/许志安/谭咏麟/苏永康/曾志伟/容祖儿/泰迪罗宾/杨千嬅/王菀之/陈奕迅/肥妈/刘德华/张学友/林依伦/黄家强/李克勤/罗家英">
   <span title="郑融/林子祥/梁汉文/莫文蔚/梁咏琪/钟镇涛/郑欣宜/侧田/汪明荃/at17/方大同/许志安/谭咏麟/苏永康/曾志伟/容祖儿/泰迪罗宾/杨千嬅/王菀之/陈奕迅/肥妈/刘德华/张学友/林依伦/黄家强/李克勤/罗家英"><a class="" href="/artist?id=10580" hidefocus="true">郑
     <div class="soil">
      荻缹頡
     </div>融</a>/<a class="" href="/artist?id=3706" hidefocus="true">林
     <div class="soil">
      看备都半
     </div>子祥</a>/<a class="" href="/artist?id=3722" hidefocus="true">梁
     <div class="soil">
      动是次
     </div>汉文</a>/<a class="" href="/artist?id=8926" hidefocus="true">莫
     <div class="soil">
      八华
     </div>文蔚</a>/<a class="" href="/artist?id=8329" hidefocus="true">梁
     <div class="soil">
      确己
     </div>咏琪</a>/<a class="" href="/artist?id=6495" hidefocus="true">钟
     <div class="soil">
      現
     </div>镇涛</a>/<a class="" href="/artist?id=10782" hidefocus="true">郑
     <div class="soil">
      每断
     </div>欣宜</a>/<a class="" href="/artist?id=2117" hidefocus="true">侧
     <div class="soil">
      嶙翝
     </div>田</a>/<a class="" href="/artist?id=9624" hidefocus="true">汪
     <div class="soil">
      布龙声消
     </div>明荃</a>/<a class="" href="/artist?id=11001" hidefocus="true">at
     <div class="soil">
      r4rv
     </div>17</a>/<a class="" href="/artist?id=2738" hidefocus="true">方
     <div class="soil">
      影见改活转
     </div>大同</a>/<a class="" href="/artist?id=5787" hidefocus="true">许
     <div class="soil">
      鹜
     </div>志安</a>/<a class="" href="/artist?id=5205" hidefocus="true">谭
     <div class="soil">
      忑鳻
     </div>咏麟</a>/<a class="" href="/artist?id=4948" hidefocus="true">苏
     <div class="soil">
      祚甡瑛恠
     </div>永康</a>/<a class="" href="/artist?id=6608" hidefocus="true">曾
     <div class="soil">
      幬奓捞
     </div>志伟</a>/<a class="" href="/artist?id=9269" hidefocus="true">容
     <div class="soil">
      引说而
     </div>祖儿</a>/<a class="" href="/artist?id=5207" hidefocus="true">泰迪
     <div class="soil">
      民八么任持
     </div>罗宾</a>/<a class="" href="/artist?id=10204" hidefocus="true">杨
     <div class="soil">
      下市四全角
     </div>千嬅</a>/<a class="" href="/artist?id=9608" hidefocus="true">王
     <div class="soil">
      趾鰝緤
     </div>菀之</a>/<a class="" href="/artist?id=2116" hidefocus="true">陈
     <div class="soil">
      者越结电
     </div>奕迅</a>/<a class="" href="/artist?id=226341" hidefocus="true">肥
     <div class="soil">
      稓緱
     </div>妈</a>/<a class="" href="/artist?id=3691" hidefocus="true">刘
     <div class="soil">
      粔馪
     </div>德华</a>/<a class="" href="/artist?id=6460" hidefocus="true">张
     <div class="soil">
      斗此八主
     </div>学友</a>/<a class="" href="/artist?id=226349" hidefocus="true">林
     <div class="soil">
      峗蕭瑭
     </div>依伦</a>/<a class="" href="/artist?id=3116" hidefocus="true">黄
     <div class="soil">
      糵忩慿
     </div>家强</a>/<a class="" href="/artist?id=3699" hidefocus="true">李
     <div class="soil">
      务头族号
     </div>克勤</a>/<a class="" href="/artist?id=3956" hidefocus="true">罗
     <div class="soil">
      宒暟杗
     </div>家英</a></span>
  </div>
  <div class="text">
   <a href="/album?id=511843" title="承诺">承
    <div class="soil">
     篷鍼
    </div>诺</a>
  </div>
  <div class="hd ">
   <span data-res-id="186345" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">41</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=186345"><b title="爱如潮水">爱
        <div class="soil">
         刽鶤刚驦
        </div>如潮水</b></a><span data-res-id="186345" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:32</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="186345" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="186345" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="186345" data-res-type="18" data-res-action="share" data-res-name="爱如潮水" data-res-author="张信哲" data-res-pic="http://p1.music.126.net/ns4zt4X5JPRf42h5q4F7wA==/841126395248902.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="186345" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张信哲">
   <span title="张信哲"><a class="" href="/artist?id=6454" hidefocus="true">张
     <div class="soil">
      蟹
     </div>信哲</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18933" title="张信哲精选">张信
    <div class="soil">
     生交龙当
    </div>哲精选</a>
  </div>
  <div class="hd ">
   <span data-res-id="188489" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">42</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=188489"><b title="风继续吹(Live)">风继续
        <div class="soil">
         铗
        </div>吹(Live)</b></a><span data-res-id="188489" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">06:56</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="188489" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="188489" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="188489" data-res-type="18" data-res-action="share" data-res-name="风继续吹(Live)" data-res-author="张国荣" data-res-pic="http://p1.music.126.net/FEgl2i8gDkOdppr5Ko3kEA==/69269232562640.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="188489" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张国荣">
   <span title="张国荣"><a class="" href="/artist?id=6457" hidefocus="true">张
     <div class="soil">
      满百火习点
     </div>国荣</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19078" title="张国荣告别乐坛演唱会">张国荣
    <div class="soil">
     拉家算
    </div>告别乐坛演唱会</a>
  </div>
  <div class="hd ">
   <span data-res-id="65528" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">43</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=65528"><b title="淘汰">淘
        <div class="soil">
         铊
        </div>汰</b></a><span data-res-id="65528" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:45</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="65528" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="65528" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="65528" data-res-type="18" data-res-action="share" data-res-name="淘汰" data-res-author="陈奕迅" data-res-pic="http://p1.music.126.net/o_OjL_NZNoeog9fIjBXAyw==/18782957139233959.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="65528" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陈奕迅">
   <span title="陈奕迅"><a class="" href="/artist?id=2116" hidefocus="true">陈
     <div class="soil">
      五收义想
     </div>奕迅</a></span>
  </div>
  <div class="text">
   <a href="/album?id=6434" title="认了吧">认
    <div class="soil">
     骥貂鎶荻
    </div>了吧</a>
  </div>
  <div class="hd ">
   <span data-res-id="186490" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">44</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=186490"><b title="心跳呼吸正常">心跳
        <div class="soil">
         而教关
        </div>呼吸正常</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:28</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="186490" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="186490" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="186490" data-res-type="18" data-res-action="share" data-res-name="心跳呼吸正常" data-res-author="张国荣" data-res-pic="http://p1.music.126.net/2YIpNoCzXfYgz4zIw3s0Vg==/73667279073787.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="186490" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张国荣">
   <span title="张国荣"><a class="" href="/artist?id=6457" hidefocus="true">张
     <div class="soil">
      羗樖勬
     </div>国荣</a></span>
  </div>
  <div class="text">
   <a href="/album?id=18937" title="I&nbsp;Am&nbsp;What&nbsp;I&nbsp;Am">I&nbsp;Am&nbsp;What
    <div class="soil">
     IK
    </div>&nbsp;I&nbsp;Am</a>
  </div>
  <div class="hd ">
   <span data-res-id="190449" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">45</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=190449"><b title="吻别">吻
        <div class="soil">
         溁
        </div>别</b></a><span data-res-id="190449" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:06</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="190449" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="190449" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="190449" data-res-type="18" data-res-action="share" data-res-name="吻别" data-res-author="张学友" data-res-pic="http://p1.music.126.net/636SSPpKW0avAqkK1QgzgQ==/43980465112096.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="190449" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张学友">
   <span title="张学友"><a class="" href="/artist?id=6460" hidefocus="true">张
     <div class="soil">
      哋
     </div>学友</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19243" title="吻别">吻
    <div class="soil">
     治干见
    </div>别</a>
  </div>
  <div class="hd ">
   <span data-res-id="66476" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">46</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=66476"><b title="偏偏喜欢你">偏
        <div class="soil">
         负忔偵薽
        </div>偏喜欢你</b></a><span data-res-id="66476" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:31</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="66476" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="66476" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="66476" data-res-type="18" data-res-action="share" data-res-name="偏偏喜欢你" data-res-author="陈百强" data-res-pic="http://p1.music.126.net/gbeP6upLG0PFp8ecmy0-7w==/109951163240606902.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="66476" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="陈百强">
   <span title="陈百强"><a class="" href="/artist?id=2115" hidefocus="true">陈
     <div class="soil">
      謜屔蛊謜
     </div>百强</a></span>
  </div>
  <div class="text">
   <a href="/album?id=6519" title="偏偏喜欢你">偏偏喜
    <div class="soil">
     规们要即
    </div>欢你</a>
  </div>
  <div class="hd ">
   <span data-res-id="189895" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">47</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=189895"><b title="有没有一首歌会让你想起我">有没有一
        <div class="soil">
         鬛臜綀
        </div>首歌会让你想起我</b></a></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">03:57</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="189895" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="189895" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="189895" data-res-type="18" data-res-action="share" data-res-name="有没有一首歌会让你想起我" data-res-author="周传雄" data-res-pic="http://p1.music.126.net/7qj5TKx51l02wgiuXAspFA==/109951163432572665.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="189895" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="周传雄">
   <span title="周传雄"><a class="" href="/artist?id=6652" hidefocus="true">周
     <div class="soil">
      进育周报
     </div>传雄</a></span>
  </div>
  <div class="text">
   <a href="/album?id=19191" title="Dubbing&nbsp;1987-2003新歌+经典">Dubbing&nbsp;1987-2003
    <div class="soil">
     工照
    </div>新歌+经典</a>
  </div>
  <div class="hd ">
   <span data-res-id="387635" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">48</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=387635"><b title="假如">假
        <div class="soil">
         礜
        </div>如</b></a><span data-res-id="387635" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">04:24</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="387635" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="387635" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="387635" data-res-type="18" data-res-action="share" data-res-name="假如" data-res-author="信乐团" data-res-pic="http://p1.music.126.net/U3uwHEdkkp-wXBynNYEVjg==/119846767442613.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="387635" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="信乐团">
   <span title="信乐团"><a class="" href="/artist?id=13283" hidefocus="true">信
     <div class="soil">
      鲊
     </div>乐团</a></span>
  </div>
  <div class="text">
   <a href="/album?id=38400" title="挑信">挑
    <div class="soil">
     筟媼
    </div>信</a>
  </div>
  <div class="hd ">
   <span data-res-id="326904" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">49</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=326904"><b title="如果你也听说">如果你
        <div class="soil">
         影建厂团看
        </div>也听说</b></a><span data-res-id="326904" data-res-action="mv" title="播放mv" class="mv">MV</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">05:13</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="326904" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="326904" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="326904" data-res-type="18" data-res-action="share" data-res-name="如果你也听说" data-res-author="张惠妹" data-res-pic="http://p1.music.126.net/-ZRQT0sqWRu2y-cMT8mmvA==/109951163265779897.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="326904" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="张惠妹">
   <span title="张惠妹"><a class="" href="/artist?id=10559" hidefocus="true">张
     <div class="soil">
      各多
     </div>惠妹</a></span>
  </div>
  <div class="text">
   <a href="/album?id=32338" title="Star">St
    <div class="soil">
     c5
    </div>ar</a>
  </div>
  <div class="hd ">
   <span data-res-id="26090155" data-res-type="18" data-res-action="play" data-res-from="13" data-res-data="2342830892" class="ply ">&nbsp;</span>
   <span class="num">50</span>
  </div>
  <div class="f-cb">
   <div class="tt">
    <div class="ttc">
     <span class="txt"><a href="/song?id=26090155"><b title="送别 - ((电影《厨子戏子痞子》片尾曲))">送
        <div class="soil">
         溆渫氦
        </div>别</b></a><span title="(电影《厨子戏子痞子》片尾曲)" class="s-fc8"> - ((电影《厨子戏子痞子》片尾
       <div class="soil">
        前天局知例
       </div>曲))</span></span>
    </div>
   </div>
  </div>
  <span class="u-dur ">02:52</span>
  <div class="opt hshow">
   <a class="u-icn u-icn-81 icn-add" href="javascript:;" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="26090155" data-res-action="addto" data-res-from="13" data-res-data="2342830892"></a>
   <span data-res-id="26090155" data-res-type="18" data-res-action="fav" class="icn icn-fav" title="收藏"></span>
   <span data-res-id="26090155" data-res-type="18" data-res-action="share" data-res-name="送别" data-res-author="朴树" data-res-pic="http://p1.music.126.net/4k12UxIfZK9lUDPZIzSYlg==/2442015325313098.jpg" class="icn icn-share" title="分享">分享</span>
   <span data-res-id="26090155" data-res-type="18" data-res-action="download" class="icn icn-dl" title="下载"></span>
  </div>
  <div class="text" title="朴树">
   <span title="朴树"><a class="" href="/artist?id=4721" hidefocus="true">朴
     <div class="soil">
      称其厂因火
     </div>树</a></span>
  </div>
  <div class="text">
   <a href="/album?id=2390018" title="送别">送
    <div class="soil">
     养格报表光
    </div>别</a>
  </div>
 </body>
</html>'''
ht = re.sub('&nbsp;','',html)
results = re.findall('<b\stitle="(.*?)">.*?"text"\stitle="(.*?)".*?u-dur\s">(.*?)</span>.*?<a\shref=".album\?(.*?)"\stitle="(.*?)">',ht,re.S)
with open('songs.txt','w') as f:
    name =''
    for i in results:
        if len(i[0]) < 4:
            name = f'{i[0]}\t\t\t\t'
        elif len(i[0]) < 8:
            name = f'{i[0]}\t\t\t'
        elif len(i[0]) < 12:
            name = f'{i[0]}\t\t'
        elif len(i[0]) < 16:
            name = f'{i[0]}\t'
        elif len(i[0]) < 20:
            name = f'{i[0]}\t'
        else:
            name = f'{i[0]}'
        print(name+':'+i[1]+'-'+i[2]+' \t专辑：'+i[4]+f'--http://music.163.com/#/album?{i[3]}')
        line = f'{name}:{i[1]}-{i[2]} \t专辑：{i[4]}--http://music.163.com/#/album?{i[3]}\n'
        f.write(line)
    f.close()