





import java.util.List;
import java.util.ArrayList;

public class uml_ParameterSet extends NamedElement {






    private List<uml_Constraint> uml_constraints;




    private uml_BehavioralFeature uml_behavioralfeature;


    public uml_ParameterSet(
    ) {
        super(
        );
        this.uml_constraints = new ArrayList<>();
    }

    public uml_ParameterSet(
        ArrayList<uml_Constraint> uml_constraints    ) {
        this.uml_constraints = uml_constraints;
    }


    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public uml_BehavioralFeature getUml_behavioralfeature() {
        return uml_behavioralfeature;
    }

    public void setUml_behavioralfeature(uml_BehavioralFeature uml_behavioralfeature) {
        this.uml_behavioralfeature = uml_behavioralfeature;
    }

}