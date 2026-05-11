





import java.util.List;
import java.util.ArrayList;

public class room_ActorClass extends ActorContainerClass {

    private boolean abstract;
    private String commType;





    private room_ActorRef room_actorref;




    private List<room_Attribute> room_attributes;




    private List<room_StandardOperation> room_standardoperations;




    private room_ActorClass room_actorclass;


    public room_ActorClass(
        boolean abstract,        String commType    ) {
        super(
        );
        this.abstract = abstract;
        this.commType = commType;
        this.room_attributes = new ArrayList<>();
        this.room_standardoperations = new ArrayList<>();
    }

    public room_ActorClass(
        boolean abstract,        String commType        ArrayList<room_Attribute> room_attributes,        ArrayList<room_StandardOperation> room_standardoperations    ) {
        this.abstract = abstract;
        this.commType = commType;
        this.room_attributes = room_attributes;
        this.room_standardoperations = room_standardoperations;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getCommtype() {
        return commType;
    }

    public void setCommtype(String commType) {
        this.commType = commType;
    }

    public room_ActorRef getRoom_actorref() {
        return room_actorref;
    }

    public void setRoom_actorref(room_ActorRef room_actorref) {
        this.room_actorref = room_actorref;
    }
    public List<room_Attribute> getRoom_attributes() {
        return room_attributes;
    }

    public void addRoom_attribute(Room_attribute room_attribute) {
        this.room_attributes.add(room_attribute);
    }
    public List<room_StandardOperation> getRoom_standardoperations() {
        return room_standardoperations;
    }

    public void addRoom_standardoperation(Room_standardoperation room_standardoperation) {
        this.room_standardoperations.add(room_standardoperation);
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }

}