





import java.util.List;
import java.util.ArrayList;

public class room_RoomModel  {

    private String name;





    private List<room_SubSystemClass> room_subsystemclasss;




    private List<room_ExternalType> room_externaltypes;




    private List<room_ProtocolClass> room_protocolclasss;




    private List<room_ActorClass> room_actorclasss;




    private List<room_LogicalSystem> room_logicalsystems;




    private List<room_PrimitiveType> room_primitivetypes;




    private List<room_DataClass> room_dataclasss;


    public room_RoomModel(
        String name    ) {
        this.name = name;
        this.room_subsystemclasss = new ArrayList<>();
        this.room_externaltypes = new ArrayList<>();
        this.room_protocolclasss = new ArrayList<>();
        this.room_actorclasss = new ArrayList<>();
        this.room_logicalsystems = new ArrayList<>();
        this.room_primitivetypes = new ArrayList<>();
        this.room_dataclasss = new ArrayList<>();
    }

    public room_RoomModel(
        String name        ArrayList<room_SubSystemClass> room_subsystemclasss,        ArrayList<room_ExternalType> room_externaltypes,        ArrayList<room_ProtocolClass> room_protocolclasss,        ArrayList<room_ActorClass> room_actorclasss,        ArrayList<room_LogicalSystem> room_logicalsystems,        ArrayList<room_PrimitiveType> room_primitivetypes,        ArrayList<room_DataClass> room_dataclasss    ) {
        this.name = name;
        this.room_subsystemclasss = room_subsystemclasss;
        this.room_externaltypes = room_externaltypes;
        this.room_protocolclasss = room_protocolclasss;
        this.room_actorclasss = room_actorclasss;
        this.room_logicalsystems = room_logicalsystems;
        this.room_primitivetypes = room_primitivetypes;
        this.room_dataclasss = room_dataclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<room_SubSystemClass> getRoom_subsystemclasss() {
        return room_subsystemclasss;
    }

    public void addRoom_subsystemclass(Room_subsystemclass room_subsystemclass) {
        this.room_subsystemclasss.add(room_subsystemclass);
    }
    public List<room_ExternalType> getRoom_externaltypes() {
        return room_externaltypes;
    }

    public void addRoom_externaltype(Room_externaltype room_externaltype) {
        this.room_externaltypes.add(room_externaltype);
    }
    public List<room_ProtocolClass> getRoom_protocolclasss() {
        return room_protocolclasss;
    }

    public void addRoom_protocolclass(Room_protocolclass room_protocolclass) {
        this.room_protocolclasss.add(room_protocolclass);
    }
    public List<room_ActorClass> getRoom_actorclasss() {
        return room_actorclasss;
    }

    public void addRoom_actorclass(Room_actorclass room_actorclass) {
        this.room_actorclasss.add(room_actorclass);
    }
    public List<room_LogicalSystem> getRoom_logicalsystems() {
        return room_logicalsystems;
    }

    public void addRoom_logicalsystem(Room_logicalsystem room_logicalsystem) {
        this.room_logicalsystems.add(room_logicalsystem);
    }
    public List<room_PrimitiveType> getRoom_primitivetypes() {
        return room_primitivetypes;
    }

    public void addRoom_primitivetype(Room_primitivetype room_primitivetype) {
        this.room_primitivetypes.add(room_primitivetype);
    }
    public List<room_DataClass> getRoom_dataclasss() {
        return room_dataclasss;
    }

    public void addRoom_dataclass(Room_dataclass room_dataclass) {
        this.room_dataclasss.add(room_dataclass);
    }

}