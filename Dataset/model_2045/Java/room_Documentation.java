





import java.util.List;
import java.util.ArrayList;

public class room_Documentation  {

    private String text;





    private room_Transition room_transition;




    private room_State room_state;




    private room_ActorContainerRef room_actorcontainerref;




    private room_ActorClass room_actorclass;




    private room_Port room_port;




    private room_Operation room_operation;




    private room_RoomModel room_roommodel;




    private room_ActorClass room_actorclass;




    private room_Message room_message;




    private room_Attribute room_attribute;




    private room_ChoicePoint room_choicepoint;


    public room_Documentation(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public room_Transition getRoom_transition() {
        return room_transition;
    }

    public void setRoom_transition(room_Transition room_transition) {
        this.room_transition = room_transition;
    }
    public room_State getRoom_state() {
        return room_state;
    }

    public void setRoom_state(room_State room_state) {
        this.room_state = room_state;
    }
    public room_ActorContainerRef getRoom_actorcontainerref() {
        return room_actorcontainerref;
    }

    public void setRoom_actorcontainerref(room_ActorContainerRef room_actorcontainerref) {
        this.room_actorcontainerref = room_actorcontainerref;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_Port getRoom_port() {
        return room_port;
    }

    public void setRoom_port(room_Port room_port) {
        this.room_port = room_port;
    }
    public room_Operation getRoom_operation() {
        return room_operation;
    }

    public void setRoom_operation(room_Operation room_operation) {
        this.room_operation = room_operation;
    }
    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }
    public room_ActorClass getRoom_actorclass() {
        return room_actorclass;
    }

    public void setRoom_actorclass(room_ActorClass room_actorclass) {
        this.room_actorclass = room_actorclass;
    }
    public room_Message getRoom_message() {
        return room_message;
    }

    public void setRoom_message(room_Message room_message) {
        this.room_message = room_message;
    }
    public room_Attribute getRoom_attribute() {
        return room_attribute;
    }

    public void setRoom_attribute(room_Attribute room_attribute) {
        this.room_attribute = room_attribute;
    }
    public room_ChoicePoint getRoom_choicepoint() {
        return room_choicepoint;
    }

    public void setRoom_choicepoint(room_ChoicePoint room_choicepoint) {
        this.room_choicepoint = room_choicepoint;
    }

}