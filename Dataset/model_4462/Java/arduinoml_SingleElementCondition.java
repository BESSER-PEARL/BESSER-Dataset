





import java.util.List;
import java.util.ArrayList;

public class arduinoml_SingleElementCondition extends Condition {

    private String value;



    public arduinoml_SingleElementCondition(
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