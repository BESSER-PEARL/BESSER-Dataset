





import java.util.List;
import java.util.ArrayList;

public class JTLMM_template_TemplateExp extends LiteralExp {






    private OclExpression oclexpression;




    private Variable variable;


    public JTLMM_template_TemplateExp(
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
    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}