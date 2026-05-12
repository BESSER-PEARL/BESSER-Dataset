





import java.util.List;
import java.util.ArrayList;

public class Alarm  {

    private String AlarmID;





    private ViewTemp_Smoke viewtemp_smoke;




    private Notification notification;




    private TurnDownAlarm turndownalarm;




    private MobileApp mobileapp;




    private AddAlarm addalarm;


    public Alarm(
        String AlarmID    ) {
        this.AlarmID = AlarmID;
    }


    public String getAlarmid() {
        return AlarmID;
    }

    public void setAlarmid(String AlarmID) {
        this.AlarmID = AlarmID;
    }

    public ViewTemp_Smoke getViewtemp_smoke() {
        return viewtemp_smoke;
    }

    public void setViewtemp_smoke(ViewTemp_Smoke viewtemp_smoke) {
        this.viewtemp_smoke = viewtemp_smoke;
    }
    public Notification getNotification() {
        return notification;
    }

    public void setNotification(Notification notification) {
        this.notification = notification;
    }
    public TurnDownAlarm getTurndownalarm() {
        return turndownalarm;
    }

    public void setTurndownalarm(TurnDownAlarm turndownalarm) {
        this.turndownalarm = turndownalarm;
    }
    public MobileApp getMobileapp() {
        return mobileapp;
    }

    public void setMobileapp(MobileApp mobileapp) {
        this.mobileapp = mobileapp;
    }
    public AddAlarm getAddalarm() {
        return addalarm;
    }

    public void setAddalarm(AddAlarm addalarm) {
        this.addalarm = addalarm;
    }

}