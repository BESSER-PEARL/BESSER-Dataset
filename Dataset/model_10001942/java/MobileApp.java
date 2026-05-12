





import java.util.List;
import java.util.ArrayList;

public class MobileApp  {

    private int UserID;
    private int AlarmID;





    private Firebase firebase;


    public MobileApp(
        int UserID,        int AlarmID    ) {
        this.UserID = UserID;
        this.AlarmID = AlarmID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getAlarmid() {
        return AlarmID;
    }

    public void setAlarmid(int AlarmID) {
        this.AlarmID = AlarmID;
    }

    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }

}