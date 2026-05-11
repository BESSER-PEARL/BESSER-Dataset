





import java.util.List;
import java.util.ArrayList;

public class gremlin_ReturnStatement extends Instruction {

    private String value;



    public gremlin_ReturnStatement(
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