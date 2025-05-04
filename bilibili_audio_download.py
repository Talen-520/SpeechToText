import requests
import json
import re
from urllib.parse import unquote

# bilibili音频下载脚本

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.bilibili.com/"
}

def get_bilibili_audio(bvid):
    try:
        # 1. 获取视频基本信息（包含cid）
        info_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        response = requests.get(info_url, headers=headers)
        response.raise_for_status()
        data = json.loads(response.text)
        
        if data.get('code') != 0:
            raise Exception(f"API错误: {data.get('message')}")
        
        cid = data['data']['cid']
        title = data['data']['title']
        print(f"获取视频信息成功: {title} (CID: {cid})")

        # 2. 获取播放地址信息
        play_url = f"https://api.bilibili.com/x/player/playurl?cid={cid}&bvid={bvid}&qn=0&fnver=0&fnval=16&otype=json"
        play_response = requests.get(play_url, headers=headers)
        play_response.raise_for_status()
        play_data = json.loads(play_response.text)
        
        if play_data.get('code') != 0:
            raise Exception(f"获取播放地址失败: {play_data.get('message')}")

        # 3. 提取音频URL（从dash音频流中获取）
        if 'dash' in play_data['data']:
            audio_url = play_data['data']['dash']['audio'][0]['base_url']
            print(f"获取到音频URL: {audio_url[:60]}...")  # 只打印前60个字符避免太长
            
            # 4. 下载音频
            audio_response = requests.get(audio_url, headers=headers, stream=True)
            audio_response.raise_for_status()
            
            # 清理文件名中的非法字符
            safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
            filename = f"{safe_title}.m4a"
            
            with open(filename, "wb") as f:
                for chunk in audio_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            
            print(f"音频下载完成: {filename}")
            return filename
        else:
            raise Exception("无法获取DASH格式的音频流，可能是视频不支持")
            
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None

# 使用示例
bvid = "BV15ZVjzREyE"  # 替换为你想下载的视频BV号
get_bilibili_audio(bvid)