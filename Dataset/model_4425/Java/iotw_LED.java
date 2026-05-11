





import java.util.List;
import java.util.ArrayList;

public class iotw_LED extends OutputControl {

    private String pin2;
    private String pin1;



    public iotw_LED(
        String pin2,        String pin1    ) {
        super(
        );
        this.pin2 = pin2;
        this.pin1 = pin1;
    }


    public String getPin2() {
        return pin2;
    }

    public void setPin2(String pin2) {
        this.pin2 = pin2;
    }
    public String getPin1() {
        return pin1;
    }

    public void setPin1(String pin1) {
        this.pin1 = pin1;
    }


}