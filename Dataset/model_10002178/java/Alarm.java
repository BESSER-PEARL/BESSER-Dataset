





import java.util.List;
import java.util.ArrayList;

public class Alarm  {






    private TurnDownAlarm turndownalarm;




    private AddAlarm addalarm;




    private Notification notification;




    private ViewTemp_Smoke viewtemp_smoke;




    private MobileApp mobileapp;


    public Alarm(
    ) {
    }



    public TurnDownAlarm getTurndownalarm() {
        return turndownalarm;
    }

    public void setTurndownalarm(TurnDownAlarm turndownalarm) {
        this.turndownalarm = turndownalarm;
    }
    public AddAlarm getAddalarm() {
        return addalarm;
    }

    public void setAddalarm(AddAlarm addalarm) {
        this.addalarm = addalarm;
    }
    public Notification getNotification() {
        return notification;
    }

    public void setNotification(Notification notification) {
        this.notification = notification;
    }
    public ViewTemp_Smoke getViewtemp_smoke() {
        return viewtemp_smoke;
    }

    public void setViewtemp_smoke(ViewTemp_Smoke viewtemp_smoke) {
        this.viewtemp_smoke = viewtemp_smoke;
    }
    public MobileApp getMobileapp() {
        return mobileapp;
    }

    public void setMobileapp(MobileApp mobileapp) {
        this.mobileapp = mobileapp;
    }

}