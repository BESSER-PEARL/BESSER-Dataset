





import java.util.List;
import java.util.ArrayList;

public class esmodel_ServerSpace  {






    private List<ProjectHistory> projecthistorys;




    private List<SessionId> sessionids;




    private List<accesscontrol_ACUser> accesscontrol_acusers;


    public esmodel_ServerSpace(
    ) {
        this.projecthistorys = new ArrayList<>();
        this.sessionids = new ArrayList<>();
        this.accesscontrol_acusers = new ArrayList<>();
    }

    public esmodel_ServerSpace(
        ArrayList<ProjectHistory> projecthistorys,        ArrayList<SessionId> sessionids,        ArrayList<accesscontrol_ACUser> accesscontrol_acusers    ) {
        this.projecthistorys = projecthistorys;
        this.sessionids = sessionids;
        this.accesscontrol_acusers = accesscontrol_acusers;
    }


    public List<ProjectHistory> getProjecthistorys() {
        return projecthistorys;
    }

    public void addProjecthistory(Projecthistory projecthistory) {
        this.projecthistorys.add(projecthistory);
    }
    public List<SessionId> getSessionids() {
        return sessionids;
    }

    public void addSessionid(Sessionid sessionid) {
        this.sessionids.add(sessionid);
    }
    public List<accesscontrol_ACUser> getAccesscontrol_acusers() {
        return accesscontrol_acusers;
    }

    public void addAccesscontrol_acuser(Accesscontrol_acuser accesscontrol_acuser) {
        this.accesscontrol_acusers.add(accesscontrol_acuser);
    }

}