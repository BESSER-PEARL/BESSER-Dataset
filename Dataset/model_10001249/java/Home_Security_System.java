





import java.util.List;
import java.util.ArrayList;

public class Home_Security_System  {

    private int UserID;





    private Smart_mirror smart_mirror;


    public Home_Security_System(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public Smart_mirror getSmart_mirror() {
        return smart_mirror;
    }

    public void setSmart_mirror(Smart_mirror smart_mirror) {
        this.smart_mirror = smart_mirror;
    }

}