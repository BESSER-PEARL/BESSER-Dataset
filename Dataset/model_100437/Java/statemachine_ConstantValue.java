





import java.util.List;
import java.util.ArrayList;

public class statemachine_ConstantValue extends Value {

    private String value;



    public statemachine_ConstantValue(
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