





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedProtocolTransition extends TracedTransition {






    private List<uml_TracedOperation> uml_tracedoperations;




    private uml_TracedConstraint uml_tracedconstraint;




    private uml_TracedConstraint uml_tracedconstraint;


    public umlTrace_uml_TracedProtocolTransition(
    ) {
        super(
        );
        this.uml_tracedoperations = new ArrayList<>();
    }

    public umlTrace_uml_TracedProtocolTransition(
        ArrayList<uml_TracedOperation> uml_tracedoperations    ) {
        this.uml_tracedoperations = uml_tracedoperations;
    }


    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }
    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }
    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }

}