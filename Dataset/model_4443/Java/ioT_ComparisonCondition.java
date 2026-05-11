





import java.util.List;
import java.util.ArrayList;

public class ioT_ComparisonCondition extends Condition {

    private String operator;



    public ioT_ComparisonCondition(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}