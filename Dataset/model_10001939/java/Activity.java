





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityType;
    private String User;
    private boolean Seen;
    private int ActivitySubType;
    private String PrevValue;
    private String NewValue;
    private String Project;
    private int ActivityID;



    public Activity(
        int ActivityType,        String User,        boolean Seen,        int ActivitySubType,        String PrevValue,        String NewValue,        String Project,        int ActivityID    ) {
        this.ActivityType = ActivityType;
        this.User = User;
        this.Seen = Seen;
        this.ActivitySubType = ActivitySubType;
        this.PrevValue = PrevValue;
        this.NewValue = NewValue;
        this.Project = Project;
        this.ActivityID = ActivityID;
    }


    public int getActivitytype() {
        return ActivityType;
    }

    public void setActivitytype(int ActivityType) {
        this.ActivityType = ActivityType;
    }
    public String getUser() {
        return User;
    }

    public void setUser(String User) {
        this.User = User;
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
    public String getProject() {
        return Project;
    }

    public void setProject(String Project) {
        this.Project = Project;
    }
    public int getActivityid() {
        return ActivityID;
    }

    public void setActivityid(int ActivityID) {
        this.ActivityID = ActivityID;
    }


}