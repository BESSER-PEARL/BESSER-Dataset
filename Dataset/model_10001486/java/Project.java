





import java.util.List;
import java.util.ArrayList;

public class Project  {

    private String Info;
    private String State;
    private int Id;
    private String Access;
    private String Title;





    private User user;


    public Project(
        String Info,        String State,        int Id,        String Access,        String Title    ) {
        this.Info = Info;
        this.State = State;
        this.Id = Id;
        this.Access = Access;
        this.Title = Title;
    }


    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getAccess() {
        return Access;
    }

    public void setAccess(String Access) {
        this.Access = Access;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}