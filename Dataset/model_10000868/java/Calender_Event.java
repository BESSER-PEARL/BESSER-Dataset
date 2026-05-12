





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private String eventType;
    private String time;
    private None volunteer;
    private None admin;
    private String participantAmount;
    private String date;
    private String category;
    private None nomarlUser;
    private String description;





    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;




    private List<Admin> admins;




    private Normal_user normal_user;


    public Calender_Event(
        String eventType,        String time,        None volunteer,        None admin,        String participantAmount,        String date,        String category,        None nomarlUser,        String description    ) {
        this.eventType = eventType;
        this.time = time;
        this.volunteer = volunteer;
        this.admin = admin;
        this.participantAmount = participantAmount;
        this.date = date;
        this.category = category;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        String eventType,        String time,        None volunteer,        None admin,        String participantAmount,        String date,        String category,        None nomarlUser,        String description        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins    ) {
        this.eventType = eventType;
        this.time = time;
        this.volunteer = volunteer;
        this.admin = admin;
        this.participantAmount = participantAmount;
        this.date = date;
        this.category = category;
        this.nomarlUser = nomarlUser;
        this.description = description;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
        this.admins = admins;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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