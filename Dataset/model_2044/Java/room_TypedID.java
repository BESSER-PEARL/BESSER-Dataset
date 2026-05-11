





import java.util.List;
import java.util.ArrayList;

public class room_TypedID  {

    private String name;





    private room_Message room_message;


    public room_TypedID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_Message getRoom_message() {
        return room_message;
    }

    public void setRoom_message(room_Message room_message) {
        this.room_message = room_message;
    }

}