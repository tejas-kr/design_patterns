from abc import ABC, abstractmethod
from os import PathLike

# We need to design a system which changes the resolution of the video according to dimentions passed
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
    

class ConvertVideos:
    """ConvertVideos
    """

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


if __name__ == "__main__":
    video = "Pokemon ep 1"
    resolution720 = "720p"
    resolution1080 = "1080p"

    con_vid_720 = ConvertVideos(video=video, resolution=resolution720)
    print("720p video: ", con_vid_720.convert_video())
    
    con_vid_1080 = ConvertVideos(video=video, resolution=resolution1080)
    print("1080p video: ", con_vid_1080.convert_video())