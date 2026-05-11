





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_RelationalExpression extends Expression {

    private String operator;



    public CompleteDSLPckg_RelationalExpression(
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