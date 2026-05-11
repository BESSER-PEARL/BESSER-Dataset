





import java.util.List;
import java.util.ArrayList;

public class mil_PrtInstruction extends Instruction {

    private String value;



    public mil_PrtInstruction(
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