





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_IterateExp extends LoopExp {






    private OclExpression oclexpression;




    private ocl_ir_VariableDeclaration ocl_ir_variabledeclaration;


    public ir_ocl_IterateExp(
    ) {
        super(
        );
    }



    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public ocl_ir_VariableDeclaration getOcl_ir_variabledeclaration() {
        return ocl_ir_variabledeclaration;
    }

    public void setOcl_ir_variabledeclaration(ocl_ir_VariableDeclaration ocl_ir_variabledeclaration) {
        this.ocl_ir_variabledeclaration = ocl_ir_variabledeclaration;
    }

}