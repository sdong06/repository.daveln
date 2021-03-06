# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/>  
'''                                                                           

import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon

mysettings=xbmcaddon.Addon(id='plugin.video.nettivi')
profile=mysettings.getAddonInfo('profile')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
viet_simpletv='https://raw.githubusercontent.com/giolao/Viet-Simpletv/master/new_playlist.m3u'
tvchannels='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/tvchannels.json'
haotivi='https://raw.githubusercontent.com/daveln/repository.daveln/master/playlists/haotivi.json'
vtcplay='http://117.103.206.21:88/Channel/GetChannels'
htvonline='http://www.htvonline.com.vn/livetv'
fptplay='http://fptplay.net'
tv24vn='http://www.tv24.vn'
zuitv='http://zui.vn/livetv.html'
token = 'token=1b#K8!3zc65ends!'

def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req, timeout=120)
    link=response.read()
    response.close()  
    return link
  except urllib2.URLError, e:
    print 'We failed to open "%s".' % url
    if hasattr(e, 'code'):
      print 'We failed with error code - %s.' % e.code	
    if hasattr(e, 'reason'):
      print 'We failed to reach a server.'
      print 'Reason: ', e.reason
 	  
def main():
  addDir('[COLOR lime]HD [COLOR cyan]Channels[/COLOR]','hdchannels',8,logos+'hd.png')
  addDir('[COLOR yellow]TV Hải Ngoại   ++   [COLOR cyan]Âm Nhạc   ++   [COLOR lime]Radio[/COLOR]',tvchannels,7,logos+'tivihn.png')
  addDir('[COLOR deeppink]Access Asia Network[/COLOR]',tvchannels,7,logos+'accessasia.png')
  addDir('[COLOR lightblue]FPTPlay[/COLOR]',fptplay,2,logos+'fptplay.png')
  addDir('[COLOR cyan]haotivi[/COLOR]',haotivi,1,logos+'hao.png')		
  #addDir('[COLOR orange]VTCPlay[/COLOR]',vtcplay,7,logos+'vtcplay.png')
  addDir('[COLOR yellow]VietSimple TV[/COLOR]',viet_simpletv,10,logos+'vietsimpletv.png')  
  addDir('[COLOR cyan]VTC[/COLOR]',tvchannels,7,logos+'vtccomvn.png')		
  addDir('[COLOR magenta]HTVOnline[/COLOR]',htvonline,6,logos+'htvonline.png')
  addDir('[COLOR lime]TV24VN    [COLOR lime]>[COLOR magenta]>[COLOR orange]>[COLOR yellow]>    [COLOR yellow]SCTV[/COLOR]',tv24vn,6,logos+'tv24vn.png')				
  #addDir('[COLOR white]Zui Live TV[/COLOR]',zuitv,6,logos+'zui.png')
  addLink('[COLOR lightgreen]Little Sai Gon TV[/COLOR]','http://stream.s15.cpanelservices.com/lstvlive/livestream/playlist.m3u8',logos+'littlesaigon.png')	
  addLink('[COLOR silver]Animal Planet[/COLOR]','http://202.75.23.34:80/live/ch31//01.m3u8',logos+'ap.png')	
  addLink('[COLOR violet]Discovery Channel[/COLOR]','http://202.75.23.34:80/live/ch29/01.m3u8',logos+'discovery.png')	
  addLink('[COLOR pink]Discovery HD World[/COLOR]','http://202.75.23.34:80/live/ch30/01.m3u8',logos+'dischd.png')	
  addLink('[COLOR olive]Discovery Science[/COLOR]','http://202.75.23.34:80/live/ch33/01.m3u8',logos+'discsc.png')	
  addLink('[COLOR gold]History Channel[/COLOR]','http://202.75.23.36:80/live/ch45/01.m3u8',logos+'history.png')	
  addLink('[COLOR chocolate]NatGeo Wild[/COLOR]','http://202.75.23.35:80/live/ch39/01.m3u8',logos+'natgeowild.png')	
  addLink('[COLOR blue]National Geographic[/COLOR]','http://202.75.23.35:80/live/ch38/01.m3u8',logos+'natgeo.png')

def vietsimpletv(url):
  content=makeRequest(url)	
  match=re.compile('#EXTINF.+?,(.+)\s([^"]*)\n').findall(content)
  for name,url in match:
    if 'htvonline' in url:
	    add_Link('[COLOR cyan]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')
    elif 'tv24.vn' in url:  
      addLink('[COLOR lime]'+name+'[/COLOR]',url.replace('rtmp://$OPT:rtmp-raw=',''),logos+'vietsimpletv.png')
    elif 'torrent-tv.ru' in url:  
      addLink('[COLOR magenta]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')
    elif 'xemphimso' in url:  
      addDir('[COLOR blue]'+name+'[/COLOR]',url,7,logos+'vietsimpletv.png')	  
    elif 'radiovietnam' in url or 'VOA News' in name  or 'NHK Vietnam' in name  or 'RFI Vietnam' in name  or 'VOH' in name:  
      addLink('[COLOR orange]'+name+'  -  [COLOR lightgreen]Radio[/COLOR]',url,logos+'vietsimpletv.png')	 
    elif 'accessasia' in url:  
      addLink('[COLOR silver]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')		  
    else:  
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,logos+'vietsimpletv.png')		  
  
def fpt(url):
  #addDir('[COLOR cyan]Tìm FPTPlay\'s Video[B]   [COLOR cyan]>[COLOR yellow]>[COLOR lime]>[COLOR orange]>   [/B][COLOR orange]Video Search[/COLOR]',fptplay,11,logos+'fptplay.png')		 
  content=makeRequest(url)	
  match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(content)
  for url,name in match:
    if 'livetv' in url:
      addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,6,logos+'fptplay.png')
    else: 
      pass
'''      
    elif 'film' in url or 'livetv' in url:
      pass	
    else:
      addDir('[COLOR lime]'+name+'[/COLOR]',fptplay+url,4,logos+'fptplay.png')			
