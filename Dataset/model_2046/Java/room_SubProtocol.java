





import java.util.List;
import java.util.ArrayList;

public class room_SubProtocol  {

    private String name;





    private room_CompoundProtocolClass room_compoundprotocolclass;




    private room_GeneralProtocolClass room_generalprotocolclass;


    public room_SubProtocol(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_CompoundProtocolClass getRoom_compoundprotocolclass() {
        return room_compoundprotocolclass;
    }

    public void setRoom_compoundprotocolclass(room_CompoundProtocolClass room_compoundprotocolclass) {
        this.room_compoundprotocolclass = room_compoundprotocolclass;
    }
    public room_GeneralProtocolClass getRoom_generalprotocolclass() {
        return room_generalprotocolclass;
    }

    public void setRoom_generalprotocolclass(room_GeneralProtocolClass room_generalprotocolclass) {
        this.room_generalprotocolclass = room_generalprotocolclass;
    }

}