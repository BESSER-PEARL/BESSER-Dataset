





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private String PrevValue;
    private String NewValue;
    private int ActivityType;
    private int ActivitySubType;
    private None Project;
    private boolean Seen;
    private None User;
    private int ActivityID;





    private Project project;




    private User user;


    public Activity(
        String PrevValue,        String NewValue,        int ActivityType,        int ActivitySubType,        None Project,        boolean Seen,        None User,        int ActivityID    ) {
        this.PrevValue = PrevValue;
        this.NewValue = NewValue;
        this.ActivityType = ActivityType;
        this.ActivitySubType = ActivitySubType;
        this.Project = Project;
        this.Seen = Seen;
        this.User = User;
        this.ActivityID = ActivityID;
    }


    public String getPrevvalue() {
        return PrevValue;
    }

    public void setPrevvalue(String PrevValue) {
        this.PrevValue = PrevValue;
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
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
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
    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
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