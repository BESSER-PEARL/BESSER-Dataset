





import java.util.List;
import java.util.ArrayList;

public class arduino_Delay extends Instruction {

    private String value;



    public arduino_Delay(
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