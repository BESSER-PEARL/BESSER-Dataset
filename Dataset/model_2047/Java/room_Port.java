





import java.util.List;
import java.util.ArrayList;

public class room_Port extends InterfaceItem {

    private boolean conjugated;
    private int multiplicity;





    private room_GeneralProtocolClass room_generalprotocolclass;




    private room_ActorClass room_actorclass;




    private room_SubSystemClass room_subsystemclass;




    private room_Documentation room_documentation;




    private room_ActorClass room_actorclass;


    public room_Port(
        boolean conjugated,        int multiplicity    ) {
        super(
        );
        this.conjugated = conjugated;
        this.multiplicity = multiplicity;
    }


    public boolean getConjugated() {
        return conjugated;
    }

    public void setConjugated(boolean conjugated) {
        this.conjugated = conjugated;
    }
    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }

    public room_GeneralProtocolClass getRoom_generalprotocolclass() {
        return room_generalprotocolclass;
    }

    public void setRoom_generalprotocolclass(room_GeneralProtocolClass room_generalprotocolclass) {
        this.room_generalprotocolclass = room_generalprotocolclass;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_SubSystemClass getRoom_subsystemclass() {
        return room_subsystemclass;
    }

    public void setRoom_subsystemclass(room_SubSystemClass room_subsystemclass) {
        this.room_subsystemclass = room_subsystemclass;
    }
    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }

}