





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private None volunteer;
    private String participantAmount;
    private None admin;
    private String eventType;
    private String time;
    private None nomarlUser;
    private String description;
    private String date;
    private String category;





    private Normal_user normal_user;




    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;




    private List<Admin> admins;


    public Calender_Event(
        None volunteer,        String participantAmount,        None admin,        String eventType,        String time,        None nomarlUser,        String description,        String date,        String category    ) {
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.admin = admin;
        this.eventType = eventType;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.date = date;
        this.category = category;
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        None volunteer,        String participantAmount,        None admin,        String eventType,        String time,        None nomarlUser,        String description,        String date,        String category        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins    ) {
        this.volunteer = volunteer;
        this.participantAmount = participantAmount;
        this.admin = admin;
        this.eventType = eventType;
        this.time = time;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.date = date;
        this.category = category;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
        this.admins = admins;
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
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

}