'''
def mediaList(url):	
  content=makeRequest(url)
  match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
  for url,thumbnail,name in match:	
    addDir('[COLOR lime]'+name.replace('&amp;','[COLOR cyan]và')+'[/COLOR]',fptplay+url,5,thumbnail)
  match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
  for url,name in match:	
    addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,3,logos+'fptplay.png')
	  	  
def dirs(url):
  content=makeRequest(url)
  match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(content)
  for url,name in match:	
    addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,3,logos+'fptplay.png')
	
def episodes(url):
  content=makeRequest(url)
  title=re.compile('<title>([^\']+)</title>').findall(content)		
  match=re.compile("<a href=\"\/Video([^\"]*)\">(.*?)<\/a><\/li>").findall(content)
  for url,name in match:
    add_Link(('%s   -   %s' % ('[COLOR lime]Tập '+name,'[COLOR yellow]'+title[-1].replace('&amp;','[COLOR cyan]và')+'[/COLOR]')),('%sVideo%s' % (fptplay, url)),logos+'fptplay.png')
	
def index(url):
  content=makeRequest(url)
  if 'tv24' in url:
	  match=re.compile("<SPAN id=\".+?\"><a href='(.+?)'><img src='(.+?)' onmouseover=\"this.src='http:\/\/tv24.vn\/WebMedia\/Channels\/\d+\/(.+?).png'").findall(content)
	  for url,thumbnail,name in match:
	    if 'vtv' in name:
	      add_Link('[COLOR yellow][UPPERCASE]'+name+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),thumbnail)	  
	    else:	  
	      add_Link('[COLOR lime][UPPERCASE]'+name.replace('b','')+'[/UPPERCASE][/COLOR]',('%s%s' % (tv24vn, url)),thumbnail)
  elif 'htvonline' in url:
	  match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(content)
	  for url,name,thumbnail in match:
	    add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)  
  elif 'fptplay' in url:
	  match=re.compile("channel=\"(.*?)\" href=\".+?\" data=\"(.+?)\" adsstatus.+?>\s+<img src=\"(.*?)\"").findall(content)
	  for name,url,thumbnail in match:
	    if 'VOVTV' in name or 'OneTV' in name or 'VTV3' in name or 'VTV6' in name:
	      add_Link('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,thumbnail)	  
	    else:
	      add_Link('[COLOR lime]'+name.replace('&#39;','\'')+'[/COLOR]',fptplay+url,thumbnail)						
  elif 'zui' in url:
    match=re.compile("alt='(.+?)' href='(.+?)'><img src='(.+?)'").findall(content)[3:36]
    for name,url,thumbnail in match:
      if 'SCTV1' in name or 'VTC14' in name or 'ITV' in name or 'Nhạc của tui' in name or 'Thuần Việt' in name:
	      add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)	  
      else:
        pass
		
def videoLinks(url,name):
  content=makeRequest(url)
  if 'xemphimso' in url:
    match=re.compile("file: '(.+?)'").findall(content)
    for url in match:
      addLink(name,url,logos+'vietsimpletv.png')	  	  
  elif 'Access Asia Network' in name:
    match=re.compile("\"BroadcastStation\":\"accessasia\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'TV Hải Ngoại' in name:
    match=re.compile("\"BroadcastStation\":\"haingoaitv\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)										
  elif 'VTCPlay' in name:
    match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"").findall(content)
    for name,thumbnail,url in match:
      addLink('[COLOR yellow]'+name.decode("utf-8")+'[/COLOR]',url,thumbnail)						
  elif 'VTC' in name:
    match=re.compile("\"BroadcastStation\":\"vtccomvn\",\"Channel\":\"(.*?)\",\"Path\":\"([^\"]*)\",\"Thumbnail\":\"(.+?)\"").findall(content)
    for name,url,thumbnail in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)								
  elif 'Việt Nam' in name:
    match=re.compile("\"lang\":\"vi\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR yellow]'+name+'[/COLOR]',url,logos+'vn.png')
  elif 'Spain' in name:		
    match=re.compile("\"lang\":\"sp\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR pink]'+name+'[/COLOR]',url,logos+'sp.png')
  elif 'France' in name:						
    match=re.compile("\"lang\":\"fr\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR orange]'+name+'[/COLOR]',url,logos+'fr.png')
  elif 'Hong Kong' in name:						
    match=re.compile("\"lang\":\"hk\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR blue]Hong Kong - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'hk.png')
  elif 'Taiwan' in name:			
    match=re.compile("\"lang\":\"tw\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR magenta]Taiwan - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'tw.png')
  elif 'US' in name:		
    match=re.compile("\"lang\":\"us\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR lime]'+name+'[/COLOR]',url,logos+'us.png')
  elif 'China' in name:						
    match=re.compile("\"lang\":\"cn\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR cyan]China - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'cn.png')
  elif 'Brazil' in name:		
    match=re.compile("\"lang\":\"br\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR silver]'+name+'[/COLOR]',url,logos+'br.png')
  elif 'Korea' in name:		
    match=re.compile("\"lang\":\"ko\".*?:\"([^\"]*)\",\"title\":\".+?\",\"uid\":\"(.*?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR deeppink]Korea - [COLOR yellow]channel  '+name+'[/COLOR]',url,logos+'ko.png')
  elif 'Thailand' in name:		
    match=re.compile("\"lang\":\"th\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR gold]'+name+'[/COLOR]',url,logos+'th.png')
  elif 'Japan' in name:						
    match=re.compile("\"lang\":\"ja\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR tomato]'+name+'[/COLOR]',url,logos+'ja.png')
  elif 'Indonesia' in name:		
    match=re.compile("\"lang\":\"id\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR tan]'+name+'[/COLOR]',url,logos+'id.png')
  elif 'Malaysia' in name:						
    match=re.compile("\"lang\":\"my\".*?:\"([^\"]*)\",\"title\":\"(.+?)\"").findall(content)
    for url,name in match:
      addLink('[COLOR coral]'+name+'[/COLOR]',url,logos+'my.png')
	  
def hao():						
  #addDir('[COLOR yellow]Việt Nam[/COLOR]',haotivi,7,logos+'vn.png')
  addDir('[COLOR lime]US[/COLOR]',haotivi,7,logos+'us.png')
  addDir('[COLOR orange]France[/COLOR]',haotivi,7,logos+'fr.png')
  addDir('[COLOR blue]Hong Kong[/COLOR]',haotivi,7,logos+'hk.png')
  addDir('[COLOR magenta]Taiwan[/COLOR]',haotivi,7,logos+'tw.png')
  addDir('[COLOR cyan]China[/COLOR]',haotivi,7,logos+'cn.png')
  addDir('[COLOR silver]Brazil[/COLOR]',haotivi,7,logos+'br.png')
  addDir('[COLOR pink]Spain[/COLOR]',haotivi,7,logos+'sp.png')
  addDir('[COLOR tomato]Japan[/COLOR]',haotivi,7,logos+'ja.png')
  addDir('[COLOR deeppink]Korea[/COLOR]',haotivi,7,logos+'ko.png')
  addDir('[COLOR gold]Thailand[/COLOR]',haotivi,7,logos+'th.png')
  addDir('[COLOR tan]Indonesia[/COLOR]',haotivi,7,logos+'id.png')
  addDir('[COLOR coral]Malaysia[/COLOR]',haotivi,7,logos+'my.png')
	  
def HD():
  add_Link('[COLOR lime]National Geographic HD[/COLOR]','http://www.htvonline.com.vn/livetv/national-geographic-3132366E61.html',logos+'natgeohd.png')
  add_Link('[COLOR lime]Discovery World HD[/COLOR]','http://www.htvonline.com.vn/livetv/discovery-hd-3132336E61.html',logos+'dischd.png')
  add_Link('[COLOR lime]FOX SPORTS PLUS HD[/COLOR]','http://www.htvonline.com.vn/livetv/espn-hd-3132346E61.html',logos+'foxsporthd.png')	  
  content=makeRequest(htvonline)  
  match=re.compile("<a class=\"mh-grids5-img\" href=\"([^\"]*)\" title=\"(.+?)\">\s.*?\s*<img src=\"(.*?)\"").findall(content)
  for url,name,thumbnail in match:	
    if 'HTV7' in name or 'HTV9' in name or ' HD' in name or 'htv2-31336E61' in url:
	    add_Link('[COLOR cyan]'+name+'[/COLOR]',url,thumbnail)
  add_Link('[COLOR cyan]FBNC HD[/COLOR]','http://www.htvonline.com.vn/livetv/fbnc-34306E61.html',logos+'fnbchd.png')
'''  
  content=makeRequest(vtcplay)  
  match=re.compile("\"Name\":\"(.*?)\".+?\"Thumbnail2\":\"(.+?)\".+?\"Path\":\"([^\"]*)\"").findall(content)
  for name,thumbnail,url in match:
    if ' HD' in name:
	    addLink('[COLOR yellow]'+name.decode("utf-8")+'[/COLOR]',url,thumbnail)
