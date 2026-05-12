





import java.util.List;
import java.util.ArrayList;

public class EventType  {

    private int EventTypeId;
    private String Type;





    private List<Event> events;


    public EventType(
        int EventTypeId,        String Type    ) {
        this.EventTypeId = EventTypeId;
        this.Type = Type;
        this.events = new ArrayList<>();
    }

    public EventType(
        int EventTypeId,        String Type        ArrayList<Event> events    ) {
        this.EventTypeId = EventTypeId;
        this.Type = Type;
        this.events = events;
    }

    public int getEventtypeid() {
        return EventTypeId;
    }

    public void setEventtypeid(int EventTypeId) {
        this.EventTypeId = EventTypeId;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public List<Event> getEvents() {
        return events;
    }

    public void addEvent(Event event) {
        this.events.add(event);
    }

}