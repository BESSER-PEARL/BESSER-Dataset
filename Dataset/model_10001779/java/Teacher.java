





import java.util.List;
import java.util.ArrayList;

public class Teacher  {

    private String Name;





    private Room room;


    public Teacher(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

}