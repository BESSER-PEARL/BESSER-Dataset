





import java.util.List;
import java.util.ArrayList;

public class se_roomManager_Room extends IRoom {

    private float extraCostPrice;
    private boolean occupied;
    private int roomNumber;
    private String extraCostDescriptions;
    private boolean blocked;





    private roomManager_IRoomType roommanager_iroomtype;


    public se_roomManager_Room(
        float extraCostPrice,        boolean occupied,        int roomNumber,        String extraCostDescriptions,        boolean blocked    ) {
        super(
        );
        this.extraCostPrice = extraCostPrice;
        this.occupied = occupied;
        this.roomNumber = roomNumber;
        this.extraCostDescriptions = extraCostDescriptions;
        this.blocked = blocked;
    }


    public float getExtracostprice() {
        return extraCostPrice;
    }

    public void setExtracostprice(float extraCostPrice) {
        this.extraCostPrice = extraCostPrice;
    }
    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }
    public int getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getExtracostdescriptions() {
        return extraCostDescriptions;
    }

    public void setExtracostdescriptions(String extraCostDescriptions) {
        this.extraCostDescriptions = extraCostDescriptions;
    }
    public boolean getBlocked() {
        return blocked;
    }

    public void setBlocked(boolean blocked) {
        this.blocked = blocked;
    }

    public roomManager_IRoomType getRoommanager_iroomtype() {
        return roommanager_iroomtype;
    }

    public void setRoommanager_iroomtype(roomManager_IRoomType roommanager_iroomtype) {
        this.roommanager_iroomtype = roommanager_iroomtype;
    }

}