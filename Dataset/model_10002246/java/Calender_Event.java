





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String eventType;
    private String time;
    private String category;
    private None nomarlUser;
    private String date;
    private None admin;
    private String description;
    private None volunteer;
    private String participantAmount;



    public Calender_Event(
        String eventType,        String time,        String category,        None nomarlUser,        String date,        None admin,        String description,        None volunteer,        String participantAmount    ) {
        this.eventType = eventType;
        this.time = time;
        this.category = category;
        this.nomarlUser = nomarlUser;
        this.date = date;
        this.admin = admin;
        this.description = description;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
    }


    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }


}