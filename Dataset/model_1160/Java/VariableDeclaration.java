





import java.util.List;
import java.util.ArrayList;

public class VariableDeclaration  {






    private genericity_dsl_BindingModel genericity_dsl_bindingmodel;




    private OCL_OclType ocl_ocltype;




    private OCL_OclExpression ocl_oclexpression;




    private OCL_LetExp ocl_letexp;


    public VariableDeclaration(
    ) {
    }



    public genericity_dsl_BindingModel getGenericity_dsl_bindingmodel() {
        return genericity_dsl_bindingmodel;
    }

    public void setGenericity_dsl_bindingmodel(genericity_dsl_BindingModel genericity_dsl_bindingmodel) {
        this.genericity_dsl_bindingmodel = genericity_dsl_bindingmodel;
    }
    public OCL_OclType getOcl_ocltype() {
        return ocl_ocltype;
    }

    public void setOcl_ocltype(OCL_OclType ocl_ocltype) {
        this.ocl_ocltype = ocl_ocltype;
    }
    public OCL_OclExpression getOcl_oclexpression() {
        return ocl_oclexpression;
    }

    public void setOcl_oclexpression(OCL_OclExpression ocl_oclexpression) {
        this.ocl_oclexpression = ocl_oclexpression;
    }
    public OCL_LetExp getOcl_letexp() {
        return ocl_letexp;
    }

    public void setOcl_letexp(OCL_LetExp ocl_letexp) {
        this.ocl_letexp = ocl_letexp;
    }

}