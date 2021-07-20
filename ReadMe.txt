=============================================
运行方式：
	1.打开Fiddler开始抓包
	2.打开浏览器的Tik Tok网站并开始滑动
	3.运行视频下载python脚本
=============================================
爬取Tik Tok视频实现流程：
	1.鼠标自动滑动功能实现浏览器翻页
	2.fiddler抓包后在fiddlerScript中加入自动保存指定url的代码
	3.保存后通过python在后端对url进行视频下载保存
=============================================
在Fiddler的function OnBeforeRequest结尾加入的代码：
        //过滤无关请求，只关注特定请求 
        if (oSession.fullUrl.Contains("tiktokcdn.com")) { 
            var fso;
            var file; 
            fso = new ActiveXObject("Scripting.FileSystemObject");
            //文件保存路径，可自定义 
            file = fso.OpenTextFile("C:\\Users\\Administrator\\Desktop\\mytest\\Temp\\data.txt",8 , true, true);

            file.writeLine(oSession.url);  // + "RequestUrl:"

            //file.writeLine("Request header:" + "\n" + oSession.oRequest.headers); 
            //file.writeLine("Request body: " + oSession.GetRequestBodyAsString()); 
            file.writeLine("\n"); 
            file.close(); 
        }
=============================================


	