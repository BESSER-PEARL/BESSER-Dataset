





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedReclassifyObjectAction extends TracedAction {






    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private uml_TracedInputPin uml_tracedinputpin;


    public umlTrace_uml_TracedReclassifyObjectAction(
    ) {
        super(
        );
        this.uml_tracedclassifiers = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
    }

    public umlTrace_uml_TracedReclassifyObjectAction(
        ArrayList<uml_TracedClassifier> uml_tracedclassifiers,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers    ) {
        this.uml_tracedclassifiers = uml_tracedclassifiers;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
    }


    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public uml_TracedInputPin getUml_tracedinputpin() {
        return uml_tracedinputpin;
    }

    public void setUml_tracedinputpin(uml_TracedInputPin uml_tracedinputpin) {
        this.uml_tracedinputpin = uml_tracedinputpin;
    }

}