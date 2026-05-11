





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_Argument extends declaration_NamedElement, type_TypedElement {

    private boolean out;
    private boolean default;
    private boolean in_;





    private Expression expression;


    public plsql_declaration_Argument(
        boolean out,        boolean default,        boolean in_    ) {
        super(
        );
        this.out = out;
        this.default = default;
        this.in_ = in_;
    }


    public boolean getOut() {
        return out;
    }

    public void setOut(boolean out) {
        this.out = out;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public boolean getIn_() {
        return in_;
    }

    public void setIn_(boolean in_) {
        this.in_ = in_;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}