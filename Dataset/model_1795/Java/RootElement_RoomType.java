





import java.util.List;
import java.util.ArrayList;

public class RootElement_RoomType  {

    private String price;
    private String capacity;
    private String name;





    private RootElement_Room rootelement_room;


    public RootElement_RoomType(
        String price,        String capacity,        String name    ) {
        this.price = price;
        this.capacity = capacity;
        this.name = name;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RootElement_Room getRootelement_room() {
        return rootelement_room;
    }

    public void setRootelement_room(RootElement_Room rootelement_room) {
        this.rootelement_room = rootelement_room;
    }

}