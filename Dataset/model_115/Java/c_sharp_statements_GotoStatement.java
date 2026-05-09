





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_GotoStatement extends JumpStatement {






    private Identifier identifier;




    private Case case;




    private Expression expression;




    private Default default;


    public c_sharp_statements_GotoStatement(
    ) {
        super(
        );
    }



    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public Case getCase() {
        return case;
    }

    public void setCase(Case case) {
        this.case = case;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public Default getDefault() {
        return default;
    }

    public void setDefault(Default default) {
        this.default = default;
    }

}