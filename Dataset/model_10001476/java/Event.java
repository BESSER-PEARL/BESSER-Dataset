





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private None eventhead;
    private String eventname;
    private String eventype;
    private int eventid;
    private int date;
    private int amount;





    private Volunteer volunteer;




    private Eventhead eventhead;




    private Client client;


    public Event(
        None eventhead,        String eventname,        String eventype,        int eventid,        int date,        int amount    ) {
        this.eventhead = eventhead;
        this.eventname = eventname;
        this.eventype = eventype;
        this.eventid = eventid;
        this.date = date;
        this.amount = amount;
    }


    public None getEventhead() {
        return eventhead;
    }

    public void setEventhead(None eventhead) {
        this.eventhead = eventhead;
    }
    public String getEventname() {
        return eventname;
    }

    public void setEventname(String eventname) {
        this.eventname = eventname;
    }
    public String getEventype() {
        return eventype;
    }

    public void setEventype(String eventype) {
        this.eventype = eventype;
    }
    public int getEventid() {
        return eventid;
    }

    public void setEventid(int eventid) {
        this.eventid = eventid;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Volunteer getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(Volunteer volunteer) {
        this.volunteer = volunteer;
    }
    public Eventhead getEventhead() {
        return eventhead;
    }

    public void setEventhead(Eventhead eventhead) {
        this.eventhead = eventhead;
    }
    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}