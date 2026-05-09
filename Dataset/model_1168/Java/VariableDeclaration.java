





import java.util.List;
import java.util.ArrayList;

public class VariableDeclaration  {






    private top_OCL_OclType top_ocl_ocltype;




    private top_OCL_OclExpression top_ocl_oclexpression;




    private top_OCL_LetExp top_ocl_letexp;




    private top_OCL_VariableExp top_ocl_variableexp;


    public VariableDeclaration(
    ) {
    }



    public top_OCL_OclType getTop_ocl_ocltype() {
        return top_ocl_ocltype;
    }

    public void setTop_ocl_ocltype(top_OCL_OclType top_ocl_ocltype) {
        this.top_ocl_ocltype = top_ocl_ocltype;
    }
    public top_OCL_OclExpression getTop_ocl_oclexpression() {
        return top_ocl_oclexpression;
    }

    public void setTop_ocl_oclexpression(top_OCL_OclExpression top_ocl_oclexpression) {
        this.top_ocl_oclexpression = top_ocl_oclexpression;
    }
    public top_OCL_LetExp getTop_ocl_letexp() {
        return top_ocl_letexp;
    }

    public void setTop_ocl_letexp(top_OCL_LetExp top_ocl_letexp) {
        this.top_ocl_letexp = top_ocl_letexp;
    }
    public top_OCL_VariableExp getTop_ocl_variableexp() {
        return top_ocl_variableexp;
    }

    public void setTop_ocl_variableexp(top_OCL_VariableExp top_ocl_variableexp) {
        this.top_ocl_variableexp = top_ocl_variableexp;
    }

}