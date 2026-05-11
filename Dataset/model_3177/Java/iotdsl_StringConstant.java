





import java.util.List;
import java.util.ArrayList;

public class iotdsl_StringConstant extends Expression {

    private String value;



    public iotdsl_StringConstant(
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