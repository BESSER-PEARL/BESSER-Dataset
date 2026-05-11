





import java.util.List;
import java.util.ArrayList;

public class arduinoML_StringSignal extends Signal {

    private String value;



    public arduinoML_StringSignal(
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