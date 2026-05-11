





import java.util.List;
import java.util.ArrayList;

public class arduinoML_DigitalSignal extends Signal {

    private String value;



    public arduinoML_DigitalSignal(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}