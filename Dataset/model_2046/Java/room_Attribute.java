





import java.util.List;
import java.util.ArrayList;

public class room_Attribute  {

    private String defaultValueLiteral;
    private String name;
    private int size;





    private room_RefableType room_refabletype;




    private room_ActorClass room_actorclass;




    private room_Documentation room_documentation;




    private room_DataClass room_dataclass;


    public room_Attribute(
        String defaultValueLiteral,        String name,        int size    ) {
        this.defaultValueLiteral = defaultValueLiteral;
        this.name = name;
        this.size = size;
    }


    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public room_RefableType getRoom_refabletype() {
        return room_refabletype;
    }

    public void setRoom_refabletype(room_RefableType room_refabletype) {
        this.room_refabletype = room_refabletype;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }

}