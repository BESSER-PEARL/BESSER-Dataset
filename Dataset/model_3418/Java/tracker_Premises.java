





import java.util.List;
import java.util.ArrayList;

public class tracker_Premises  {

    private String emailContact;
    private String premisesId;





    private List<tracker_Tag> tracker_tags;




    private List<tracker_Animal> tracker_animals;


    public tracker_Premises(
        String emailContact,        String premisesId    ) {
        this.emailContact = emailContact;
        this.premisesId = premisesId;
        this.tracker_tags = new ArrayList<>();
        this.tracker_animals = new ArrayList<>();
    }

    public tracker_Premises(
        String emailContact,        String premisesId        ArrayList<tracker_Tag> tracker_tags,        ArrayList<tracker_Animal> tracker_animals    ) {
        this.emailContact = emailContact;
        this.premisesId = premisesId;
        this.tracker_tags = tracker_tags;
        this.tracker_animals = tracker_animals;
    }

    public String getEmailcontact() {
        return emailContact;
    }

    public void setEmailcontact(String emailContact) {
        this.emailContact = emailContact;
    }
    public String getPremisesid() {
        return premisesId;
    }

    public void setPremisesid(String premisesId) {
        this.premisesId = premisesId;
    }

    public List<tracker_Tag> getTracker_tags() {
        return tracker_tags;
    }

    public void addTracker_tag(Tracker_tag tracker_tag) {
        this.tracker_tags.add(tracker_tag);
    }
    public List<tracker_Animal> getTracker_animals() {
        return tracker_animals;
    }

    public void addTracker_animal(Tracker_animal tracker_animal) {
        this.tracker_animals.add(tracker_animal);
    }

}