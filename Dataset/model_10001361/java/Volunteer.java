





import java.util.List;
import java.util.ArrayList;

public class Volunteer  {

    private int Age;
    private String Preparing_event;
    private String Public_relations;
    private String Time_of_volunteering;
    private String Decor__and_aesthetic_touches;
    private String Professional_status;
    private int Volunteer_ID;
    private String Organization;
    private String Design_and_montag;



    public Volunteer(
        int Age,        String Preparing_event,        String Public_relations,        String Time_of_volunteering,        String Decor__and_aesthetic_touches,        String Professional_status,        int Volunteer_ID,        String Organization,        String Design_and_montag    ) {
        this.Age = Age;
        this.Preparing_event = Preparing_event;
        this.Public_relations = Public_relations;
        this.Time_of_volunteering = Time_of_volunteering;
        this.Decor__and_aesthetic_touches = Decor__and_aesthetic_touches;
        this.Professional_status = Professional_status;
        this.Volunteer_ID = Volunteer_ID;
        this.Organization = Organization;
        this.Design_and_montag = Design_and_montag;
    }


    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getPreparing_event() {
        return Preparing_event;
    }

    public void setPreparing_event(String Preparing_event) {
        this.Preparing_event = Preparing_event;
    }
    public String getPublic_relations() {
        return Public_relations;
    }

    public void setPublic_relations(String Public_relations) {
        this.Public_relations = Public_relations;
    }
    public String getTime_of_volunteering() {
        return Time_of_volunteering;
    }

    public void setTime_of_volunteering(String Time_of_volunteering) {
        this.Time_of_volunteering = Time_of_volunteering;
    }
    public String getDecor__and_aesthetic_touches() {
        return Decor__and_aesthetic_touches;
    }

    public void setDecor__and_aesthetic_touches(String Decor__and_aesthetic_touches) {
        this.Decor__and_aesthetic_touches = Decor__and_aesthetic_touches;
    }
    public String getProfessional_status() {
        return Professional_status;
    }

    public void setProfessional_status(String Professional_status) {
        this.Professional_status = Professional_status;
    }
    public int getVolunteer_id() {
        return Volunteer_ID;
    }

    public void setVolunteer_id(int Volunteer_ID) {
        this.Volunteer_ID = Volunteer_ID;
    }
    public String getOrganization() {
        return Organization;
    }

    public void setOrganization(String Organization) {
        this.Organization = Organization;
    }
    public String getDesign_and_montag() {
        return Design_and_montag;
    }

    public void setDesign_and_montag(String Design_and_montag) {
        this.Design_and_montag = Design_and_montag;
    }


}