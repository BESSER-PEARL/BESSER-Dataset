





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private String PrevValue;
    private None User;
    private int ActivityID;
    private String NewValue;
    private boolean Seen;
    private int ActivitySubType;
    private None Project;
    private int ActivityType;





    private Project project;




    private User user;


    public Activity(
        String PrevValue,        None User,        int ActivityID,        String NewValue,        boolean Seen,        int ActivitySubType,        None Project,        int ActivityType    ) {
        this.PrevValue = PrevValue;
        this.User = User;
        this.ActivityID = ActivityID;
        this.NewValue = NewValue;
        this.Seen = Seen;
        this.ActivitySubType = ActivitySubType;
        this.Project = Project;
        this.ActivityType = ActivityType;
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
    public boolean getSeen() {
        return Seen;
    }

    public void setSeen(boolean Seen) {
        this.Seen = Seen;
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
    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
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