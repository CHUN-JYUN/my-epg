import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def generate_epg():
    tv = ET.Element('tv', generator_info_name='MyEPG')
    
    channels = [
        ('videoland_sports', '緯來體育台'),
        ('elta_sports1', '愛爾達體育1台'),
        ('dazn1', 'DAZN 1')
    ]
    
    for ch_id, ch_name in channels:
        channel = ET.SubElement(tv, 'channel', id=ch_id)
        display_name = ET.SubElement(channel, 'display-name')
        display_name.text = ch_name

    now = datetime.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)

    for ch_id, ch_name in channels:
        for i in range(12):
            p_start = start_time + timedelta(hours=2*i)
            p_end = p_start + timedelta(hours=2)
            
            start_str = p_start.strftime('%Y%m%d%H%M%S +0800')
            end_str = p_end.strftime('%Y%m%d%H%M%S +0800')
            
            programme = ET.SubElement(tv, 'programme', start=start_str, stop=end_str, channel=ch_id)
            title = ET.SubElement(programme, 'title', lang='zh')
            title.text = f"{ch_name} 精彩節目"

    tree = ET.ElementTree(tv)
    ET.indent(tree, space="  ", level=0)
    tree.write('epg.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    generate_epg()
