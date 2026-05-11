





import java.util.List;
import java.util.ArrayList;

public class room_ActorClass extends ActorContainerClass {

    private String commType;
    private boolean abstract;





    private room_RoomModel room_roommodel;




    private room_ActorRef room_actorref;




    private room_ActorClass room_actorclass;




    private room_Documentation room_documentation;




    private room_Documentation room_documentation;




    private List<room_Annotation> room_annotations;


    public room_ActorClass(
        String commType,        boolean abstract    ) {
        super(
        );
        this.commType = commType;
        this.abstract = abstract;
        this.room_annotations = new ArrayList<>();
    }

    public room_ActorClass(
        String commType,        boolean abstract        ArrayList<room_Annotation> room_annotations    ) {
        this.commType = commType;
        this.abstract = abstract;
        this.room_annotations = room_annotations;
    }

    public String getCommtype() {
        return commType;
    }

    public void setCommtype(String commType) {
        this.commType = commType;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }
    public room_ActorRef getRoom_actorref() {
        return room_actorref;
    }

    public void setRoom_actorref(room_ActorRef room_actorref) {
        this.room_actorref = room_actorref;
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
    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }
    public List<room_Annotation> getRoom_annotations() {
        return room_annotations;
    }

    public void addRoom_annotation(Room_annotation room_annotation) {
        this.room_annotations.add(room_annotation);
    }

}