





import java.util.List;
import java.util.ArrayList;

public class QVTTemplate_TemplateExp extends LiteralExp {






    private OclExpression oclexpression;




    private Variable variable;


    public QVTTemplate_TemplateExp(
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