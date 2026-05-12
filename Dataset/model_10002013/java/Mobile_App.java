





import java.util.List;
import java.util.ArrayList;

public class Mobile_App  {

    private int UserID;





    private Firebase firebase;


    public Mobile_App(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }

}