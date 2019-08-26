import requests
def download(url, fileName='tmp.zip'):
    content = requests.get(url, stream = True)
    with open(fileName, "wb") as target_file:
        for chunk in content.iter_content(chunk_size = 1024):
            if chunk:
                target_file.write(chunk)

def download2(url, file_name="tmp"):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print(f"Downloading: {file_name} Bytes: {file_size}")

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print(status)

	f.close()

def extact(path, target_path=''):
    from zipfile import ZipFile
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall(target_path)

url = "https://github.com/FormatMemory/AutoSSR/raw/master/ssr.zip"
download(url, 'tmp.zip')
extact('tmp.zip', 'ssr')
import subprocess
subprocess.call([r"ssr//ShadowsocksR-dotnet4.0.exe"])
