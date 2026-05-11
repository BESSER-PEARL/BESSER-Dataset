





import java.util.List;
import java.util.ArrayList;

public class dbl_ExpansionStatement extends SimpleStatement {

    private boolean variableContext;
    private boolean functionContext;
    private boolean classContext;



    public dbl_ExpansionStatement(
        boolean variableContext,        boolean functionContext,        boolean classContext    ) {
        super(
        );
        this.variableContext = variableContext;
        this.functionContext = functionContext;
        this.classContext = classContext;
    }


    public boolean getVariablecontext() {
        return variableContext;
    }

    public void setVariablecontext(boolean variableContext) {
        this.variableContext = variableContext;
    }
    public boolean getFunctioncontext() {
        return functionContext;
    }

    public void setFunctioncontext(boolean functionContext) {
        this.functionContext = functionContext;
    }
    public boolean getClasscontext() {
        return classContext;
    }

    public void setClasscontext(boolean classContext) {
        this.classContext = classContext;
    }


}