from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client["ytmanager"]
video_collection = db["videos"]

print("Connected to MongoDB successfully")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def update_video(video_id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": name, "time": time}}
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all Youtube videos")
        print("2. Add a youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice = input("Please enter your choice: ")

        if choice == '1':
            list_all_videos()

        elif choice == '2':
            name = input("Please enter video name: ")
            time = input("Please enter video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Please enter video ID: ")
            name = input("Please enter new name: ")
            time = input("Please enter new time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Please enter video ID: ")
            delete_video(video_id)

        elif choice == '5':
            print("Exiting app...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()