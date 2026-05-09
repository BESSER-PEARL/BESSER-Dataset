





import java.util.List;
import java.util.ArrayList;

public class newClasses_Room extends RoomType {

    private String status;
    private String roomNum;





    private newClasses_RoomHandler newclasses_roomhandler;


    public newClasses_Room(
        String status,        String roomNum    ) {
        super(
        );
        this.status = status;
        this.roomNum = roomNum;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getRoomnum() {
        return roomNum;
    }

    public void setRoomnum(String roomNum) {
        this.roomNum = roomNum;
    }

    public newClasses_RoomHandler getNewclasses_roomhandler() {
        return newclasses_roomhandler;
    }

    public void setNewclasses_roomhandler(newClasses_RoomHandler newclasses_roomhandler) {
        this.newclasses_roomhandler = newclasses_roomhandler;
    }

}