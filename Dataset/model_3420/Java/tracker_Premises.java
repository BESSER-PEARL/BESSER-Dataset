





import java.util.List;
import java.util.ArrayList;

public class tracker_Premises  {

    private String premisesId;
    private String emailContact;





    private List<tracker_Animal> tracker_animals;


    public tracker_Premises(
        String premisesId,        String emailContact    ) {
        this.premisesId = premisesId;
        this.emailContact = emailContact;
        this.tracker_animals = new ArrayList<>();
    }

    public tracker_Premises(
        String premisesId,        String emailContact        ArrayList<tracker_Animal> tracker_animals    ) {
        this.premisesId = premisesId;
        this.emailContact = emailContact;
        this.tracker_animals = tracker_animals;
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

    public List<tracker_Animal> getTracker_animals() {
        return tracker_animals;
    }

    public void addTracker_animal(Tracker_animal tracker_animal) {
        this.tracker_animals.add(tracker_animal);
    }

}