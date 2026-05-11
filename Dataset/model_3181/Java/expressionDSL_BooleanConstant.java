





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_BooleanConstant extends Expression {

    private String value;



    public expressionDSL_BooleanConstant(
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