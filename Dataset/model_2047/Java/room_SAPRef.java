





import java.util.List;
import java.util.ArrayList;

public class room_SAPRef extends InterfaceItem {






    private room_ProtocolClass room_protocolclass;




    private room_ActorClass room_actorclass;


    public room_SAPRef(
    ) {
        super(
        );
    }



    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }

}