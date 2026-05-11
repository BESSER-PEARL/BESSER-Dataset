





import java.util.List;
import java.util.ArrayList;

public class events_EventModel  {






    private events_EventPattern events_eventpattern;




    private List<events_EventPattern> events_eventpatterns;


    public events_EventModel(
    ) {
        this.events_eventpatterns = new ArrayList<>();
    }

    public events_EventModel(
        ArrayList<events_EventPattern> events_eventpatterns    ) {
        this.events_eventpatterns = events_eventpatterns;
    }


    public events_EventPattern getEvents_eventpattern() {
        return events_eventpattern;
    }

    public void setEvents_eventpattern(events_EventPattern events_eventpattern) {
        this.events_eventpattern = events_eventpattern;
    }
    public List<events_EventPattern> getEvents_eventpatterns() {
        return events_eventpatterns;
    }

    public void addEvents_eventpattern(Events_eventpattern events_eventpattern) {
        this.events_eventpatterns.add(events_eventpattern);
    }

}