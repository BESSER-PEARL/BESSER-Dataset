





import java.util.List;
import java.util.ArrayList;

public class Fire_Alarm_system  {

    private boolean system_On;
    private boolean system_Off;



    public Fire_Alarm_system(
        boolean system_On,        boolean system_Off    ) {
        this.system_On = system_On;
        this.system_Off = system_Off;
    }


    public boolean getSystem_on() {
        return system_On;
    }

    public void setSystem_on(boolean system_On) {
        this.system_On = system_On;
    }
    public boolean getSystem_off() {
        return system_Off;
    }

    public void setSystem_off(boolean system_Off) {
        this.system_Off = system_Off;
    }


}