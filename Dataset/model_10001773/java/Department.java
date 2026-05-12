





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String name;





    private Fire_Alarm_system fire_alarm_system;


    public Department(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Fire_Alarm_system getFire_alarm_system() {
        return fire_alarm_system;
    }

    public void setFire_alarm_system(Fire_Alarm_system fire_alarm_system) {
        this.fire_alarm_system = fire_alarm_system;
    }

}