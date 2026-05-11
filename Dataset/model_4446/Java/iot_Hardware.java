





import java.util.List;
import java.util.ArrayList;

public class iot_Hardware extends Component {

    private int pinNumber;
    private boolean mode;
    private String type;
    private int timeInterval;



    public iot_Hardware(
        int pinNumber,        boolean mode,        String type,        int timeInterval    ) {
        super(
        );
        this.pinNumber = pinNumber;
        this.mode = mode;
        this.type = type;
        this.timeInterval = timeInterval;
    }


    public int getPinnumber() {
        return pinNumber;
    }

    public void setPinnumber(int pinNumber) {
        this.pinNumber = pinNumber;
    }
    public boolean getMode() {
        return mode;
    }

    public void setMode(boolean mode) {
        this.mode = mode;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getTimeinterval() {
        return timeInterval;
    }

    public void setTimeinterval(int timeInterval) {
        this.timeInterval = timeInterval;
    }


}