





import java.util.List;
import java.util.ArrayList;

public class UML2_ParameterSet extends NamedElement {






    private UML2_Parameter uml2_parameter;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Constraint> uml2_constraints;


    public UML2_ParameterSet(
    ) {
        super(
        );
        this.uml2_parameters = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
    }

    public UML2_ParameterSet(
        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Constraint> uml2_constraints    ) {
        this.uml2_parameters = uml2_parameters;
        this.uml2_constraints = uml2_constraints;
    }


    public UML2_Parameter getUml2_parameter() {
        return uml2_parameter;
    }

    public void setUml2_parameter(UML2_Parameter uml2_parameter) {
        this.uml2_parameter = uml2_parameter;
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }

}