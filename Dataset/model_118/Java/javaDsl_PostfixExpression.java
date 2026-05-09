





import java.util.List;
import java.util.ArrayList;

public class javaDsl_PostfixExpression extends NoArrayExpressionWithoutMinus, StatementExpression {

    private String reference;
    private String operators;



    public javaDsl_PostfixExpression(
        String reference,        String operators    ) {
        super(
        );
        this.reference = reference;
        this.operators = operators;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }


}