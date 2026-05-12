





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String date;
    private String category;
    private String time;
    private String description;
    private String eventType;
    private None nomarlUser;
    private None volunteer;
    private String participantAmount;
    private None admin;





    private List<Volunteer> volunteers;




    private Normal_user normal_user;




    private List<Admin> admins;




    private List<SuperAdmin> superadmins;


    public Calender_Event(
        String date,        String category,        String time,        String description,        String eventType,        None nomarlUser,        None volunteer,        String participantAmount,        None admin    ) {
        this.date = date;
        this.category = category;
        this.time = time;
        this.description = description;
        this.eventType = eventType;
        this.nomarlUser = nomarlUser;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.admin = admin;
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Calender_Event(
        String date,        String category,        String time,        String description,        String eventType,        None nomarlUser,        None volunteer,        String participantAmount,        None admin        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins,        ArrayList<SuperAdmin> superadmins    ) {
        this.date = date;
        this.category = category;
        this.time = time;
        this.description = description;
        this.eventType = eventType;
        this.nomarlUser = nomarlUser;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.admin = admin;
        this.volunteers = volunteers;
        this.admins = admins;
        this.superadmins = superadmins;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
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
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }

    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
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

}