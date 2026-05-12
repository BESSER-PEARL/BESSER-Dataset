





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private None User;
    private int ActivitySubType;
    private int ActivityType;
    private int ActivityID;
    private None Project;
    private String NewValue;
    private String PrevValue;
    private boolean Seen;





    private Project project;




    private User user;


    public Activity(
        None User,        int ActivitySubType,        int ActivityType,        int ActivityID,        None Project,        String NewValue,        String PrevValue,        boolean Seen    ) {
        this.User = User;
        this.ActivitySubType = ActivitySubType;
        this.ActivityType = ActivityType;
        this.ActivityID = ActivityID;
        this.Project = Project;
        this.NewValue = NewValue;
        this.PrevValue = PrevValue;
        this.Seen = Seen;
    }


    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }
    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
    }
    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public String getNewvalue() {
        return NewValue;
    }

    public void setNewvalue(String NewValue) {
        this.NewValue = NewValue;
    }
    public String getPrevvalue() {
        return PrevValue;
    }

    public void setPrevvalue(String PrevValue) {
        this.PrevValue = PrevValue;
    }
    public boolean getSeen() {
        return Seen;
    }

    public void setSeen(boolean Seen) {
        this.Seen = Seen;
    }

    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}