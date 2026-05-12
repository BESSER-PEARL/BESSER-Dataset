





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String category;
    private String date;
    private String eventType;
    private String participantAmount;
    private String description;
    private None nomarlUser;
    private String time;
    private None volunteer;
    private None admin;





    private Normal_user normal_user;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;




    private List<Admin> admins;


    public Calender_Event(
        String category,        String date,        String eventType,        String participantAmount,        String description,        None nomarlUser,        String time,        None volunteer,        None admin    ) {
        this.category = category;
        this.date = date;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.description = description;
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.volunteer = volunteer;
        this.admin = admin;
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        String category,        String date,        String eventType,        String participantAmount,        String description,        None nomarlUser,        String time,        None volunteer,        None admin        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins    ) {
        this.category = category;
        this.date = date;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.description = description;
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.volunteer = volunteer;
        this.admin = admin;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
        this.admins = admins;
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
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
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
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }

    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }
    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}