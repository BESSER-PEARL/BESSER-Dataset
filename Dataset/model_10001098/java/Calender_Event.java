





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String date;
    private String category;
    private None admin;
    private String description;
    private None nomarlUser;
    private String participantAmount;
    private String time;
    private String eventType;
    private None volunteer;





    private List<Admin> admins;




    private Normal_user normal_user;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;


    public Calender_Event(
        String date,        String category,        None admin,        String description,        None nomarlUser,        String participantAmount,        String time,        String eventType,        None volunteer    ) {
        this.date = date;
        this.category = category;
        this.admin = admin;
        this.description = description;
        this.nomarlUser = nomarlUser;
        this.participantAmount = participantAmount;
        this.time = time;
        this.eventType = eventType;
        this.volunteer = volunteer;
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Calender_Event(
        String date,        String category,        None admin,        String description,        None nomarlUser,        String participantAmount,        String time,        String eventType,        None volunteer        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins    ) {
        this.date = date;
        this.category = category;
        this.admin = admin;
        this.description = description;
        this.nomarlUser = nomarlUser;
        this.participantAmount = participantAmount;
        this.time = time;
        this.eventType = eventType;
        this.volunteer = volunteer;
        this.admins = admins;
        this.volunteers = volunteers;
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
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
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
    public String getParticipantamount() {
        return participantAmount;
    }

    public void setParticipantamount(String participantAmount) {
        this.participantAmount = participantAmount;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }

}