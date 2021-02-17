import pyautogui, pafy, time, os, requests

from setup import browser_location, youtube_api_key, link

link_length = len(link)

if link_length == 68:
    print('Processing, Please Wait...')
    link_detector = link[34:68]
    videos = requests.get(f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=50&playlistId={link_detector}&key={youtube_api_key}')
    videolist = videos.json()
    videolistarray = videolist['items']
    first_video = videolistarray[0]['contentDetails']['videoId']

    total_video_length = 0
    for video in videolistarray:
        x = (video['contentDetails']['videoId'])
        video = pafy.new(x)
        video_length = video.length
        total_video_length += video_length

    os.system(f"open {browser_location}")

    time.sleep(10)

    pyautogui.write(f'https://www.youtube.com/watch?v={first_video}&list={link_detector}')
    pyautogui.press('enter')

    print('done')

elif link_length == 43:
    link_detector = link[32:43]
    video = pafy.new(link_detector)
    video_length = video.length

    os.system(f"open {browser_location}")

    time.sleep(10)

    pyautogui.write(link)
    pyautogui.press('enter')

    time.sleep(15)

    pyautogui.hotkey('shift', 'command', '3')

    time.sleep(video_length)

    pyautogui.hotkey('shift', 'command', '3')
