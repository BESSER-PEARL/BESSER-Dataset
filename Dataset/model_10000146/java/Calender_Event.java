





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private None nomarlUser;
    private String time;
    private String participantAmount;
    private String date;
    private None admin;
    private String eventType;
    private String category;
    private String description;
    private None volunteer;





    private List<Admin> admins;




    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;




    private Normal_user normal_user;


    public Calender_Event(
        None nomarlUser,        String time,        String participantAmount,        String date,        None admin,        String eventType,        String category,        String description,        None volunteer    ) {
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.participantAmount = participantAmount;
        this.date = date;
        this.admin = admin;
        this.eventType = eventType;
        this.category = category;
        this.description = description;
        this.volunteer = volunteer;
        this.admins = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Calender_Event(
        None nomarlUser,        String time,        String participantAmount,        String date,        None admin,        String eventType,        String category,        String description,        None volunteer        ArrayList<Admin> admins,        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers    ) {
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.participantAmount = participantAmount;
        this.date = date;
        this.admin = admin;
        this.eventType = eventType;
        this.category = category;
        this.description = description;
        this.volunteer = volunteer;
        this.admins = admins;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
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
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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
    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }

}