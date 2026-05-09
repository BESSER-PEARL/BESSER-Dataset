





import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends BehavioralFeature, MultiplicityElement, ParameterableElement, TypedElement {

    private boolean isQuery;





    private List<UML2_Parameter> uml2_parameters;




    private UML2_Constraint uml2_constraint;


    public UML2_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml2_parameters = new ArrayList<>();
    }

    public UML2_Operation(
        boolean isQuery        ArrayList<UML2_Parameter> uml2_parameters    ) {
        this.isQuery = isQuery;
        this.uml2_parameters = uml2_parameters;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }

}