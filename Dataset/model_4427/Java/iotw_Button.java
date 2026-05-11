





import java.util.List;
import java.util.ArrayList;

public class iotw_Button extends InputDevice {

    private String pin1;



    public iotw_Button(
        String pin1    ) {
        super(
        );
        this.pin1 = pin1;
    }


    public String getPin1() {
        return pin1;
    }

    public void setPin1(String pin1) {
        this.pin1 = pin1;
    }


}