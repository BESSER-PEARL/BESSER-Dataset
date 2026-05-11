





import java.util.List;
import java.util.ArrayList;

public class company106_Room extends Function {






    private List<company106_Room> company106_rooms;


    public company106_Room(
    ) {
        super(
        );
        this.company106_rooms = new ArrayList<>();
    }

    public company106_Room(
        ArrayList<company106_Room> company106_rooms    ) {
        this.company106_rooms = company106_rooms;
    }


    public List<company106_Room> getCompany106_rooms() {
        return company106_rooms;
    }

    public void addCompany106_room(Company106_room company106_room) {
        this.company106_rooms.add(company106_room);
    }

}