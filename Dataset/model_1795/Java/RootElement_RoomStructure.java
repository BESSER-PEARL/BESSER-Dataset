





import java.util.List;
import java.util.ArrayList;

public class RootElement_RoomStructure extends RoomFetcher, RoomHandling, RoomTypeHandling, RoomAttributeHandling {






    private List<RootElement_RoomType> rootelement_roomtypes;




    private List<RootElement_Room> rootelement_rooms;




    private List<RootElement_RoomAttribute> rootelement_roomattributes;


    public RootElement_RoomStructure(
    ) {
        super(
        );
        this.rootelement_roomtypes = new ArrayList<>();
        this.rootelement_rooms = new ArrayList<>();
        this.rootelement_roomattributes = new ArrayList<>();
    }

    public RootElement_RoomStructure(
        ArrayList<RootElement_RoomType> rootelement_roomtypes,        ArrayList<RootElement_Room> rootelement_rooms,        ArrayList<RootElement_RoomAttribute> rootelement_roomattributes    ) {
        this.rootelement_roomtypes = rootelement_roomtypes;
        this.rootelement_rooms = rootelement_rooms;
        this.rootelement_roomattributes = rootelement_roomattributes;
    }


    public List<RootElement_RoomType> getRootelement_roomtypes() {
        return rootelement_roomtypes;
    }

    public void addRootelement_roomtype(Rootelement_roomtype rootelement_roomtype) {
        this.rootelement_roomtypes.add(rootelement_roomtype);
    }
    public List<RootElement_Room> getRootelement_rooms() {
        return rootelement_rooms;
    }

    public void addRootelement_room(Rootelement_room rootelement_room) {
        this.rootelement_rooms.add(rootelement_room);
    }
    public List<RootElement_RoomAttribute> getRootelement_roomattributes() {
        return rootelement_roomattributes;
    }

    public void addRootelement_roomattribute(Rootelement_roomattribute rootelement_roomattribute) {
        this.rootelement_roomattributes.add(rootelement_roomattribute);
    }

}