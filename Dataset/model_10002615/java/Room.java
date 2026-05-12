





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int roomno;
    private String roomname;



    public Room(
        int roomno,        String roomname    ) {
        this.roomno = roomno;
        this.roomname = roomname;
    }


    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getRoomname() {
        return roomname;
    }

    public void setRoomname(String roomname) {
        this.roomname = roomname;
    }


}