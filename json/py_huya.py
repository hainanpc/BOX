#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json

class Spider(Spider):
	def getName(self):
		return "虎牙"
	def init(self,extend=""):
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"一起看": "一起看",
			"三国杀": "三国杀",
			"网游竞技": "网游竞技",
"英雄联盟": "英雄联盟",
"王者荣耀": "王者荣耀",
"英雄联盟电竞经理": "英雄联盟电竞经理",
"一起看": "一起看",
"户外": "户外",
"和平精英": "和平精英",
"美食": "美食",
"综合手游": "综合手游",
"暴雪专区": "暴雪专区",
"颜值": "颜值",
"CF手游": "CF手游",
"交友": "交友",
"地下城与勇士": "地下城与勇士",
"新游广场": "新游广场",
"体育": "体育",
"棋牌桌游": "棋牌桌游",
"我的世界": "我的世界",
"炉石传说": "炉石传说",
"魔兽世界": "魔兽世界",
"CS:GO": "CS:GO",
"DOTA1": "DOTA1",
"QQ飞车": "QQ飞车",
"娱乐天地": "娱乐天地",
"放映厅": "放映厅",
"虎牙地方": "虎牙地方",
"传奇": "传奇",
"御龙在天": "御龙在天",
"军事游戏": "军事游戏",
"传奇类游戏": "传奇类游戏",
"射击综合游戏": "射击综合游戏",
"幻塔": "幻塔",
"战争冲突": "战争冲突",
"虎牙领主争霸": "虎牙领主争霸",
"王者模拟战": "王者模拟战",
"Dread Hunger": "Dread Hunger",
"艾尔登法环": "艾尔登法环",
"永恒之塔": "永恒之塔",
"英魂之刃": "英魂之刃",
"第五人格": "第五人格",
"COD手游": "COD手游",
"虚拟偶像": "虚拟偶像",
"音乐": "音乐",
"CFHD": "CFHD",
"热血江湖": "热血江湖",
"枪神纪": "枪神纪",
"NBA2KOL系列": "NBA2KOL系列",
"旅游": "旅游",
"刀剑英雄": "刀剑英雄",
"流放之路": "流放之路",
"摔跤城大乱斗": "摔跤城大乱斗",
"诛仙世界": "诛仙世界",
"QQ华夏": "QQ华夏",
"奶块": "奶块",
"生死狙击": "生死狙击",
"部落冲突": "部落冲突",
"魔兽世界怀旧服": "魔兽世界怀旧服",
"香肠派对": "香肠派对",
"恐鬼症": "恐鬼症",
"创造与魔法": "创造与魔法",
"完美世界手游": "完美世界手游",
"率土之滨": "率土之滨",
"星球大战系列": "星球大战系列",
"SKY光遇": "SKY光遇",
"铁甲雄兵": "铁甲雄兵",
"JJ棋牌": "JJ棋牌",
"派对": "派对",
"FIFA Online系列": "FIFA Online系列",
"SCUM": "SCUM",
"超击突破": "超击突破",
"港诡实录": "港诡实录",
"丝路传说2": "丝路传说2",
"007：传奇": "007：传奇",
"天下": "天下",
"极限竞速：地平线": "极限竞速：地平线",
"龙之谷2手游": "龙之谷2手游",
"蛋仔派对": "蛋仔派对",
"虎牙球球": "虎牙球球",
"Badlanders": "Badlanders",
"激战2": "激战2",
"征途2手游": "征途2手游",
"剑灵：革命": "剑灵：革命",
"绝世仙王": "绝世仙王",
"超激斗梦境": "超激斗梦境",
"航海王：燃烧意志": "航海王：燃烧意志",
"红警OL": "红警OL",
"使命召唤系列": "使命召唤系列",
"猎人：荒野的召唤": "猎人：荒野的召唤",
"真·三国无双OL": "真·三国无双OL",
"VALORANT": "VALORANT",
"FF14": "FF14",
"不良人2": "不良人2",
"坎公骑冠剑": "坎公骑冠剑",
"瑞奇与叮当": "瑞奇与叮当",
"最终幻想：起源": "最终幻想：起源",
"玄天之剑": "玄天之剑",
"逃脱者2": "逃脱者2",
"远征军：征服者": "远征军：征服者",
"黑暗领域2": "黑暗领域2",
"精灵与萤火意志": "精灵与萤火意志",
"三国": "三国",
"神界2": "神界2",
"诺亚之心": "诺亚之心",
"梦想世界3手游": "梦想世界3手游",
"一起玩农场": "一起玩农场",
"EVE Online": "EVE Online",
"龙族血统": "龙族血统",
"切尔诺贝利突击队": "切尔诺贝利突击队",
"蜀门": "蜀门",
"鹿鼎记": "鹿鼎记",
"五子棋": "五子棋",
"格斗游戏": "格斗游戏",
"环绕走廊": "环绕走廊",
"天穗之咲稻姬": "天穗之咲稻姬",
"重写三国志": "重写三国志",
"Factorio": "Factorio",
"互动点播": "互动点播",
"Dread Hunger": "Dread Hunger",
"星秀": "星秀",
"户外": "户外",
"二次元": "二次元",
"一起看": "一起看",
"美食": "美食",
"颜值": "颜值",
"交友": "交友",
"体育": "体育",
"组队": "组队",
"王者荣耀": "王者荣耀",
"和平精英": "和平精英",
"LOL电竞经理": "LOL电竞经理",
"LOL手游": "LOL手游",
"新游广场": "新游广场",
"金铲铲之战": "金铲铲之战",
"暗区突围": "暗区突围",
"火影忍者手游": "火影忍者手游",
"CF手游": "CF手游",
"棋牌休闲": "棋牌休闲",
"原神": "原神",
"综合手游": "综合手游",
"暗黑破坏神：不朽": "暗黑破坏神：不朽",
"环形战争": "环形战争",
"二次元手游": "二次元手游",
"下载客户端": "下载客户端",
"我要直播": "我要直播"


			
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name': k,
				'type_id': cateManual[k]
			})

		result['class'] = classes
		if (filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		url = 'http://live.yj1211.work/api/live/getRecommendByPlatformArea?platform=huya&size=20&area={0}&page={1}'.format(tid, pg)
		rsp = self.fetch(url)
		content = rsp.text
		jo = json.loads(content)
		videos = []
		vodList = jo['data']
		for vod in vodList:
			aid = (vod['roomId']).strip()
			title = vod['roomName'].strip()
			img = vod['roomPic'].strip()
			remark = (vod['categoryName']).strip()
			videos.append({
				"vod_id": aid,
				"vod_name": title,
				"vod_pic": img,
				"vod_remarks": remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def detailContent(self,array):
		aid = array[0]
		url = "http://live.yj1211.work/api/live/getRoomInfo?platform=huya&roomId={0}".format(aid)
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['roomName']
		pic = jo['roomPic']
		desc = str(jo['online'])
		dire = jo['ownerName']
		typeName = jo['categoryName']
		remark = jo['categoryName']
		vod = {
			"vod_id": aid,
			"vod_name": title,
			"vod_pic": pic,
			"type_name": typeName,
			"vod_year": "",
			"vod_area": "",
			"vod_remarks": remark,
			"vod_actor": '在线人数:' + desc,
			"vod_director": dire,
			"vod_content": ""
		}
		playUrl = '原画' + '${0}#'.format(aid)
		vod['vod_play_from'] = '虎牙直播'
		vod['vod_play_url'] = playUrl

		result = {
			'list': [
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {}

		url = 'https://mp.huya.com/cache.php?m=Live&do=profileRoom&roomid={0}'.format(id)
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['stream']['baseSteamInfoList'][0]['sStreamName']
		url = 'http://txtest-xp2p.p2p.huya.com/src/' + ja + '.xs?ratio=4000'

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	config = {
		"player": {},
		"filter": {}
	}
	header = {}
	def localProxy(self,param):
		action = {
			'url':'',
			'header':'',
			'param':'',
			'type':'string',
			'after':''
		}
		return [200, "video/MP2T", action, ""]
