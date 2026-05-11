





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedTransition extends uml_TracedRedefinableElement, uml_TracedNamespace {






    private uml_TracedConstraint uml_tracedconstraint;




    private uml_TracedRegion uml_tracedregion;




    private List<uml_TracedTrigger> uml_tracedtriggers;




    private uml_TracedTransition uml_tracedtransition;


    public umlTrace_uml_TracedTransition(
    ) {
        super(
        );
        this.uml_tracedtriggers = new ArrayList<>();
    }

    public umlTrace_uml_TracedTransition(
        ArrayList<uml_TracedTrigger> uml_tracedtriggers    ) {
        this.uml_tracedtriggers = uml_tracedtriggers;
    }


    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }
    public uml_TracedRegion getUml_tracedregion() {
        return uml_tracedregion;
    }

    public void setUml_tracedregion(uml_TracedRegion uml_tracedregion) {
        this.uml_tracedregion = uml_tracedregion;
    }
    public List<uml_TracedTrigger> getUml_tracedtriggers() {
        return uml_tracedtriggers;
    }

    public void addUml_tracedtrigger(Uml_tracedtrigger uml_tracedtrigger) {
        this.uml_tracedtriggers.add(uml_tracedtrigger);
    }
    public uml_TracedTransition getUml_tracedtransition() {
        return uml_tracedtransition;
    }

    public void setUml_tracedtransition(uml_TracedTransition uml_tracedtransition) {
        this.uml_tracedtransition = uml_tracedtransition;
    }

}