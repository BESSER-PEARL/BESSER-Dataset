





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String description;
    private String category;
    private String time;
    private None admin;
    private String eventType;
    private None volunteer;
    private String participantAmount;
    private None nomarlUser;
    private String date;





    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;




    private List<Admin> admins;




    private Normal_user normal_user;


    public Calender_Event(
        String description,        String category,        String time,        None admin,        String eventType,        None volunteer,        String participantAmount,        None nomarlUser,        String date    ) {
        this.description = description;
        this.category = category;
        this.time = time;
        this.admin = admin;
        this.eventType = eventType;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.date = date;
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        String description,        String category,        String time,        None admin,        String eventType,        None volunteer,        String participantAmount,        None nomarlUser,        String date        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins    ) {
        this.description = description;
        this.category = category;
        this.time = time;
        this.admin = admin;
        this.eventType = eventType;
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.date = date;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
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
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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