





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private None User;
    private int ActivityID;
    private String PrevValue;
    private String NewValue;
    private None Project;
    private boolean Seen;
    private int ActivitySubType;
    private int ActivityType;





    private User user;




    private Project project;


    public Activity(
        None User,        int ActivityID,        String PrevValue,        String NewValue,        None Project,        boolean Seen,        int ActivitySubType,        int ActivityType    ) {
        this.User = User;
        this.ActivityID = ActivityID;
        this.PrevValue = PrevValue;
        this.NewValue = NewValue;
        this.Project = Project;
        this.Seen = Seen;
        this.ActivitySubType = ActivitySubType;
        this.ActivityType = ActivityType;
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