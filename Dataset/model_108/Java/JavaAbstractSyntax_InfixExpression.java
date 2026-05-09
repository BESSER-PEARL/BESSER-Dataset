





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_InfixExpression extends Expression {

    private String operator;



    public JavaAbstractSyntax_InfixExpression(
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