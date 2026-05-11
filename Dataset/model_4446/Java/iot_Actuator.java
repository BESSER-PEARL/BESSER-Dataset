





import java.util.List;
import java.util.ArrayList;

public class iot_Actuator extends Hardware {

    private boolean toggle;



    public iot_Actuator(
        boolean toggle    ) {
        super(
        );
        this.toggle = toggle;
    }


    public boolean getToggle() {
        return toggle;
    }

    public void setToggle(boolean toggle) {
        this.toggle = toggle;
    }


}