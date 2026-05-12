





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private None Project;
    private int ActivityType;
    private boolean Seen;
    private String NewValue;
    private int ActivityID;
    private int ActivitySubType;
    private String PrevValue;
    private None User;





    private User user;




    private Project project;


    public Activity(
        None Project,        int ActivityType,        boolean Seen,        String NewValue,        int ActivityID,        int ActivitySubType,        String PrevValue,        None User    ) {
        this.Project = Project;
        this.ActivityType = ActivityType;
        this.Seen = Seen;
        this.NewValue = NewValue;
        this.ActivityID = ActivityID;
        this.ActivitySubType = ActivitySubType;
        this.PrevValue = PrevValue;
        this.User = User;
    }


    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
    }
    public boolean getSeen() {
        return Seen;
    }

    public void setSeen(boolean Seen) {
        this.Seen = Seen;
    }
    public String getNewvalue() {
        return NewValue;
    }

    public void setNewvalue(String NewValue) {
        this.NewValue = NewValue;
    }
    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }
    public String getPrevvalue() {
        return PrevValue;
    }

    public void setPrevvalue(String PrevValue) {
        this.PrevValue = PrevValue;
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