





import java.util.List;
import java.util.ArrayList;

public class RoomType  {

    private String pricePerNight;
    private String name;





    private List<Room> rooms;


    public RoomType(
        String pricePerNight,        String name    ) {
        this.pricePerNight = pricePerNight;
        this.name = name;
        this.rooms = new ArrayList<>();
    }

    public RoomType(
        String pricePerNight,        String name        ArrayList<Room> rooms    ) {
        this.pricePerNight = pricePerNight;
        this.name = name;
        this.rooms = rooms;
    }

    public String getPricepernight() {
        return pricePerNight;
    }

    public void setPricepernight(String pricePerNight) {
        this.pricePerNight = pricePerNight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

}