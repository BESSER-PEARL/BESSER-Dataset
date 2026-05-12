





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityType;
    private boolean Seen;
    private String PrevValue;
    private None Project;
    private int ActivitySubType;
    private None User;
    private String NewValue;
    private int ActivityID;





    private User user;




    private Project project;


    public Activity(
        int ActivityType,        boolean Seen,        String PrevValue,        None Project,        int ActivitySubType,        None User,        String NewValue,        int ActivityID    ) {
        this.ActivityType = ActivityType;
        this.Seen = Seen;
        this.PrevValue = PrevValue;
        this.Project = Project;
        this.ActivitySubType = ActivitySubType;
        this.User = User;
        this.NewValue = NewValue;
        this.ActivityID = ActivityID;
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
    public String getPrevvalue() {
        return PrevValue;
    }

    public void setPrevvalue(String PrevValue) {
        this.PrevValue = PrevValue;
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
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
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