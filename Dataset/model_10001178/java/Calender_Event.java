





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String description;
    private None volunteer;
    private String date;
    private String eventType;
    private None admin;
    private String category;
    private String time;
    private None nomarlUser;
    private String participantAmount;





    private Normal_user normal_user;




    private List<Admin> admins;




    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;


    public Calender_Event(
        String description,        None volunteer,        String date,        String eventType,        None admin,        String category,        String time,        None nomarlUser,        String participantAmount    ) {
        this.description = description;
        this.volunteer = volunteer;
        this.date = date;
        this.eventType = eventType;
        this.admin = admin;
        this.category = category;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.participantAmount = participantAmount;
        this.admins = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Calender_Event(
        String description,        None volunteer,        String date,        String eventType,        None admin,        String category,        String time,        None nomarlUser,        String participantAmount        ArrayList<Admin> admins,        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers    ) {
        this.description = description;
        this.volunteer = volunteer;
        this.date = date;
        this.eventType = eventType;
        this.admin = admin;
        this.category = category;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.participantAmount = participantAmount;
        this.admins = admins;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
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
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }

    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }
    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }

}