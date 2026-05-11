





import java.util.List;
import java.util.ArrayList;

public class b_BoolLiteral extends Arg, ReturnExpr, Condition {

    private String value;
    private String constant;



    public b_BoolLiteral(
        String value,        String constant    ) {
        super(
        );
        this.value = value;
        this.constant = constant;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}