





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Name;
    private int ID;
    private String Type;





    private List<Rooms> roomss;


    public Staff(
        String Name,        int ID,        String Type    ) {
        this.Name = Name;
        this.ID = ID;
        this.Type = Type;
        this.roomss = new ArrayList<>();
    }

    public Staff(
        String Name,        int ID,        String Type        ArrayList<Rooms> roomss    ) {
        this.Name = Name;
        this.ID = ID;
        this.Type = Type;
        this.roomss = roomss;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public List<Rooms> getRoomss() {
        return roomss;
    }

    public void addRooms(Rooms rooms) {
        this.roomss.add(rooms);
    }

}