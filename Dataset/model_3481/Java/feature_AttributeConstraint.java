





import java.util.List;
import java.util.ArrayList;

public class feature_AttributeConstraint extends Constraint {

    private String operator;



    public feature_AttributeConstraint(
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