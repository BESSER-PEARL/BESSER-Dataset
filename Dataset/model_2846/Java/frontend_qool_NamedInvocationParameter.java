





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_NamedInvocationParameter  {

    private String formalName;





    private Expression expression;


    public frontend_qool_NamedInvocationParameter(
        String formalName    ) {
        this.formalName = formalName;
    }


    public String getFormalname() {
        return formalName;
    }

    public void setFormalname(String formalName) {
        this.formalName = formalName;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}