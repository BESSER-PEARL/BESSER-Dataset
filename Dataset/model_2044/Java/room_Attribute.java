





import java.util.List;
import java.util.ArrayList;

public class room_Attribute  {

    private String name;
    private int size;





    private room_DataClass room_dataclass;




    private room_ActorClass room_actorclass;


    public room_Attribute(
        String name,        int size    ) {
        this.name = name;
        this.size = size;
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