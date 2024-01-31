import tagesschau
import blink
import ardaudio
from mdutils.mdutils import MdUtils
from datetime import date

ts = tagesschau.headlines()
bl = blink.free()
ard = ardaudio.table()

mdFile = MdUtils(file_name="Readme", title= "Daily Information")

tag = date.today()
mdFile.new_header(1, str(tag))
mdFile.new_header(2, "Tagesschau")

for item in ts:
	mdFile.new_line(mdFile.new_inline_link(item["url"], item["hl"]))

mdFile.new_header(2, "Blink")

mdFile.new_line(mdFile.new_inline_link(bl["url"], bl["title"]+": "+ bl["subtitle"]))

mdFile.new_header(2,"täglicher Podcast")

for item in ard:
	mdFile.new_line(mdFile.new_inline_link(item["url"], item["title"]))

mdFile.create_md_file()

print("MD created")