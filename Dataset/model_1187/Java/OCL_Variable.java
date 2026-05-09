





import java.util.List;
import java.util.ArrayList;

public class OCL_Variable extends TypedElement {






    private Parameter parameter;




    private OclExpression oclexpression;


    public OCL_Variable(
    ) {
        super(
        );
    }



    public Parameter getParameter() {
        return parameter;
    }

    public void setParameter(Parameter parameter) {
        this.parameter = parameter;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}