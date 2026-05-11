





import java.util.List;
import java.util.ArrayList;

public class room_Trigger  {






    private List<room_MessageFromIf> room_messagefromifs;




    private room_Guard room_guard;




    private room_TriggeredTransition room_triggeredtransition;


    public room_Trigger(
    ) {
        this.room_messagefromifs = new ArrayList<>();
    }

    public room_Trigger(
        ArrayList<room_MessageFromIf> room_messagefromifs    ) {
        this.room_messagefromifs = room_messagefromifs;
    }


    public List<room_MessageFromIf> getRoom_messagefromifs() {
        return room_messagefromifs;
    }

    public void addRoom_messagefromif(Room_messagefromif room_messagefromif) {
        this.room_messagefromifs.add(room_messagefromif);
    }
    public room_Guard getRoom_guard() {
        return room_guard;
    }

    public void setRoom_guard(room_Guard room_guard) {
        this.room_guard = room_guard;
    }
    public room_TriggeredTransition getRoom_triggeredtransition() {
        return room_triggeredtransition;
    }

    public void setRoom_triggeredtransition(room_TriggeredTransition room_triggeredtransition) {
        this.room_triggeredtransition = room_triggeredtransition;
    }

}