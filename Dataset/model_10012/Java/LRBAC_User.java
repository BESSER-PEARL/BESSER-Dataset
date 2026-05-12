





import java.util.List;
import java.util.ArrayList;

public class LRBAC_User  {

    private String UserName;
    private int Age;
    private int UserID;
    private String Gender;





    private LRBAC_Session lrbac_session;




    private List<LRBAC_Session> lrbac_sessions;




    private LRBAC_Role lrbac_role;




    private List<LRBAC_Role> lrbac_roles;


    public LRBAC_User(
        String UserName,        int Age,        int UserID,        String Gender    ) {
        this.UserName = UserName;
        this.Age = Age;
        this.UserID = UserID;
        this.Gender = Gender;
        this.lrbac_sessions = new ArrayList<>();
        this.lrbac_roles = new ArrayList<>();
    }

    public LRBAC_User(
        String UserName,        int Age,        int UserID,        String Gender        ArrayList<LRBAC_Session> lrbac_sessions,        ArrayList<LRBAC_Role> lrbac_roles    ) {
        this.UserName = UserName;
        this.Age = Age;
        this.UserID = UserID;
        this.Gender = Gender;
        this.lrbac_sessions = lrbac_sessions;
        this.lrbac_roles = lrbac_roles;
    }

    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }

    public LRBAC_Session getLrbac_session() {
        return lrbac_session;
    }

    public void setLrbac_session(LRBAC_Session lrbac_session) {
        this.lrbac_session = lrbac_session;
    }
    public List<LRBAC_Session> getLrbac_sessions() {
        return lrbac_sessions;
    }

    public void addLrbac_session(Lrbac_session lrbac_session) {
        this.lrbac_sessions.add(lrbac_session);
    }
    public LRBAC_Role getLrbac_role() {
        return lrbac_role;
    }

    public void setLrbac_role(LRBAC_Role lrbac_role) {
        this.lrbac_role = lrbac_role;
    }
    public List<LRBAC_Role> getLrbac_roles() {
        return lrbac_roles;
    }

    public void addLrbac_role(Lrbac_role lrbac_role) {
        this.lrbac_roles.add(lrbac_role);
    }

}