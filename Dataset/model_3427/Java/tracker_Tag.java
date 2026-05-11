





import java.util.List;
import java.util.ArrayList;

public class tracker_Tag  {

    private String id;
    private boolean usainNumberUsed;





    private tracker_Event tracker_event;




    private List<tracker_Event> tracker_events;


    public tracker_Tag(
        String id,        boolean usainNumberUsed    ) {
        this.id = id;
        this.usainNumberUsed = usainNumberUsed;
        this.tracker_events = new ArrayList<>();
    }

    public tracker_Tag(
        String id,        boolean usainNumberUsed        ArrayList<tracker_Event> tracker_events    ) {
        this.id = id;
        this.usainNumberUsed = usainNumberUsed;
        this.tracker_events = tracker_events;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getUsainnumberused() {
        return usainNumberUsed;
    }

    public void setUsainnumberused(boolean usainNumberUsed) {
        this.usainNumberUsed = usainNumberUsed;
    }

    public tracker_Event getTracker_event() {
        return tracker_event;
    }

    public void setTracker_event(tracker_Event tracker_event) {
        this.tracker_event = tracker_event;
    }
    public List<tracker_Event> getTracker_events() {
        return tracker_events;
    }

    public void addTracker_event(Tracker_event tracker_event) {
        this.tracker_events.add(tracker_event);
    }

}