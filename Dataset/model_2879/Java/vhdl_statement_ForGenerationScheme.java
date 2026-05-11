





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_ForGenerationScheme extends GenerationScheme {

    private String variable;





    private Expression expression;


    public vhdl_statement_ForGenerationScheme(
        String variable    ) {
        super(
        );
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}