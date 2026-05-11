





import java.util.List;
import java.util.ArrayList;

public class room_SemanticsRule  {






    private room_ProtocolSemantics room_protocolsemantics;




    private room_Message room_message;




    private List<room_SemanticsRule> room_semanticsrules;


    public room_SemanticsRule(
    ) {
        this.room_semanticsrules = new ArrayList<>();
    }

    public room_SemanticsRule(
        ArrayList<room_SemanticsRule> room_semanticsrules    ) {
        this.room_semanticsrules = room_semanticsrules;
    }


    public room_ProtocolSemantics getRoom_protocolsemantics() {
        return room_protocolsemantics;
    }

    public void setRoom_protocolsemantics(room_ProtocolSemantics room_protocolsemantics) {
        this.room_protocolsemantics = room_protocolsemantics;
    }
    public room_Message getRoom_message() {
        return room_message;
    }

    public void setRoom_message(room_Message room_message) {
        this.room_message = room_message;
    }
    public List<room_SemanticsRule> getRoom_semanticsrules() {
        return room_semanticsrules;
    }

    public void addRoom_semanticsrule(Room_semanticsrule room_semanticsrule) {
        this.room_semanticsrules.add(room_semanticsrule);
    }

}