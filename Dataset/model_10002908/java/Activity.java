





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityType;
    private int ActivitySubType;
    private String NewValue;
    private String PrevValue;
    private boolean Seen;
    private int ActivityID;
    private None User;
    private None Project;





    private User user;




    private Project project;


    public Activity(
        int ActivityType,        int ActivitySubType,        String NewValue,        String PrevValue,        boolean Seen,        int ActivityID,        None User,        None Project    ) {
        this.ActivityType = ActivityType;
        this.ActivitySubType = ActivitySubType;
        this.NewValue = NewValue;
        this.PrevValue = PrevValue;
        this.Seen = Seen;
        this.ActivityID = ActivityID;
        this.User = User;
        this.Project = Project;
    }


    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
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
    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
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