





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedReplyAction extends TracedAction {






    private uml_TracedTrigger uml_tracedtrigger;




    private uml_TracedInputPin uml_tracedinputpin;




    private List<uml_TracedInputPin> uml_tracedinputpins;


    public umlTrace_uml_TracedReplyAction(
    ) {
        super(
        );
        this.uml_tracedinputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedReplyAction(
        ArrayList<uml_TracedInputPin> uml_tracedinputpins    ) {
        this.uml_tracedinputpins = uml_tracedinputpins;
    }


    public uml_TracedTrigger getUml_tracedtrigger() {
        return uml_tracedtrigger;
    }

    public void setUml_tracedtrigger(uml_TracedTrigger uml_tracedtrigger) {
        this.uml_tracedtrigger = uml_tracedtrigger;
    }
    public uml_TracedInputPin getUml_tracedinputpin() {
        return uml_tracedinputpin;
    }

    public void setUml_tracedinputpin(uml_TracedInputPin uml_tracedinputpin) {
        this.uml_tracedinputpin = uml_tracedinputpin;
    }
    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }

}