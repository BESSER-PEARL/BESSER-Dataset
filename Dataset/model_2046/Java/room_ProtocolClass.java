





import java.util.List;
import java.util.ArrayList;

public class room_ProtocolClass extends GeneralProtocolClass {

    private String commType;





    private room_DetailCode room_detailcode;




    private room_ProtocolClass room_protocolclass;




    private room_PortClass room_portclass;




    private room_PortClass room_portclass;




    private room_ProtocolSemantics room_protocolsemantics;




    private room_DetailCode room_detailcode;




    private List<room_Message> room_messages;




    private List<room_Message> room_messages;




    private room_DetailCode room_detailcode;




    private room_SPPRef room_sppref;


    public room_ProtocolClass(
        String commType    ) {
        super(
        );
        this.commType = commType;
        this.room_messages = new ArrayList<>();
        this.room_messages = new ArrayList<>();
    }

    public room_ProtocolClass(
        String commType        ArrayList<room_Message> room_messages,        ArrayList<room_Message> room_messages    ) {
        this.commType = commType;
        this.room_messages = room_messages;
        this.room_messages = room_messages;
    }

    public String getCommtype() {
        return commType;
    }

    public void setCommtype(String commType) {
        this.commType = commType;
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
    public room_PortClass getRoom_portclass() {
        return room_portclass;
    }

    public void setRoom_portclass(room_PortClass room_portclass) {
        this.room_portclass = room_portclass;
    }
    public room_PortClass getRoom_portclass() {
        return room_portclass;
    }

    public void setRoom_portclass(room_PortClass room_portclass) {
        this.room_portclass = room_portclass;
    }
    public room_ProtocolSemantics getRoom_protocolsemantics() {
        return room_protocolsemantics;
    }

    public void setRoom_protocolsemantics(room_ProtocolSemantics room_protocolsemantics) {
        this.room_protocolsemantics = room_protocolsemantics;
    }
    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }
    public List<room_Message> getRoom_messages() {
        return room_messages;
    }

    public void addRoom_message(Room_message room_message) {
        this.room_messages.add(room_message);
    }
    public List<room_Message> getRoom_messages() {
        return room_messages;
    }

    public void addRoom_message(Room_message room_message) {
        this.room_messages.add(room_message);
    }
    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }
    public room_SPPRef getRoom_sppref() {
        return room_sppref;
    }

    public void setRoom_sppref(room_SPPRef room_sppref) {
        this.room_sppref = room_sppref;
    }

}