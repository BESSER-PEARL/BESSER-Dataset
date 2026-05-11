





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_VariableDeclaration extends declaration_Declaration, type_TypedElement {

    private boolean constant;
    private boolean default;
    private boolean notnull;





    private Expression expression;


    public plsql_declaration_VariableDeclaration(
        boolean constant,        boolean default,        boolean notnull    ) {
        super(
        );
        this.constant = constant;
        this.default = default;
        this.notnull = notnull;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
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