





import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends TypedElement, BehavioralFeature, ParameterableElement, MultiplicityElement {

    private boolean isQuery;





    private UML2_Constraint uml2_constraint;


    public UML2_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
    }


    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }

}