





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String description;
    private String category;
    private String date;
    private String time;
    private None nomarlUser;
    private None volunteer;
    private None admin;
    private String participantAmount;
    private String eventType;





    private List<Volunteer> volunteers;




    private List<Executive_Director> executive_directors;




    private List<Admin> admins;




    private Normal_user normal_user;


    public Calender_Event(
        String description,        String category,        String date,        String time,        None nomarlUser,        None volunteer,        None admin,        String participantAmount,        String eventType    ) {
        this.description = description;
        this.category = category;
        this.date = date;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.volunteer = volunteer;
        this.admin = admin;
        this.participantAmount = participantAmount;
        this.eventType = eventType;
        this.volunteers = new ArrayList<>();
        this.executive_directors = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        String description,        String category,        String date,        String time,        None nomarlUser,        None volunteer,        None admin,        String participantAmount,        String eventType        ArrayList<Volunteer> volunteers,        ArrayList<Executive_Director> executive_directors,        ArrayList<Admin> admins    ) {
        this.description = description;
        this.category = category;
        this.date = date;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.volunteer = volunteer;
        this.admin = admin;
        this.participantAmount = participantAmount;
        this.eventType = eventType;
        this.volunteers = volunteers;
        this.executive_directors = executive_directors;
        this.admins = admins;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }

    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }
    public List<Executive_Director> getExecutive_directors() {
        return executive_directors;
    }

    public void addExecutive_director(Executive_director executive_director) {
        this.executive_directors.add(executive_director);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }

}