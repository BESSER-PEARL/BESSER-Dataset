





import java.util.List;
import java.util.ArrayList;

public class urml_Variable extends StatementOperation, Statement {

    private boolean assign;





    private urml_Expression urml_expression;




    private urml_LocalVar urml_localvar;


    public urml_Variable(
        boolean assign    ) {
        super(
        );
        this.assign = assign;
    }


    public boolean getAssign() {
        return assign;
    }

    public void setAssign(boolean assign) {
        this.assign = assign;
    }

    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }
    public urml_LocalVar getUrml_localvar() {
        return urml_localvar;
    }

    public void setUrml_localvar(urml_LocalVar urml_localvar) {
        this.urml_localvar = urml_localvar;
    }

}