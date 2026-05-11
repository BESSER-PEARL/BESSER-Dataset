





import java.util.List;
import java.util.ArrayList;

public class House2_RainSensor extends Sensor {

    private boolean active;



    public House2_RainSensor(
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