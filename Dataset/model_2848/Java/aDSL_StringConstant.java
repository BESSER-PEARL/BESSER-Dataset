





import java.util.List;
import java.util.ArrayList;

public class aDSL_StringConstant extends Expression {

    private String value;



    public aDSL_StringConstant(
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