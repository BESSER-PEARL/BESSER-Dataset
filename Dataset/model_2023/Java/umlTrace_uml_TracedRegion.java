





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedRegion extends uml_TracedRedefinableElement, uml_TracedNamespace {






    private List<uml_TracedTransition> uml_tracedtransitions;




    private uml_TracedRegion uml_tracedregion;




    private uml_TracedStateMachine uml_tracedstatemachine;




    private uml_TracedState uml_tracedstate;


    public umlTrace_uml_TracedRegion(
    ) {
        super(
        );
        this.uml_tracedtransitions = new ArrayList<>();
    }

    public umlTrace_uml_TracedRegion(
        ArrayList<uml_TracedTransition> uml_tracedtransitions    ) {
        this.uml_tracedtransitions = uml_tracedtransitions;
    }


    public List<uml_TracedTransition> getUml_tracedtransitions() {
        return uml_tracedtransitions;
    }

    public void addUml_tracedtransition(Uml_tracedtransition uml_tracedtransition) {
        this.uml_tracedtransitions.add(uml_tracedtransition);
    }
    public uml_TracedRegion getUml_tracedregion() {
        return uml_tracedregion;
    }

    public void setUml_tracedregion(uml_TracedRegion uml_tracedregion) {
        this.uml_tracedregion = uml_tracedregion;
    }
    public uml_TracedStateMachine getUml_tracedstatemachine() {
        return uml_tracedstatemachine;
    }

    public void setUml_tracedstatemachine(uml_TracedStateMachine uml_tracedstatemachine) {
        this.uml_tracedstatemachine = uml_tracedstatemachine;
    }
    public uml_TracedState getUml_tracedstate() {
        return uml_tracedstate;
    }

    public void setUml_tracedstate(uml_TracedState uml_tracedstate) {
        this.uml_tracedstate = uml_tracedstate;
    }

}