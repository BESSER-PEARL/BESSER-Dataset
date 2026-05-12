





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private String attribute;
    private String Address;
    private int CurrentNumberOfPlayers;
    private int EventId;
    private String DateTime;
    private String Description;
    private int MaxNumberOfPlayers;



    public Event(
        String attribute,        String Address,        int CurrentNumberOfPlayers,        int EventId,        String DateTime,        String Description,        int MaxNumberOfPlayers    ) {
        this.attribute = attribute;
        this.Address = Address;
        this.CurrentNumberOfPlayers = CurrentNumberOfPlayers;
        this.EventId = EventId;
        this.DateTime = DateTime;
        this.Description = Description;
        this.MaxNumberOfPlayers = MaxNumberOfPlayers;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getCurrentnumberofplayers() {
        return CurrentNumberOfPlayers;
    }

    public void setCurrentnumberofplayers(int CurrentNumberOfPlayers) {
        this.CurrentNumberOfPlayers = CurrentNumberOfPlayers;
    }
    public int getEventid() {
        return EventId;
    }

    public void setEventid(int EventId) {
        this.EventId = EventId;
    }
    public String getDatetime() {
        return DateTime;
    }

    public void setDatetime(String DateTime) {
        this.DateTime = DateTime;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getMaxnumberofplayers() {
        return MaxNumberOfPlayers;
    }

    public void setMaxnumberofplayers(int MaxNumberOfPlayers) {
        this.MaxNumberOfPlayers = MaxNumberOfPlayers;
    }


}