





import java.util.List;
import java.util.ArrayList;

public class arduino_PushButton extends ArduinoDigitalModule {

    private boolean isPushed;



    public arduino_PushButton(
        boolean isPushed    ) {
        super(
        );
        this.isPushed = isPushed;
    }


    public boolean getIspushed() {
        return isPushed;
    }

    public void setIspushed(boolean isPushed) {
        this.isPushed = isPushed;
    }


}