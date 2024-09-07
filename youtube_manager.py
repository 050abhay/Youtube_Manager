import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:  
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  
        return []

def save_data_helper(videos, filename):
    with open(filename, 'w') as file:  
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}, {video['video_link']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    video_link = input("Enter the link of videos: ")
    videos.append({'name': name, 'time': time, 'video_link': video_link})
    save_data_helper(videos, 'youtube.txt')

def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: "))  
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        video_link = input("Enter the link of videos: ")
        videos[index-1] = {'name': name, 'time': time, 'video_link': video_link}
        save_data_helper(videos, 'youtube.txt')
    else:
        print("Invalid index selected !")

def delete_video(videos, deleted_video):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to be deleted: "))  
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if 1 <= index <= len(videos):
        video = videos[index-1]
        deleted_video.append({'name': video['name'], 'time': video['time'], 'video_link': video['video_link']})
        save_data_helper(deleted_video, 'deleted_detail.txt')

        print("\nDeleted video is-\n")
        print(f"Name: {video['name']}, Duration: {video['time']}, Link: {video['video_link']}")
        del videos[index-1]
        save_data_helper(videos, 'youtube.txt')
        print("\nAfter deletion of the video detail.")
        list_all_videos(videos)
    else:
        print("Invalid video index selected !")

def main():
    videos = load_data('youtube.txt')
    deleted_video = load_data('deleted_detail.txt')
    while True:
        print("\nYoutube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. List all deleted youtube video ")
        print("6. Exit the app ")
        choice = input("Enter your choice: ")
        

        match choice:  
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos, deleted_video)
            case '5':
                list_all_videos(deleted_video)
            case '6':
                break
            case _:
                print("Invalid Choice !!!!")

if __name__ == "__main__":
    main()
