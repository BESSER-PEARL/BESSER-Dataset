





import java.util.List;
import java.util.ArrayList;

public class room_Annotation  {

    private String name;





    private room_StructureClass room_structureclass;




    private room_DataClass room_dataclass;




    private room_GeneralProtocolClass room_generalprotocolclass;




    private room_ActorClass room_actorclass;


    public room_Annotation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_StructureClass getRoom_structureclass() {
        return room_structureclass;
    }

    public void setRoom_structureclass(room_StructureClass room_structureclass) {
        this.room_structureclass = room_structureclass;
    }
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
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

}