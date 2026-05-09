





import java.util.List;
import java.util.ArrayList;

public class Classes_IBookingManagementImpl extends IBookingManagement {






    private Classes_Room classes_room;




    private List<Classes_Room> classes_rooms;


    public Classes_IBookingManagementImpl(
    ) {
        super(
        );
        this.classes_rooms = new ArrayList<>();
    }

    public Classes_IBookingManagementImpl(
        ArrayList<Classes_Room> classes_rooms    ) {
        this.classes_rooms = classes_rooms;
    }


    public Classes_Room getClasses_room() {
        return classes_room;
    }

    public void setClasses_room(Classes_Room classes_room) {
        this.classes_room = classes_room;
    }
    public List<Classes_Room> getClasses_rooms() {
        return classes_rooms;
    }

    public void addClasses_room(Classes_room classes_room) {
        this.classes_rooms.add(classes_room);
    }

}