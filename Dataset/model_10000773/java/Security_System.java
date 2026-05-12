





import java.util.List;
import java.util.ArrayList;

public class Security_System  {

    private int UserID;





    private System system;


    public Security_System(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}