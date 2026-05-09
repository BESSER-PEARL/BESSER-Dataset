





import java.util.List;
import java.util.ArrayList;

public class tda593_facilities_RoomType  {

    private float price;
    private String roomApprovals;
    private String description;
    private String name;



    public tda593_facilities_RoomType(
        float price,        String roomApprovals,        String description,        String name    ) {
        this.price = price;
        this.roomApprovals = roomApprovals;
        this.description = description;
        this.name = name;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getRoomapprovals() {
        return roomApprovals;
    }

    public void setRoomapprovals(String roomApprovals) {
        this.roomApprovals = roomApprovals;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}