





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String eventType;
    private String date;
    private String category;
    private None admin;
    private None volunteer;
    private String participantAmount;
    private None nomarlUser;
    private String time;
    private String description;





    private List<SuperAdmin> superadmins;




    private List<Admin> admins;




    private List<Volunteer> volunteers;




    private Normal_user normal_user;


    public Calender_Event(
        String eventType,        String date,        String category,        None admin,        None volunteer,        String participantAmount,        None nomarlUser,        String time,        String description    ) {
        this.eventType = eventType;
        this.date = date;
        this.category = category;
        this.admin = admin;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.description = description;
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Calender_Event(
        String eventType,        String date,        String category,        None admin,        None volunteer,        String participantAmount,        None nomarlUser,        String time,        String description        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers    ) {
        this.eventType = eventType;
        this.date = date;
        this.category = category;
        this.admin = admin;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.time = time;
        this.description = description;
        this.superadmins = superadmins;
        this.admins = admins;
        this.volunteers = volunteers;
    }

    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
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
    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }

}