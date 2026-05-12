





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private None volunteer;
    private None admin;
    private String time;
    private String date;
    private String eventType;
    private String participantAmount;
    private None nomarlUser;
    private String description;
    private String category;





    private List<Admin> admins;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;




    private Normal_user normal_user;


    public Calender_Event(
        None volunteer,        None admin,        String time,        String date,        String eventType,        String participantAmount,        None nomarlUser,        String description,        String category    ) {
        this.volunteer = volunteer;
        this.admin = admin;
        this.time = time;
        this.date = date;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.category = category;
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Calender_Event(
        None volunteer,        None admin,        String time,        String date,        String eventType,        String participantAmount,        None nomarlUser,        String description,        String category        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins    ) {
        this.volunteer = volunteer;
        this.admin = admin;
        this.time = time;
        this.date = date;
        this.eventType = eventType;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.category = category;
        this.admins = admins;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
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
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }
    public Normal_user getNormal_user() {
        return normal_user;
    }

    public void setNormal_user(Normal_user normal_user) {
        this.normal_user = normal_user;
    }

}