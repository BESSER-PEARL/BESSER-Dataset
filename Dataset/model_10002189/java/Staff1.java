





import java.util.List;
import java.util.ArrayList;

public class Staff1  {






    private List<Room> rooms;


    public Staff1(
    ) {
        this.rooms = new ArrayList<>();
    }

    public Staff1(
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