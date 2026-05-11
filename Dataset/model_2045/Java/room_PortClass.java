





import java.util.List;
import java.util.ArrayList;

public class room_PortClass  {






    private room_ProtocolClass room_protocolclass;




    private List<room_Attribute> room_attributes;




    private room_ProtocolClass room_protocolclass;




    private List<room_PortOperation> room_portoperations;




    private room_DetailCode room_detailcode;


    public room_PortClass(
    ) {
        this.room_attributes = new ArrayList<>();
        this.room_portoperations = new ArrayList<>();
    }

    public room_PortClass(
        ArrayList<room_Attribute> room_attributes,        ArrayList<room_PortOperation> room_portoperations    ) {
        this.room_attributes = room_attributes;
        this.room_portoperations = room_portoperations;
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
    public List<room_PortOperation> getRoom_portoperations() {
        return room_portoperations;
    }

    public void addRoom_portoperation(Room_portoperation room_portoperation) {
        this.room_portoperations.add(room_portoperation);
    }
    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }

}