





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String eventType;
    private String time;
    private None volunteer;
    private String description;
    private String participantAmount;
    private None nomarlUser;
    private String category;
    private None admin;
    private String date;





    private List<Volunteer> volunteers;




    private List<Admin> admins;




    private List<Executive_Director> executive_directors;




    private Normal_user normal_user;


    public Calender_Event(
        String eventType,        String time,        None volunteer,        String description,        String participantAmount,        None nomarlUser,        String category,        None admin,        String date    ) {
        this.eventType = eventType;
        this.time = time;
        this.volunteer = volunteer;
        this.description = description;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.category = category;
        this.admin = admin;
        this.date = date;
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.executive_directors = new ArrayList<>();
    }

    public Calender_Event(
        String eventType,        String time,        None volunteer,        String description,        String participantAmount,        None nomarlUser,        String category,        None admin,        String date        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins,        ArrayList<Executive_Director> executive_directors    ) {
        this.eventType = eventType;
        this.time = time;
        this.volunteer = volunteer;
        this.description = description;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.category = category;
        this.admin = admin;
        this.date = date;
        this.volunteers = volunteers;
        this.admins = admins;
        this.executive_directors = executive_directors;
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
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<Executive_Director> getExecutive_directors() {
        return executive_directors;
    }

    public void addExecutive_director(Executive_director executive_director) {
        this.executive_directors.add(executive_director);
    }
    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }

}