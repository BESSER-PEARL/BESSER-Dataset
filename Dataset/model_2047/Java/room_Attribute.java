





import java.util.List;
import java.util.ArrayList;

public class room_Attribute  {

    private String name;
    private String defaultValueLiteral;
    private int size;





    private room_Documentation room_documentation;




    private room_ActorClass room_actorclass;




    private room_DataClass room_dataclass;


    public room_Attribute(
        String name,        String defaultValueLiteral,        int size    ) {
        this.name = name;
        this.defaultValueLiteral = defaultValueLiteral;
        this.size = size;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
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
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }

}