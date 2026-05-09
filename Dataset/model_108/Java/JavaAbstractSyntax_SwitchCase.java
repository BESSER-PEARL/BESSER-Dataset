





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SwitchCase extends Statement {

    private String default;





    private Expression expression;


    public JavaAbstractSyntax_SwitchCase(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}