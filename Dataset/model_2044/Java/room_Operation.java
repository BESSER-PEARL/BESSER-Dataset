





import java.util.List;
import java.util.ArrayList;

public class room_Operation  {

    private String name;





    private room_ActorClass room_actorclass;




    private room_DataClass room_dataclass;




    private room_FreeType room_freetype;




    private List<room_FreeTypedID> room_freetypedids;


    public room_Operation(
        String name    ) {
        this.name = name;
        this.room_freetypedids = new ArrayList<>();
    }

    public room_Operation(
        String name        ArrayList<room_FreeTypedID> room_freetypedids    ) {
        this.name = name;
        this.room_freetypedids = room_freetypedids;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public room_FreeType getRoom_freetype() {
        return room_freetype;
    }

    public void setRoom_freetype(room_FreeType room_freetype) {
        this.room_freetype = room_freetype;
    }
    public List<room_FreeTypedID> getRoom_freetypedids() {
        return room_freetypedids;
    }

    public void addRoom_freetypedid(Room_freetypedid room_freetypedid) {
        this.room_freetypedids.add(room_freetypedid);
    }

}