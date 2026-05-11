





import java.util.List;
import java.util.ArrayList;

public class room_Port extends InterfaceItem {

    private int multiplicity;
    private boolean conjugated;





    private room_SubSystemClass room_subsystemclass;




    private room_ActorClass room_actorclass;




    private room_ActorClass room_actorclass;


    public room_Port(
        int multiplicity,        boolean conjugated    ) {
        super(
        );
        this.multiplicity = multiplicity;
        this.conjugated = conjugated;
    }


    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }
    public boolean getConjugated() {
        return conjugated;
    }

    public void setConjugated(boolean conjugated) {
        this.conjugated = conjugated;
    }

    public room_SubSystemClass getRoom_subsystemclass() {
        return room_subsystemclass;
    }

    public void setRoom_subsystemclass(room_SubSystemClass room_subsystemclass) {
        this.room_subsystemclass = room_subsystemclass;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }

}