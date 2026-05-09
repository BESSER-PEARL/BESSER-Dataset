





import java.util.List;
import java.util.ArrayList;

public class ocl_uml_Constraint extends utilities_Visitable, ENamedElement {

    private String stereotype;
    private String instanceVarName;





    private OCLExpression oclexpression;


    public ocl_uml_Constraint(
        String stereotype,        String instanceVarName    ) {
        super(
        );
        this.stereotype = stereotype;
        this.instanceVarName = instanceVarName;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }
    public String getInstancevarname() {
        return instanceVarName;
    }

    public void setInstancevarname(String instanceVarName) {
        this.instanceVarName = instanceVarName;
    }

    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}