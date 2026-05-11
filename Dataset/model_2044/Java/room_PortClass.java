





import java.util.List;
import java.util.ArrayList;

public class room_PortClass  {






    private List<room_Operation> room_operations;




    private room_DetailCode room_detailcode;




    private room_ProtocolClass room_protocolclass;




    private List<room_Attribute> room_attributes;




    private room_ProtocolClass room_protocolclass;


    public room_PortClass(
    ) {
        this.room_operations = new ArrayList<>();
        this.room_attributes = new ArrayList<>();
    }

    public room_PortClass(
        ArrayList<room_Operation> room_operations,        ArrayList<room_Attribute> room_attributes    ) {
        this.room_operations = room_operations;
        this.room_attributes = room_attributes;
    }


    public List<room_Operation> getRoom_operations() {
        return room_operations;
    }

    public void addRoom_operation(Room_operation room_operation) {
        this.room_operations.add(room_operation);
    }
    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }
    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }
    public List<room_Attribute> getRoom_attributes() {
        return room_attributes;
    }

    public void addRoom_attribute(Room_attribute room_attribute) {
        this.room_attributes.add(room_attribute);
    }
    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }

}