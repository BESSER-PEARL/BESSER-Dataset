





import java.util.List;
import java.util.ArrayList;

public class Variable  {






    private ocl_expressions_LetExp ocl_expressions_letexp;




    private ocl_expressions_LoopExp ocl_expressions_loopexp;




    private ocl_expressions_IterateExp ocl_expressions_iterateexp;




    private ocl_expressions_VariableExp ocl_expressions_variableexp;


    public Variable(
    ) {
    }



    public ocl_expressions_LetExp getOcl_expressions_letexp() {
        return ocl_expressions_letexp;
    }

    public void setOcl_expressions_letexp(ocl_expressions_LetExp ocl_expressions_letexp) {
        this.ocl_expressions_letexp = ocl_expressions_letexp;
    }
    public ocl_expressions_LoopExp getOcl_expressions_loopexp() {
        return ocl_expressions_loopexp;
    }

    public void setOcl_expressions_loopexp(ocl_expressions_LoopExp ocl_expressions_loopexp) {
        this.ocl_expressions_loopexp = ocl_expressions_loopexp;
    }
    public ocl_expressions_IterateExp getOcl_expressions_iterateexp() {
        return ocl_expressions_iterateexp;
    }

    public void setOcl_expressions_iterateexp(ocl_expressions_IterateExp ocl_expressions_iterateexp) {
        this.ocl_expressions_iterateexp = ocl_expressions_iterateexp;
    }
    public ocl_expressions_VariableExp getOcl_expressions_variableexp() {
        return ocl_expressions_variableexp;
    }

    public void setOcl_expressions_variableexp(ocl_expressions_VariableExp ocl_expressions_variableexp) {
        this.ocl_expressions_variableexp = ocl_expressions_variableexp;
    }

}