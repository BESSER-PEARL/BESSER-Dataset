





import java.util.List;
import java.util.ArrayList;

public class tracker_Premises  {

    private String uri;
    private String premisesId;
    private String emailContact;
    private String name;





    private List<tracker_Animal> tracker_animals;




    private List<tracker_Tag> tracker_tags;


    public tracker_Premises(
        String uri,        String premisesId,        String emailContact,        String name    ) {
        this.uri = uri;
        this.premisesId = premisesId;
        this.emailContact = emailContact;
        this.name = name;
        this.tracker_animals = new ArrayList<>();
        this.tracker_tags = new ArrayList<>();
    }

    public tracker_Premises(
        String uri,        String premisesId,        String emailContact,        String name        ArrayList<tracker_Animal> tracker_animals,        ArrayList<tracker_Tag> tracker_tags    ) {
        this.uri = uri;
        this.premisesId = premisesId;
        this.emailContact = emailContact;
        this.name = name;
        this.tracker_animals = tracker_animals;
        this.tracker_tags = tracker_tags;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getPremisesid() {
        return premisesId;
    }

    public void setPremisesid(String premisesId) {
        this.premisesId = premisesId;
    }
    public String getEmailcontact() {
        return emailContact;
    }

    public void setEmailcontact(String emailContact) {
        this.emailContact = emailContact;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tracker_Animal> getTracker_animals() {
        return tracker_animals;
    }

    public void addTracker_animal(Tracker_animal tracker_animal) {
        this.tracker_animals.add(tracker_animal);
    }
    public List<tracker_Tag> getTracker_tags() {
        return tracker_tags;
    }

    public void addTracker_tag(Tracker_tag tracker_tag) {
        this.tracker_tags.add(tracker_tag);
    }

}