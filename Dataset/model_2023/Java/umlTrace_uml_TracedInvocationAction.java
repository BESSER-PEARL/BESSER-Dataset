





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInvocationAction extends TracedAction {






    private uml_TracedPort uml_tracedport;




    private List<uml_TracedInputPin> uml_tracedinputpins;


    public umlTrace_uml_TracedInvocationAction(
    ) {
        super(
        );
        this.uml_tracedinputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedInvocationAction(
        ArrayList<uml_TracedInputPin> uml_tracedinputpins    ) {
        this.uml_tracedinputpins = uml_tracedinputpins;
    }


    public uml_TracedPort getUml_tracedport() {
        return uml_tracedport;
    }

    public void setUml_tracedport(uml_TracedPort uml_tracedport) {
        this.uml_tracedport = uml_tracedport;
    }
    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }

}