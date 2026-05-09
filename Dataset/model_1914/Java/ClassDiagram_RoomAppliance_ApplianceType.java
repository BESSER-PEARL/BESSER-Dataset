





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_RoomAppliance_ApplianceType  {

    private String name;





    private ClassDiagram_Room_RoomType classdiagram_room_roomtype;


    public ClassDiagram_RoomAppliance_ApplianceType(
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

}