





import java.util.List;
import java.util.ArrayList;

public class dbl_ExpansionStatement extends SimpleStatement {

    private boolean functionContext;
    private boolean variableContext;
    private boolean classContext;





    private List<dbl_Expression> dbl_expressions;




    private dbl_IdExpr dbl_idexpr;


    public dbl_ExpansionStatement(
        boolean functionContext,        boolean variableContext,        boolean classContext    ) {
        super(
        );
        this.functionContext = functionContext;
        this.variableContext = variableContext;
        this.classContext = classContext;
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_ExpansionStatement(
        boolean functionContext,        boolean variableContext,        boolean classContext        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.functionContext = functionContext;
        this.variableContext = variableContext;
        this.classContext = classContext;
        this.dbl_expressions = dbl_expressions;
    }

    public boolean getFunctioncontext() {
        return functionContext;
    }

    public void setFunctioncontext(boolean functionContext) {
        this.functionContext = functionContext;
    }
    public boolean getVariablecontext() {
        return variableContext;
    }

    public void setVariablecontext(boolean variableContext) {
        this.variableContext = variableContext;
    }
    public boolean getClasscontext() {
        return classContext;
    }

    public void setClasscontext(boolean classContext) {
        this.classContext = classContext;
    }

    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }
    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }

}