





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedUnmarshallAction extends TracedAction {






    private List<uml_TracedOutputPin> uml_tracedoutputpins;




    private uml_TracedInputPin uml_tracedinputpin;




    private uml_TracedClassifier uml_tracedclassifier;


    public umlTrace_uml_TracedUnmarshallAction(
    ) {
        super(
        );
        this.uml_tracedoutputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedUnmarshallAction(
        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins    ) {
        this.uml_tracedoutputpins = uml_tracedoutputpins;
    }


    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }
    public uml_TracedInputPin getUml_tracedinputpin() {
        return uml_tracedinputpin;
    }

    public void setUml_tracedinputpin(uml_TracedInputPin uml_tracedinputpin) {
        this.uml_tracedinputpin = uml_tracedinputpin;
    }
    public uml_TracedClassifier getUml_tracedclassifier() {
        return uml_tracedclassifier;
    }

    public void setUml_tracedclassifier(uml_TracedClassifier uml_tracedclassifier) {
        this.uml_tracedclassifier = uml_tracedclassifier;
    }

}