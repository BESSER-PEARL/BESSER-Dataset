





import java.util.List;
import java.util.ArrayList;

public class Classes_Room  {

    private String roomNumber;
    private String status;



    public Classes_Room(
        String roomNumber,        String status    ) {
        this.roomNumber = roomNumber;
        this.status = status;
    }


    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}