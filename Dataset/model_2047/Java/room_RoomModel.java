





import java.util.List;
import java.util.ArrayList;

public class room_RoomModel  {

    private String name;





    private List<room_LogicalSystem> room_logicalsystems;


    public room_RoomModel(
        String name    ) {
        this.name = name;
        this.room_logicalsystems = new ArrayList<>();
    }

    public room_RoomModel(
        String name        ArrayList<room_LogicalSystem> room_logicalsystems    ) {
        this.name = name;
        this.room_logicalsystems = room_logicalsystems;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<room_LogicalSystem> getRoom_logicalsystems() {
        return room_logicalsystems;
    }

    public void addRoom_logicalsystem(Room_logicalsystem room_logicalsystem) {
        this.room_logicalsystems.add(room_logicalsystem);
    }

}