





import java.util.List;
import java.util.ArrayList;

public class QVTTemplate_TemplateExp extends LiteralExp {






    private Variable variable;




    private OclExpression oclexpression;


    public QVTTemplate_TemplateExp(
    ) {
        super(
        );
    }



    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}