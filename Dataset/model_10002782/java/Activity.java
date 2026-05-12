





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityID;
    private int ActivityType;
    private None User;
    private String PrevValue;
    private boolean Seen;
    private None Project;
    private int ActivitySubType;
    private String NewValue;





    private User user;




    private Project project;


    public Activity(
        int ActivityID,        int ActivityType,        None User,        String PrevValue,        boolean Seen,        None Project,        int ActivitySubType,        String NewValue    ) {
        this.ActivityID = ActivityID;
        this.ActivityType = ActivityType;
        this.User = User;
        this.PrevValue = PrevValue;
        this.Seen = Seen;
        this.Project = Project;
        this.ActivitySubType = ActivitySubType;
        this.NewValue = NewValue;
    }


    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }
    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
    }
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
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
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }
    public String getNewvalue() {
        return NewValue;
    }

    public void setNewvalue(String NewValue) {
        this.NewValue = NewValue;
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