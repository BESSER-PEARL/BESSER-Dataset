





import java.util.List;
import java.util.ArrayList;

public class events_ComplexEventPattern extends EventPattern {






    private events_Timewindow events_timewindow;




    private List<events_EventPatternReference> events_eventpatternreferences;


    public events_ComplexEventPattern(
    ) {
        super(
        );
        this.events_eventpatternreferences = new ArrayList<>();
    }

    public events_ComplexEventPattern(
        ArrayList<events_EventPatternReference> events_eventpatternreferences    ) {
        this.events_eventpatternreferences = events_eventpatternreferences;
    }


    public events_Timewindow getEvents_timewindow() {
        return events_timewindow;
    }

    public void setEvents_timewindow(events_Timewindow events_timewindow) {
        this.events_timewindow = events_timewindow;
    }
    public List<events_EventPatternReference> getEvents_eventpatternreferences() {
        return events_eventpatternreferences;
    }

    public void addEvents_eventpatternreference(Events_eventpatternreference events_eventpatternreference) {
        this.events_eventpatternreferences.add(events_eventpatternreference);
    }

}