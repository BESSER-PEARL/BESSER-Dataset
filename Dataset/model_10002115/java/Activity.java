





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityID;
    private String NewValue;
    private int ActivityType;
    private None Project;
    private String PrevValue;
    private int ActivitySubType;
    private boolean Seen;
    private None User;





    private User user;




    private Project project;


    public Activity(
        int ActivityID,        String NewValue,        int ActivityType,        None Project,        String PrevValue,        int ActivitySubType,        boolean Seen,        None User    ) {
        this.ActivityID = ActivityID;
        this.NewValue = NewValue;
        this.ActivityType = ActivityType;
        this.Project = Project;
        this.PrevValue = PrevValue;
        this.ActivitySubType = ActivitySubType;
        this.Seen = Seen;
        this.User = User;
    }


    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }
    public String getNewvalue() {
        return NewValue;
    }

    public void setNewvalue(String NewValue) {
        this.NewValue = NewValue;
    }
    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public String getPrevvalue() {
        return PrevValue;
    }

    public void setPrevvalue(String PrevValue) {
        this.PrevValue = PrevValue;
    }
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }
    public boolean getSeen() {
        return Seen;
    }

    public void setSeen(boolean Seen) {
        this.Seen = Seen;
    }
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }

}