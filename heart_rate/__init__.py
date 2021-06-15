from .calculate import calculate
from dataclasses import dataclass, field


@dataclass
class HeartRate:   
    __avg: int = field(default_factory=int)
    __min: int = field(default_factory=int)
    __max: int = field(default_factory=int)
    
    def __calculate(self, video):
        heart_rate = calculate(video)
        self.__avg = heart_rate.get_avg()
        self.__min = heart_rate.get_min()
        self.__max = heart_rate.get_max()
    
    def __check_video(self, video) -> bool:
        pass
    
    def check_compatibility(self, video) -> bool:
        if self.__check_video(video):
            return True
        # return a list of supported formats
        return False
    
    def add_video(self, video) -> None:
        if self.__check_video(video):
            self.__calculate(video)
        else:
            # raise exception
            pass
        
    def get_avg(self) -> int:
        if self.__avg == -1:
            # raise exception
            pass
        return self.__avg
    
    def get_min(self) -> int:
        if self.__min == -1:
            # raise exception
            pass
        return self.__min
    
    def get_max(self) -> int:
        if self.__max == -1:
            # raise exception
            pass
        return self.__max
    
    def get_all(self) -> dict:
        values = {
            'average': self.get_avg(),
            'minimum': self.get_min(),
            'maximum': self.get_max()
        }
        return values
    
    