import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def generate_epg():
    tv = ET.Element('tv', generator_info_name='MyEPG')
    
    # 只保留【體育賽事類】頻道 (頻道ID, 播放清單完整台名, 台標Logo網址)
    channels = [
        ('videoland_sports', '[TW-I] 22 緯來體育台', 'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_sports.png'),
        ('videoland_sports_a', '[TW-I] 22 緯來體育台 (a)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_sports.png'),
        ('videoland_sports_b', '[TW-I] 22 緯來體育台 (b)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_sports.png'),
        ('videoland_sports_c', '[TW-I] 22 緯來體育台 (c)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_sports.png'),
        ('dazn1', '[TW-I] 64 DAZN 1', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn1.png'),
        ('dazn1_a', '[TW-I] 64 DAZN 1 (a)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn1.png'),
        ('dazn1_b', '[TW-I] 64 DAZN 1 (b)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn1.png'),
        ('dazn2', '[TW-I] 65 DAZN 2', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn2.png'),
        ('dazn2_a', '[TW-I] 65 DAZN 2 (a)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn2.png'),
        ('dazn2_b', '[TW-I] 65 DAZN 2 (b)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn2.png'),
        ('dazn2_c', '[TW-I] 65 DAZN 2 (c)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn2.png'),
        ('elta1_backup', '[TW-I] 66 愛爾達體育1台|備 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta1.png'),
        ('elta1_1080p', '[TW-I] 66 愛爾達體育1台 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta1.png'),
        ('elta1_720p', '[TW-I] 66 愛爾達體育1台 (720p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta1.png'),
        ('elta1_live', '[TW-I] 66 愛爾達體育1台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta1.png'),
        ('elta2_1080p', '[TW-I] 67 愛爾達體育2台 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta2.png'),
        ('elta2_backup', '[TW-I] 67 愛爾達體育2台|備 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta2.png'),
        ('elta2_720p', '[TW-I] 67 愛爾達體育2台 (720p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta2.png'),
        ('elta2_live', '[TW-I] 67 愛爾達體育2台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta2.png'),
        ('elta3_1080p', '[TW-I] 68 愛爾達體育3台 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta3.png'),
        ('elta3_backup', '[TW-I] 68 愛爾達體育3台|備 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta3.png'),
        ('elta3_720p', '[TW-I] 68 愛爾達體育3台 (720p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta3.png'),
        ('elta3_live', '[TW-I] 68 愛爾達體育3台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta3.png'),
        ('elta4', '[TW-I] 69 愛爾達體育4台', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta4.png'),
        ('elta4_backup', '[TW-I] 69 愛爾達體育4台|備 (1080p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta4.png'),
        ('elta4_720p', '[TW-I] 69 愛爾達體育4台 (720p)', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta4.png'),
        ('elta4_live', '[TW-I] 69 愛爾達體育4台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta4.png'),
        ('eltamax1', '[TW-I] 70 愛爾達體育MAX1台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax2', '[TW-I] 71 愛爾達體育MAX2台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax3', '[TW-I] 72 愛爾達體育MAX3台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax4', '[TW-I] 73 愛爾達體育MAX4台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax5', '[TW-I] 544 愛爾達體育MAX5台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax6', '[TW-I] 545 愛爾達體育MAX6台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax7', '[TW-I] 546 愛爾達體育MAX7台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax8', '[TW-I] 547 愛爾達體育MAX8台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax9', '[TW-I] 548 愛爾達體育MAX9台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('eltamax10', '[TW-I] 549 愛爾達體育MAX10台|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/elta.png'),
        ('bein1', '[NowTV] 638 beIN SPORTS 1', 'https://raw.githubusercontent.com/fanming/tv/main/logo/bein1.png'),
        ('bein1_live', '[NowTV] 638 beIN SPORTS 1|比賽時開放', 'https://raw.githubusercontent.com/fanming/tv/main/logo/bein1.png'),
        ('bein2', '[NowTV] 639 beIN SPORTS 2', 'https://raw.githubusercontent.com/fanming/tv/main/logo/bein2.png')
    ]
    
    for ch_id, ch_name, logo_url in channels:
        channel = ET.SubElement(tv, 'channel', id=ch_id)
        display_name = ET.SubElement(channel, 'display-name')
        display_name.text = ch_name
        icon = ET.SubElement(channel, 'icon', src=logo_url)

    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)

    for ch_id, ch_name, _ in channels:
        for i in range(12):
            p_start = start_time + timedelta(hours=2*i)
            p_end = p_start + timedelta(hours=2)
            
            start_str = p_start.strftime('%Y%m%d%H%M%S +0800')
            end_str = p_end.strftime('%Y%m%d%H%M%S +0800')
            
            programme = ET.SubElement(tv, 'programme', start=start_str, stop=end_str, channel=ch_id)
            title = ET.SubElement(programme, 'title', lang='zh')
            title.text = f"{ch_name.split(']')[-1].strip()} - 精彩節目"

    tree = ET.ElementTree(tv)
    ET.indent(tree, space="  ", level=0)
    tree.write('epg.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    generate_epg()
