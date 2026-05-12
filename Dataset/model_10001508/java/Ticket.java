





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private None event;
    private String id;





    private Event event;


    public Ticket(
        None event,        String id    ) {
        this.event = event;
        this.id = id;
    }


    public None getEvent() {
        return event;
    }

    public void setEvent(None event) {
        this.event = event;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }

}