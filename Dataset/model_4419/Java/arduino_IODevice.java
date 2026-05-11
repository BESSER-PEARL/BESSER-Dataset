





import java.util.List;
import java.util.ArrayList;

public class arduino_IODevice extends AbstractDevice {

    private boolean analog;
    private boolean pullup;



    public arduino_IODevice(
        boolean analog,        boolean pullup    ) {
        super(
        );
        this.analog = analog;
        this.pullup = pullup;
    }


    public boolean getAnalog() {
        return analog;
    }

    public void setAnalog(boolean analog) {
        this.analog = analog;
    }
    public boolean getPullup() {
        return pullup;
    }

    public void setPullup(boolean pullup) {
        this.pullup = pullup;
    }


}