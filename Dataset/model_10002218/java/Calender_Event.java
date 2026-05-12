





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private None admin;
    private None nomarlUser;
    private String eventType;
    private String description;
    private String category;
    private String participantAmount;
    private String date;
    private String time;
    private None volunteer;





    private Normal_user normal_user;




    private List<SuperAdmin> superadmins;




    private List<Admin> admins;




    private List<Volunteer> volunteers;


    public Calender_Event(
        None admin,        None nomarlUser,        String eventType,        String description,        String category,        String participantAmount,        String date,        String time,        None volunteer    ) {
        this.admin = admin;
        this.nomarlUser = nomarlUser;
        this.eventType = eventType;
        this.description = description;
        this.category = category;
        this.participantAmount = participantAmount;
        this.date = date;
        this.time = time;
        this.volunteer = volunteer;
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Calender_Event(
        None admin,        None nomarlUser,        String eventType,        String description,        String category,        String participantAmount,        String date,        String time,        None volunteer        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers    ) {
        this.admin = admin;
        this.nomarlUser = nomarlUser;
        this.eventType = eventType;
        this.description = description;
        this.category = category;
        this.participantAmount = participantAmount;
        this.date = date;
        this.time = time;
        this.volunteer = volunteer;
        this.superadmins = superadmins;
        this.admins = admins;
        this.volunteers = volunteers;
    }

    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
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
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
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
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }

    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
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
    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }

}