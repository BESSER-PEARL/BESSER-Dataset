





import java.util.List;
import java.util.ArrayList;

public class conference_Talk  {

    private int duration;
    private String time;
    private String abstract;
    private String name;





    private conference_Day conference_day;




    private conference_Location conference_location;




    private conference_Location conference_location;




    private conference_Person conference_person;




    private conference_Track conference_track;




    private List<conference_Person> conference_persons;




    private conference_Day conference_day;


    public conference_Talk(
        int duration,        String time,        String abstract,        String name    ) {
        this.duration = duration;
        this.time = time;
        this.abstract = abstract;
        this.name = name;
        this.conference_persons = new ArrayList<>();
    }

    public conference_Talk(
        int duration,        String time,        String abstract,        String name        ArrayList<conference_Person> conference_persons    ) {
        this.duration = duration;
        this.time = time;
        this.abstract = abstract;
        this.name = name;
        this.conference_persons = conference_persons;
    }

    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public conference_Day getConference_day() {
        return conference_day;
    }

    public void setConference_day(conference_Day conference_day) {
        this.conference_day = conference_day;
    }
    public conference_Location getConference_location() {
        return conference_location;
    }

    public void setConference_location(conference_Location conference_location) {
        this.conference_location = conference_location;
    }
    public conference_Location getConference_location() {
        return conference_location;
    }

    public void setConference_location(conference_Location conference_location) {
        this.conference_location = conference_location;
    }
    public conference_Person getConference_person() {
        return conference_person;
    }

    public void setConference_person(conference_Person conference_person) {
        this.conference_person = conference_person;
    }
    public conference_Track getConference_track() {
        return conference_track;
    }

    public void setConference_track(conference_Track conference_track) {
        this.conference_track = conference_track;
    }
    public List<conference_Person> getConference_persons() {
        return conference_persons;
    }

    public void addConference_person(Conference_person conference_person) {
        this.conference_persons.add(conference_person);
    }
    public conference_Day getConference_day() {
        return conference_day;
    }

    public void setConference_day(conference_Day conference_day) {
        this.conference_day = conference_day;
    }

}