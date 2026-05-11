





import java.util.List;
import java.util.ArrayList;

public class room_ProtocolClass extends RoomClass {

    private String commType;





    private room_ProtocolClass room_protocolclass;


    public room_ProtocolClass(
        String commType    ) {
        super(
        );
        this.commType = commType;
    }


    public String getCommtype() {
        return commType;
    }

    public void setCommtype(String commType) {
        this.commType = commType;
    }

    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }

}