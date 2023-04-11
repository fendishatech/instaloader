import instaloader
import time


class InstagramScraper:
    """
    By taking a Public instagram accounts username, this class gets
    basic info and posts, it also can downloads posts.
    """
    def __init__(self, username):
        self.username = username
        self.loader = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.loader.context, self.username)

    def getProfile(self):
        if self.profile:
            return self.profile
        return None
    
    def getProfilePicture(self):
        current_time = time.time()
        if self.profile:
            self.loader.download_pic(self.username, self.profile.profile_pic_url,(current_time,current_time))

    def getPosts (self):
        # get posts logic
        return self.profile.followers

    def getPics(self):
        pass

    def getVids(self):
        pass

def main ():
    s = InstagramScraper("the_roamingchef")
    s.getProfilePicture()
    print(f"Full Name {s.profile.full_name}")
    print(f"Biography {s.profile.biography}")
    print(f"Followers {s.profile.followers}")
    print(f"Followees {s.profile.followees}")
    print("Done.")

if __name__ == "__main__":
    main()