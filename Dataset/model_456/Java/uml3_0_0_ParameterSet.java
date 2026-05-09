





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ParameterSet extends NamedElement {






    private uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;


    public uml3_0_0_ParameterSet(
    ) {
        super(
        );
        this.uml3_0_0_constraints = new ArrayList<>();
    }

    public uml3_0_0_ParameterSet(
        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints    ) {
        this.uml3_0_0_constraints = uml3_0_0_constraints;
    }


    public uml3_0_0_BehavioralFeature getUml3_0_0_behavioralfeature() {
        return uml3_0_0_behavioralfeature;
    }

    public void setUml3_0_0_behavioralfeature(uml3_0_0_BehavioralFeature uml3_0_0_behavioralfeature) {
        this.uml3_0_0_behavioralfeature = uml3_0_0_behavioralfeature;
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }

}