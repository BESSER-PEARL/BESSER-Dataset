





import java.util.List;
import java.util.ArrayList;

public class Activity  {

    private int ActivityType;
    private String User;
    private String PrevValue;
    private String NewValue;
    private boolean Seen;
    private int ActivityID;
    private String Project;
    private int ActivitySubType;



    public Activity(
        int ActivityType,        String User,        String PrevValue,        String NewValue,        boolean Seen,        int ActivityID,        String Project,        int ActivitySubType    ) {
        this.ActivityType = ActivityType;
        this.User = User;
        this.PrevValue = PrevValue;
        this.NewValue = NewValue;
        this.Seen = Seen;
        this.ActivityID = ActivityID;
        this.Project = Project;
        this.ActivitySubType = ActivitySubType;
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
    public String getProject() {
        return Project;
    }

    public void setProject(String Project) {
        this.Project = Project;
    }
    public int getActivitysubtype() {
        return ActivitySubType;
    }

    public void setActivitysubtype(int ActivitySubType) {
        this.ActivitySubType = ActivitySubType;
    }


}