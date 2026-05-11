





import java.util.List;
import java.util.ArrayList;

public class tracker_EventHistory  {






    private List<tracker_Event> tracker_events;




    private tracker_Premises tracker_premises;


    public tracker_EventHistory(
    ) {
        this.tracker_events = new ArrayList<>();
    }

    public tracker_EventHistory(
        ArrayList<tracker_Event> tracker_events    ) {
        this.tracker_events = tracker_events;
    }


    public List<tracker_Event> getTracker_events() {
        return tracker_events;
    }

    public void addTracker_event(Tracker_event tracker_event) {
        this.tracker_events.add(tracker_event);
    }
    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }

}