from abc import ABC, abstractmethod
from os import PathLike

# We will extend the example of factory pattern, we now need to convert videos based on laptop models. 
# As an example we have two models say, Lenovo and HP and we add a new resolution - 1440p
# Lenovo require 720p and 1080p 
# HP requires 720p and 1440p

class Resolution(ABC):
    """Converts Video in the specified Resolution
    """

    @abstractmethod
    def convert(self, video: str, resolution: str) -> str:
        """converts video to the specified resolution

        Args:
            video (str): _description_
            resolution (str): _description_
        """
        ...

    
class Resolution720p(Resolution):
    """Resolution720p
    """

    def __init__(self) -> None:
        super().__init__()

    def convert(self, video: str, resolution: str) -> str:
        """convert
        Converts the video to 720p Resolution

        Args:
            video (str): _description_
            resolution (str): _description_

        Returns:
            Converted video path
        """
        return "Video has been converted to 720p"


class Resolution1080p(Resolution):
    """Resolution1080p
    """

    def __init__(self) -> None:
        super().__init__()

    def convert(self, video: str, resolution: str) -> str:
        """convert
        Converts the video to 1080p Resolution

        Args:
            video (str): _description_
            resolution (str): _description_

        Returns:
            Converted video path
        """
        return "Video has been converted to 1080p"


class Resolution1440p(Resolution):
    """Resolution1440p
    """

    def __init__(self) -> None:
        super().__init__()

    def convert(self, video: str, resolution: str) -> str:
        """convert
        Converts the video to 1440p Resolution

        Args:
            video (str): _description_
            resolution (str): _description_

        Returns:
            Converted video path
        """
        return "Video has been converted to 1440p"
    

class Laptop(ABC):
    """Laptop
    Abstract class for laptop
    """

    @abstractmethod
    def convert_video(self) -> str:
        ...


class LenovoLaptop(Laptop):

    def __init__(self, video: str, resolution: str) -> None:
        self.video = video
        self.resolution = resolution
        self.resolution_converter: Resolution

    def convert_video(self) -> str:
        """convert_video
        """
        if (self.resolution).lower() == "720p":
            self.resolution_converter = Resolution720p()
        elif (self.resolution).lower() == "1440p":
            self.resolution_converter = Resolution1440p()

        return self.resolution_converter.convert(video=self.video, resolution=self.resolution)


class HPLaptop(Laptop):

    def __init__(self, video: str, resolution: str) -> None:
        self.video = video
        self.resolution = resolution
        self.resolution_converter: Resolution

    def convert_video(self) -> str:
        """convert_video
        """
        if (self.resolution).lower() == "720p": 
            self.resolution_converter = Resolution720p()
        elif (self.resolution).lower() == "1080p":
            self.resolution_converter = Resolution1080p()

        return self.resolution_converter.convert(video=self.video, resolution=self.resolution)
    

class ConvertVideos:
    """ConvertVideos
    """

    def __init__(self, video: str, resolution: str, laptop_name: str) -> None:
        self.video = video
        self.resolution = resolution
        self.laptop_name = laptop_name
        self.laptop: Laptop

    def convert_video_based_on_laptop(self) -> str:
        """convert_video_based_on_laptop
        """
        if (self.laptop_name).lower() == "lenovo": 
            self.laptop = LenovoLaptop(video=self.video, resolution=self.resolution)
        elif (self.laptop_name).lower() == "hp":
            self.laptop = HPLaptop(video=self.video, resolution=self.resolution)

        return self.laptop.convert_video()


if __name__ == "__main__":
    video = "Pokemon ep 1"
    laptop1 = 'Lenovo'
    laptop2 = 'HP'

    con_vid_lenovo_720p = ConvertVideos(video=video, resolution="720p", laptop_name=laptop1)
    print("lenovo video 720p: ", con_vid_lenovo_720p.convert_video_based_on_laptop())
    
    con_vid_hp_720p = ConvertVideos(video=video, resolution="720p", laptop_name=laptop2)
    print("hp video 720p: ", con_vid_hp_720p.convert_video_based_on_laptop())
    
    con_vid_lenovo_1080p = ConvertVideos(video=video, resolution="720p", laptop_name=laptop1)
    print("lenovo video 1080p: ", con_vid_lenovo_1080p.convert_video_based_on_laptop())
    
    con_vid_hp_1440p = ConvertVideos(video=video, resolution="720p", laptop_name=laptop2)
    print("hp video 1440p: ", con_vid_hp_1440p.convert_video_based_on_laptop())
