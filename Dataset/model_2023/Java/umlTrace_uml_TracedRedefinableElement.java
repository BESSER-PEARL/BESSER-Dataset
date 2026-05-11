





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedRedefinableElement extends TracedNamedElement {






    private List<uml_TracedClassifier> uml_tracedclassifiers;


    public umlTrace_uml_TracedRedefinableElement(
    ) {
        super(
        );
        this.uml_tracedclassifiers = new ArrayList<>();
    }

    public umlTrace_uml_TracedRedefinableElement(
        ArrayList<uml_TracedClassifier> uml_tracedclassifiers    ) {
        this.uml_tracedclassifiers = uml_tracedclassifiers;
    }


    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }

}