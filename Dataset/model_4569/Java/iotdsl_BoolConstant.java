





import java.util.List;
import java.util.ArrayList;

public class iotdsl_BoolConstant extends Value {

    private String value;



    public iotdsl_BoolConstant(
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