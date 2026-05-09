





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ParameterSet extends NamedElement {

    private String parameter;





    private List<UMLModel_Constraint> umlmodel_constraints;


    public UMLModel_ParameterSet(
        String parameter    ) {
        super(
        );
        this.parameter = parameter;
        this.umlmodel_constraints = new ArrayList<>();
    }

    public UMLModel_ParameterSet(
        String parameter        ArrayList<UMLModel_Constraint> umlmodel_constraints    ) {
        this.parameter = parameter;
        this.umlmodel_constraints = umlmodel_constraints;
    }

    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }

    public List<UMLModel_Constraint> getUmlmodel_constraints() {
        return umlmodel_constraints;
    }

    public void addUmlmodel_constraint(Umlmodel_constraint umlmodel_constraint) {
        this.umlmodel_constraints.add(umlmodel_constraint);
    }

}