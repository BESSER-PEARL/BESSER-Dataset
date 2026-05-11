





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedGeneralizationSet extends TracedPackageableElement {






    private List<uml_TracedGeneralization> uml_tracedgeneralizations;




    private uml_TracedClassifier uml_tracedclassifier;


    public umlTrace_uml_TracedGeneralizationSet(
    ) {
        super(
        );
        this.uml_tracedgeneralizations = new ArrayList<>();
    }

    public umlTrace_uml_TracedGeneralizationSet(
        ArrayList<uml_TracedGeneralization> uml_tracedgeneralizations    ) {
        this.uml_tracedgeneralizations = uml_tracedgeneralizations;
    }


    public List<uml_TracedGeneralization> getUml_tracedgeneralizations() {
        return uml_tracedgeneralizations;
    }

    public void addUml_tracedgeneralization(Uml_tracedgeneralization uml_tracedgeneralization) {
        this.uml_tracedgeneralizations.add(uml_tracedgeneralization);
    }
    public uml_TracedClassifier getUml_tracedclassifier() {
        return uml_tracedclassifier;
    }

    public void setUml_tracedclassifier(uml_TracedClassifier uml_tracedclassifier) {
        this.uml_tracedclassifier = uml_tracedclassifier;
    }

}