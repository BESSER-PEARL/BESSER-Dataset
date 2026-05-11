





import java.util.List;
import java.util.ArrayList;

public class mindstorms_TouchSensor extends Sensor {

    private boolean isPressed;



    public mindstorms_TouchSensor(
        boolean isPressed    ) {
        super(
        );
        this.isPressed = isPressed;
    }


    public boolean getIspressed() {
        return isPressed;
    }

    public void setIspressed(boolean isPressed) {
        this.isPressed = isPressed;
    }


}