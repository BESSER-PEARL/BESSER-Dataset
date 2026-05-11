





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedOpaqueAction extends TracedAction {






    private List<uml_TracedInputPin> uml_tracedinputpins;




    private List<uml_TracedOutputPin> uml_tracedoutputpins;


    public umlTrace_uml_TracedOpaqueAction(
    ) {
        super(
        );
        this.uml_tracedinputpins = new ArrayList<>();
        this.uml_tracedoutputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedOpaqueAction(
        ArrayList<uml_TracedInputPin> uml_tracedinputpins,        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins    ) {
        this.uml_tracedinputpins = uml_tracedinputpins;
        this.uml_tracedoutputpins = uml_tracedoutputpins;
    }


    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }
    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }

}