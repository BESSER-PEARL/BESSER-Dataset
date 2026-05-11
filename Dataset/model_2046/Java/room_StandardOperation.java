





import java.util.List;
import java.util.ArrayList;

public class room_StandardOperation extends Operation {

    private boolean destructor;





    private room_DataClass room_dataclass;




    private room_ActorClass room_actorclass;


    public room_StandardOperation(
        boolean destructor    ) {
        super(
        );
        this.destructor = destructor;
    }


    public boolean getDestructor() {
        return destructor;
    }

    public void setDestructor(boolean destructor) {
        this.destructor = destructor;
    }

    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }

}