





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String description;
    private String eventType;
    private String participantAmount;
    private String category;
    private None nomarlUser;
    private String date;
    private None admin;
    private None volunteer;
    private String time;





    private List<SuperAdmin> superadmins;




    private List<Admin> admins;




    private Normal_user normal_user;




    private List<Volunteer> volunteers;


    public Calender_Event(
        String description,        String eventType,        String participantAmount,        String category,        None nomarlUser,        String date,        None admin,        None volunteer,        String time    ) {
        this.description = description;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.category = category;
        this.nomarlUser = nomarlUser;
        this.date = date;
        this.admin = admin;
        this.volunteer = volunteer;
        this.time = time;
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Calender_Event(
        String description,        String eventType,        String participantAmount,        String category,        None nomarlUser,        String date,        None admin,        None volunteer,        String time        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers    ) {
        this.description = description;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.category = category;
        this.nomarlUser = nomarlUser;
        this.date = date;
        this.admin = admin;
        this.volunteer = volunteer;
        this.time = time;
        this.superadmins = superadmins;
        this.admins = admins;
        this.volunteers = volunteers;
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
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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

}