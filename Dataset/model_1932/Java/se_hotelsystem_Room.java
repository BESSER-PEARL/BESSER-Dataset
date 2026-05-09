





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_Room  {

    private int roomNumber;
    private boolean blocked;
    private boolean occupied;





    private hotelsystem_RoomType hotelsystem_roomtype;


    public se_hotelsystem_Room(
        int roomNumber,        boolean blocked,        boolean occupied    ) {
        this.roomNumber = roomNumber;
        this.blocked = blocked;
        this.occupied = occupied;
    }


    public int getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }
    public boolean getBlocked() {
        return blocked;
    }

    public void setBlocked(boolean blocked) {
        this.blocked = blocked;
    }
    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }

    public hotelsystem_RoomType getHotelsystem_roomtype() {
        return hotelsystem_roomtype;
    }

    public void setHotelsystem_roomtype(hotelsystem_RoomType hotelsystem_roomtype) {
        this.hotelsystem_roomtype = hotelsystem_roomtype;
    }

}