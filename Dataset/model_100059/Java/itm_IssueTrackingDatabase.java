





import java.util.List;
import java.util.ArrayList;

public class itm_IssueTrackingDatabase  {






    private List<itm_Tracker> itm_trackers;




    private List<itm_Project> itm_projects;




    private List<itm_Role> itm_roles;




    private List<itm_User> itm_users;


    public itm_IssueTrackingDatabase(
    ) {
        this.itm_trackers = new ArrayList<>();
        this.itm_projects = new ArrayList<>();
        this.itm_roles = new ArrayList<>();
        this.itm_users = new ArrayList<>();
    }

    public itm_IssueTrackingDatabase(
        ArrayList<itm_Tracker> itm_trackers,        ArrayList<itm_Project> itm_projects,        ArrayList<itm_Role> itm_roles,        ArrayList<itm_User> itm_users    ) {
        this.itm_trackers = itm_trackers;
        this.itm_projects = itm_projects;
        this.itm_roles = itm_roles;
        this.itm_users = itm_users;
    }


    public List<itm_Tracker> getItm_trackers() {
        return itm_trackers;
    }

    public void addItm_tracker(Itm_tracker itm_tracker) {
        this.itm_trackers.add(itm_tracker);
    }
    public List<itm_Project> getItm_projects() {
        return itm_projects;
    }

    public void addItm_project(Itm_project itm_project) {
        this.itm_projects.add(itm_project);
    }
    public List<itm_Role> getItm_roles() {
        return itm_roles;
    }

    public void addItm_role(Itm_role itm_role) {
        this.itm_roles.add(itm_role);
    }
    public List<itm_User> getItm_users() {
        return itm_users;
    }

    public void addItm_user(Itm_user itm_user) {
        this.itm_users.add(itm_user);
    }

}