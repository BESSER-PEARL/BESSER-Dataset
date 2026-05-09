





import java.util.List;
import java.util.ArrayList;

public class Implementation_RoomComponent_Room  {

    private String roomNumber;
    private String price;
    private String usable;
    private String roomTypeName;
    private String description;



    public Implementation_RoomComponent_Room(
        String roomNumber,        String price,        String usable,        String roomTypeName,        String description    ) {
        this.roomNumber = roomNumber;
        this.price = price;
        this.usable = usable;
        this.roomTypeName = roomTypeName;
        this.description = description;
    }


    public String getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getUsable() {
        return usable;
    }

    public void setUsable(String usable) {
        this.usable = usable;
    }
    public String getRoomtypename() {
        return roomTypeName;
    }

    public void setRoomtypename(String roomTypeName) {
        this.roomTypeName = roomTypeName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}