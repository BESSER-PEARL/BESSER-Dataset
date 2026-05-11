





import java.util.List;
import java.util.ArrayList;

public class tracker_Premises  {

    private String emailContact;
    private String premisesId;
    private String name;
    private String uri;





    private List<tracker_Location> tracker_locations;




    private tracker_Schema tracker_schema;




    private List<tracker_Tag> tracker_tags;


    public tracker_Premises(
        String emailContact,        String premisesId,        String name,        String uri    ) {
        this.emailContact = emailContact;
        this.premisesId = premisesId;
        this.name = name;
        this.uri = uri;
        this.tracker_locations = new ArrayList<>();
        this.tracker_tags = new ArrayList<>();
    }

    public tracker_Premises(
        String emailContact,        String premisesId,        String name,        String uri        ArrayList<tracker_Location> tracker_locations,        ArrayList<tracker_Tag> tracker_tags    ) {
        this.emailContact = emailContact;
        this.premisesId = premisesId;
        this.name = name;
        this.uri = uri;
        this.tracker_locations = tracker_locations;
        this.tracker_tags = tracker_tags;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<tracker_Location> getTracker_locations() {
        return tracker_locations;
    }

    public void addTracker_location(Tracker_location tracker_location) {
        this.tracker_locations.add(tracker_location);
    }
    public tracker_Schema getTracker_schema() {
        return tracker_schema;
    }

    public void setTracker_schema(tracker_Schema tracker_schema) {
        this.tracker_schema = tracker_schema;
    }
    public List<tracker_Tag> getTracker_tags() {
        return tracker_tags;
    }

    public void addTracker_tag(Tracker_tag tracker_tag) {
        this.tracker_tags.add(tracker_tag);
    }

}