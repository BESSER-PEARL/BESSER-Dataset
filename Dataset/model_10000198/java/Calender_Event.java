





import java.util.List;
import java.util.ArrayList;

public class Calender_Event  {

    private None admin;
    private String start_date;
    private None volunteer;
    private None nomarlUser;
    private String end_date;
    private String description;
    private String time;
    private String participantAmount;
    private String category;
    private String eventType;





    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;




    private Normal_user normal_user;




    private List<Admin> admins;


    public Calender_Event(
        None admin,        String start_date,        None volunteer,        None nomarlUser,        String end_date,        String description,        String time,        String participantAmount,        String category,        String eventType    ) {
        this.admin = admin;
        this.start_date = start_date;
        this.volunteer = volunteer;
        this.nomarlUser = nomarlUser;
        this.end_date = end_date;
        this.description = description;
        this.time = time;
        this.participantAmount = participantAmount;
        this.category = category;
        this.eventType = eventType;
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Calender_Event(
        None admin,        String start_date,        None volunteer,        None nomarlUser,        String end_date,        String description,        String time,        String participantAmount,        String category,        String eventType        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins    ) {
        this.admin = admin;
        this.start_date = start_date;
        this.volunteer = volunteer;
        this.nomarlUser = nomarlUser;
        this.end_date = end_date;
        this.description = description;
        this.time = time;
        this.participantAmount = participantAmount;
        this.category = category;
        this.eventType = eventType;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
        this.admins = admins;
    }

    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getStart_date() {
        return start_date;
    }

    public void setStart_date(String start_date) {
        this.start_date = start_date;
    }
    public None getVolunteer() {
        return volunteer;
    }

    public void setVolunteer(None volunteer) {
        this.volunteer = volunteer;
    }
    public None getNomarluser() {
        return nomarlUser;
    }

    public void setNomarluser(None nomarlUser) {
        this.nomarlUser = nomarlUser;
    }
    public String getEnd_date() {
        return end_date;
    }

    public void setEnd_date(String end_date) {
        this.end_date = end_date;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
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
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}