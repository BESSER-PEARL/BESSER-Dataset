





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_VariableDeclaration extends type_TypedElement, declaration_Declaration {

    private boolean default;
    private boolean constant;
    private boolean notnull;





    private Expression expression;


    public plsql_declaration_VariableDeclaration(
        boolean default,        boolean constant,        boolean notnull    ) {
        super(
        );
        this.default = default;
        this.constant = constant;
        this.notnull = notnull;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public boolean getNotnull() {
        return notnull;
    }

    public void setNotnull(boolean notnull) {
        this.notnull = notnull;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}