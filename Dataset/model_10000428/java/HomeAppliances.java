





import java.util.List;
import java.util.ArrayList;

public class HomeAppliances  {

    private int HAID;





    private List<Lights> lightss;




    private List<Fans> fanss;




    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;


    public HomeAppliances(
        int HAID    ) {
        this.HAID = HAID;
        this.lightss = new ArrayList<>();
        this.fanss = new ArrayList<>();
    }

    public HomeAppliances(
        int HAID        ArrayList<Lights> lightss,        ArrayList<Fans> fanss    ) {
        this.HAID = HAID;
        this.lightss = lightss;
        this.fanss = fanss;
    }

    public int getHaid() {
        return HAID;
    }

    public void setHaid(int HAID) {
        this.HAID = HAID;
    }

    public List<Lights> getLightss() {
        return lightss;
    }

    public void addLights(Lights lights) {
        this.lightss.add(lights);
    }
    public List<Fans> getFanss() {
        return fanss;
    }

    public void addFans(Fans fans) {
        this.fanss.add(fans);
    }
    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }

}