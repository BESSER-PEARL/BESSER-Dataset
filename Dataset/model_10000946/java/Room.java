





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String location;
    private int roomno;



    public Room(
        String location,        int roomno    ) {
        this.location = location;
        this.roomno = roomno;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }


}