'''	  
	  
def search():
  try:
    keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    url=fptplay+'Search/'+searchText
    print "Searching URL: "+url	
    mediaList(url)
  except: pass
	  
def resolveUrl(url):
  content=makeRequest(url)
  if 'htvonline' in url:		
    mediaUrl=re.compile("file: \"([^\"]*)\"").findall(content)[0]	
  elif 'tv24' in url:
    videoUrl=re.compile('\'file\': \'http([^\']*)\/playlist.m3u8').findall(content)[0]
    mediaUrl='rtmpe' + videoUrl + ' swfUrl=http://tv24.vn/getflash.ashx pageUrl=http://tv24.vn/ ' + token   
  elif 'zui' in url:
    mediaUrl=re.compile('livetv_play\(\'player\', \'1\', \'(.+?)\'\)').findall(content)[0]	
  elif 'fptplay' in url:
    if 'livetv' in url: 
      #mediaUrl=re.compile('"hls_stream": "(.+?)"').findall(content)[0] # ?token=c335VydmVyX3RpbWU9MTQwMjYxNzIyNCZoYXNoX3ZhbHVl&did=NzIyNCZoYXNoX3ZhbHVl
      mediaUrl=re.compile('"adapt_hls": "(.+?)"').findall(content)[0]   # No token    
    else:
	    mediaUrl=re.compile('"<source src=\'([^\']*)\'').findall(content)[0] 
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return
 	  	
def get_params():
  param=[]
  paramstring=sys.argv[2]
  if len(paramstring)>=2:
    params=sys.argv[2]
    cleanedparams=params.replace('?','')
    if (params[len(params)-1]=='/'):
      params=params[0:len(params)-2]
    pairsofparams=cleanedparams.split('&')
    param={}
    for i in range(len(pairsofparams)):
      splitparams={}
      splitparams=pairsofparams[i].split('=')
      if (len(splitparams))==2:
        param[splitparams[0]]=splitparams[1]
  return param
	
def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
 	
def addLink(name,url,iconimage):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
  return ok
  
def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=9"  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
	  
params=get_params()
url=None
name=None
mode=None

try:
  url=urllib.unquote_plus(params["url"])
except:
  pass
try:
  name=urllib.unquote_plus(params["name"])
except:
  pass
try:
  mode=int(params["mode"])
except:
  pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
  main()

elif mode==1:
  hao()
		
elif mode==2:
  fpt(url)
		
elif mode==3:
  mediaList(url)
		
elif mode==4:
  dirs(url)
		
elif mode==5:
  episodes(url)
		
elif mode==6:
  index(url)
		
elif mode==7:
  videoLinks(url,name)

elif mode==8:
  HD()
  
elif mode==9:
  resolveUrl(url)
  
elif mode==10:
  vietsimpletv(url) 

elif mode==11:
  search()  
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))