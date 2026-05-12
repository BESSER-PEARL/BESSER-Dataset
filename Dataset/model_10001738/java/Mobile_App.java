





import java.util.List;
import java.util.ArrayList;

public class Mobile_App  {

    private int AlarmID;
    private int UserID;





    private Firebase firebase;


    public Mobile_App(
        int AlarmID,        int UserID    ) {
        this.AlarmID = AlarmID;
        this.UserID = UserID;
    }


    public int getAlarmid() {
        return AlarmID;
    }

    public void setAlarmid(int AlarmID) {
        this.AlarmID = AlarmID;
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