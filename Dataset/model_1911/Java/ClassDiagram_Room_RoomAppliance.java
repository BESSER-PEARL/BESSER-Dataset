





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Room_RoomAppliance  {

    private String name;





    private ClassDiagram_Room_RoomType classdiagram_room_roomtype;




    private ClassDiagram_Hotel_Room classdiagram_hotel_room;




    private ClassDiagram_RoomAppliance_ApplianceType classdiagram_roomappliance_appliancetype;


    public ClassDiagram_Room_RoomAppliance(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Room_RoomType getClassdiagram_room_roomtype() {
        return classdiagram_room_roomtype;
    }

    public void setClassdiagram_room_roomtype(ClassDiagram_Room_RoomType classdiagram_room_roomtype) {
        this.classdiagram_room_roomtype = classdiagram_room_roomtype;
    }
    public ClassDiagram_Hotel_Room getClassdiagram_hotel_room() {
        return classdiagram_hotel_room;
    }

    public void setClassdiagram_hotel_room(ClassDiagram_Hotel_Room classdiagram_hotel_room) {
        this.classdiagram_hotel_room = classdiagram_hotel_room;
    }
    public ClassDiagram_RoomAppliance_ApplianceType getClassdiagram_roomappliance_appliancetype() {
        return classdiagram_roomappliance_appliancetype;
    }

    public void setClassdiagram_roomappliance_appliancetype(ClassDiagram_RoomAppliance_ApplianceType classdiagram_roomappliance_appliancetype) {
        this.classdiagram_roomappliance_appliancetype = classdiagram_roomappliance_appliancetype;
    }

}