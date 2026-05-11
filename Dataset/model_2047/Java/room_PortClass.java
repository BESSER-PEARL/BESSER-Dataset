





import java.util.List;
import java.util.ArrayList;

public class room_PortClass  {






    private List<room_Attribute> room_attributes;




    private room_DetailCode room_detailcode;


    public room_PortClass(
    ) {
        this.room_attributes = new ArrayList<>();
    }

    public room_PortClass(
        ArrayList<room_Attribute> room_attributes    ) {
        this.room_attributes = room_attributes;
    }


    public List<room_Attribute> getRoom_attributes() {
        return room_attributes;
    }

    public void addRoom_attribute(Room_attribute room_attribute) {
        this.room_attributes.add(room_attribute);
    }
    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }

}