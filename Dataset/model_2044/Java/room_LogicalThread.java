





import java.util.List;
import java.util.ArrayList;

public class room_LogicalThread  {

    private String name;





    private room_SubSystemClass room_subsystemclass;




    private List<room_ActorInstancePath> room_actorinstancepaths;


    public room_LogicalThread(
        String name    ) {
        this.name = name;
        this.room_actorinstancepaths = new ArrayList<>();
    }

    public room_LogicalThread(
        String name        ArrayList<room_ActorInstancePath> room_actorinstancepaths    ) {
        this.name = name;
        this.room_actorinstancepaths = room_actorinstancepaths;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_SubSystemClass getRoom_subsystemclass() {
        return room_subsystemclass;
    }

    public void setRoom_subsystemclass(room_SubSystemClass room_subsystemclass) {
        this.room_subsystemclass = room_subsystemclass;
    }
    public List<room_ActorInstancePath> getRoom_actorinstancepaths() {
        return room_actorinstancepaths;
    }

    public void addRoom_actorinstancepath(Room_actorinstancepath room_actorinstancepath) {
        this.room_actorinstancepaths.add(room_actorinstancepath);
    }

}