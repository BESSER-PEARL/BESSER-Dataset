





import java.util.List;
import java.util.ArrayList;

public class room_RoomClass  {

    private String name;





    private room_Documentation room_documentation;


    public room_RoomClass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }

}