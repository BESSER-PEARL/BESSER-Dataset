





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_Argument extends type_TypedElement, declaration_NamedElement {

    private boolean in_;
    private boolean out;
    private boolean default;





    private Expression expression;


    public plsql_declaration_Argument(
        boolean in_,        boolean out,        boolean default    ) {
        super(
        );
        this.in_ = in_;
        this.out = out;
        this.default = default;
    }


    public boolean getIn_() {
        return in_;
    }

    public void setIn_(boolean in_) {
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

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}