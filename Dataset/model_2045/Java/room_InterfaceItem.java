





import java.util.List;
import java.util.ArrayList;

public class room_InterfaceItem  {

    private String name;





    private room_ProtocolClass room_protocolclass;


    public room_InterfaceItem(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }

}