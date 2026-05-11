





import java.util.List;
import java.util.ArrayList;

public class dbl_PropertyBindingExpr extends NamedElement, RhsExpression {

    private String operator;



    public dbl_PropertyBindingExpr(
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