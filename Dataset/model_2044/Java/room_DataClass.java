





import java.util.List;
import java.util.ArrayList;

public class room_DataClass extends RoomClass {






    private room_RoomModel room_roommodel;




    private room_DataClass room_dataclass;




    private List<room_Import> room_imports;


    public room_DataClass(
    ) {
        super(
        );
        this.room_imports = new ArrayList<>();
    }

    public room_DataClass(
        ArrayList<room_Import> room_imports    ) {
        this.room_imports = room_imports;
    }


    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }
    public List<room_Import> getRoom_imports() {
        return room_imports;
    }

    public void addRoom_import(Room_import room_import) {
        this.room_imports.add(room_import);
    }

}