





import java.util.List;
import java.util.ArrayList;

public class room_ActorClass extends ActorContainerClass {

    private boolean abstract;





    private room_ActorClass room_actorclass;




    private room_RoomModel room_roommodel;


    public room_ActorClass(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}