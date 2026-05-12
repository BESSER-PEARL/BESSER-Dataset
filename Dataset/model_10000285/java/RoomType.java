





import java.util.List;
import java.util.ArrayList;

public class RoomType  {

    private String name;
    private String pricePerNight;





    private List<Room> rooms;


    public RoomType(
        String name,        String pricePerNight    ) {
        this.name = name;
        this.pricePerNight = pricePerNight;
        this.rooms = new ArrayList<>();
    }

    public RoomType(
        String name,        String pricePerNight        ArrayList<Room> rooms    ) {
        this.name = name;
        this.pricePerNight = pricePerNight;
        this.rooms = rooms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPricepernight() {
        return pricePerNight;
    }

    public void setPricepernight(String pricePerNight) {
        this.pricePerNight = pricePerNight;
    }

    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

}