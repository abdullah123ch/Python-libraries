import pywhatkit
# PyWhatkit is a versatile Python library designed for automating WhatsApp messaging and other tasks.

1. #WhatsApp Automation:**
   # - Effortlessly sending WhatsApp messages to individual contacts or groups, streamlining communication processes.
   # - Implementing sophisticated message scheduling, allowing users to set specific times for message delivery.
    
#pywhatkit.sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3)
    
#pywhatkit.sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) 
    
#pywhatkit.sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 15, tab_close: bool = False, close_time: int = 3)
    
   # - Facilitating the seamless transmission of multimedia content, including images and videos, enhancing the richness of communication.
    

#pywhatkit.sendwhats_image(receiver: str, img_path: str, caption: str = "", wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None
    