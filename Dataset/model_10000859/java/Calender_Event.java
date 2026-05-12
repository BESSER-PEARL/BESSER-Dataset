





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String time;
    private String category;
    private String participantAmount;
    private None nomarlUser;
    private String eventType;
    private None admin;
    private None volunteer;
    private String date;
    private String description;





    private Normal_user normal_user;




    private List<Admin> admins;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;


    public Calender_Event(
        String time,        String category,        String participantAmount,        None nomarlUser,        String eventType,        None admin,        None volunteer,        String date,        String description    ) {
        this.time = time;
        this.category = category;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.eventType = eventType;
        this.admin = admin;
        this.volunteer = volunteer;
        this.date = date;
        this.description = description;
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Calender_Event(
        String time,        String category,        String participantAmount,        None nomarlUser,        String eventType,        None admin,        None volunteer,        String date,        String description        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins    ) {
        this.time = time;
        this.category = category;
        this.participantAmount = participantAmount;
        this.nomarlUser = nomarlUser;
        this.eventType = eventType;
        this.admin = admin;
        this.volunteer = volunteer;
        this.date = date;
        this.description = description;
        this.admins = admins;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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