import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except:
        return []

videos = load_data()

def save_helper():
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos():
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['video_name']} \n Duration: {video['video_duration']}")


def upload_video():
    name = input("Enter name of video: ")
    duration = input("Enter duration of video: ")
    videos.append({
        "video_name": name,
        "video_duration": duration
    })
    save_helper()

def update_video(videoName):
    try:
        for video in videos:
            if video['video_name'] == videoName:
                while True:
                    print("\n What do you want to edit?")
                    print("1. Video name")
                    print("2. Video duration")
                    print("3. Save and exit")
                    choice = input("Enter your choice: ")
                    match choice:
                        case "1":
                            new_name = input("Enter new video name: ")
                            video['video_name'] = new_name
                        case "2":
                            new_duration = input("Enter new video duration: ")
                            video['video_duration'] = new_duration
                        case "3":
                            break
                        case _:
                            print("Invalid choice")
        save_helper()
    except:
        print(f"Video with name '{videoName}' does not exist.")
                

def delete_video(video_name):
    try: 
        for video in videos:
            if video['video_name'] == video_name:
                videos.pop(videos.index(video))
        save_helper()
    except:
        print(f"Video with name '{videoName}' does not exist.")
        


def main():
    print("\n Welcome to Youtube Manager App \n Choose an option")
    while True:
        print("\n 1. List all youtube videos")
        print("2. Upload a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtuve video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                upload_video()
            case "3":
                video_name = input("Name of video to be edited: ")
                update_video(video_name)
            case "4":
                video_name = input("Name of video to be deleted: ")
                delete_video(video_name)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()