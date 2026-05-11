





import java.util.List;
import java.util.ArrayList;

public class smDsl_EventsSection  {






    private smDsl_Model smdsl_model;




    private List<smDsl_Event> smdsl_events;


    public smDsl_EventsSection(
    ) {
        this.smdsl_events = new ArrayList<>();
    }

    public smDsl_EventsSection(
        ArrayList<smDsl_Event> smdsl_events    ) {
        this.smdsl_events = smdsl_events;
    }


    public smDsl_Model getSmdsl_model() {
        return smdsl_model;
    }

    public void setSmdsl_model(smDsl_Model smdsl_model) {
        this.smdsl_model = smdsl_model;
    }
    public List<smDsl_Event> getSmdsl_events() {
        return smdsl_events;
    }

    public void addSmdsl_event(Smdsl_event smdsl_event) {
        this.smdsl_events.add(smdsl_event);
    }

}