





import java.util.List;
import java.util.ArrayList;

public class odemcustom_PropertyBindingExpr extends RhsExpression, NamedElement {

    private String operator;



    public odemcustom_PropertyBindingExpr(
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