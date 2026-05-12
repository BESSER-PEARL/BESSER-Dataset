





import java.util.List;
import java.util.ArrayList;

public class HomeAppliances  {

    private int HAID;





    private Fans fans;




    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;




    private Light light;




    private Door door;


    public HomeAppliances(
        int HAID    ) {
        this.HAID = HAID;
    }


    public int getHaid() {
        return HAID;
    }

    public void setHaid(int HAID) {
        this.HAID = HAID;
    }

    public Fans getFans() {
        return fans;
    }

    public void setFans(Fans fans) {
        this.fans = fans;
    }
    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }
    public Light getLight() {
        return light;
    }

    public void setLight(Light light) {
        this.light = light;
    }
    public Door getDoor() {
        return door;
    }

    public void setDoor(Door door) {
        this.door = door;
    }

}