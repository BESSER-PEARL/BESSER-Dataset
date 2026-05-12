





import java.util.List;
import java.util.ArrayList;

public class Staff  {






    private List<Room> rooms;


    public Staff(
    ) {
        this.rooms = new ArrayList<>();
    }

    public Staff(
        ArrayList<Room> rooms    ) {
        this.rooms = rooms;
    }


    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

}