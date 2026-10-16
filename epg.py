import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def generate_epg():
    tv = ET.Element('tv', generator_info_name='MyEPG-VL-DAZN')
    
    # (標準ID, 主要名稱, M3U8所有可能的名稱別名, Logo網址)
    target_channels = [
        # --- 緯來系列 ---
        (
            'VideolandSports.tw',
            '緯來體育台',
            ['[TW-I] 22 緯來體育台', '[TW-I] 22 緯來體育台 (a)', '[TW-I] 22 緯來體育台 (b)', '[TW-I] 22 緯來體育台 (c)', '緯來體育台', '緯來體育'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_sports.png'
        ),
        (
            'VideolandVariety.tw',
            '緯來綜合台',
            ['[TW-I] 25 緯來綜合台', '[TW-I] 25 緯來綜合台 (a)', '[TW-I] 25 緯來綜合台 (b)', '緯來綜合台', '緯來綜合'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_variety.png'
        ),
        (
            'VideolandJapan.tw',
            '緯來日本台',
            ['[TW-I] 27 緯來日本台', '[TW-I] 27 緯來日本台 (a)', '[TW-I] 27 緯來日本台 (b)', '緯來日本台', '緯來日本'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_japan.png'
        ),
        (
            'VideolandDrama.tw',
            '緯來戲劇台',
            ['[TW-I] 26 緯來戲劇台', '[TW-I] 26 緯來戲劇台 (a)', '[TW-I] 26 緯來戲劇台 (b)', '[TW-I] 26 緯來戲劇台 (c)', '緯來戲劇台', '緯來戲劇'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_drama.png'
        ),
        (
            'VideolandMovie.tw',
            '緯來電影台',
            ['[TW-I] 28 緯來電影台', '[TW-I] 28 緯來電影台 (a)', '[TW-I] 28 緯來電影台 (b)', '緯來電影台', '緯來電影'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_movie.png'
        ),
        (
            'VideolandFlash.tw',
            '緯來精采',
            ['[TW-I] 138 緯來精采', '緯來精采', '緯來精彩台'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/videoland_hd.png'
        ),

        # --- DAZN 系列 ---
        (
            'DAZN1.tw',
            'DAZN 1',
            ['[TW-I] 64 DAZN 1', '[TW-I] 64 DAZN 1 (a)', '[TW-I] 64 DAZN 1 (b)', 'DAZN 1', 'DAZN1'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn1.png'
        ),
        (
            'DAZN2.tw',
            'DAZN 2',
            ['[TW-I] 65 DAZN 2', '[TW-I] 65 DAZN 2 (a)', '[TW-I] 65 DAZN 2 (b)', '[TW-I] 65 DAZN 2 (c)', 'DAZN 2', 'DAZN2'],
            'https://raw.githubusercontent.com/fanming/tv/main/logo/dazn2.png'
        )
    ]
    
    # 建立 XML 頻道資料
    for ch_id, main_name, aliases, logo_url in target_channels:
        channel = ET.SubElement(tv, 'channel', id=ch_id)
        
        # 主顯示名稱
        dn_main = ET.SubElement(channel, 'display-name')
        dn_main.text = main_name
        
        # 寫入所有 M3U8 可能對應到的別名
        for alias in aliases:
            dn = ET.SubElement(channel, 'display-name')
            dn.text = alias
            
        # 寫入 Logo 連結
        ET.SubElement(channel, 'icon', src=logo_url)

    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)

    # 產生 24 小時時段節目
    for ch_id, main_name, _, _ in target_channels:
        for i in range(12):
            p_start = start_time + timedelta(hours=2*i)
            p_end = p_start + timedelta(hours=2)
            
            start_str = p_start.strftime('%Y%m%d%H%M%S +0800')
            end_str = p_end.strftime('%Y%m%d%H%M%S +0800')
            
            programme = ET.SubElement(tv, 'programme', start=start_str, stop=end_str, channel=ch_id)
            title = ET.SubElement(programme, 'title', lang='zh')
            title.text = f"{main_name} - 精彩節目"

    tree = ET.ElementTree(tv)
    ET.indent(tree, space="  ", level=0)
    tree.write('epg.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    generate_epg()
