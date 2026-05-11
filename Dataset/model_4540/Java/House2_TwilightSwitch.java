





import java.util.List;
import java.util.ArrayList;

public class House2_TwilightSwitch extends Sensor {

    private boolean active;



    public House2_TwilightSwitch(
        boolean active    ) {
        super(
        );
        this.active = active;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}