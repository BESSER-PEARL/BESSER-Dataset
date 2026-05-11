





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedGeneralization extends TracedDirectedRelationship {






    private uml_TracedClassifier uml_tracedclassifier;




    private uml_TracedClassifier uml_tracedclassifier;




    private List<uml_TracedGeneralizationSet> uml_tracedgeneralizationsets;


    public umlTrace_uml_TracedGeneralization(
    ) {
        super(
        );
        this.uml_tracedgeneralizationsets = new ArrayList<>();
    }

    public umlTrace_uml_TracedGeneralization(
        ArrayList<uml_TracedGeneralizationSet> uml_tracedgeneralizationsets    ) {
        this.uml_tracedgeneralizationsets = uml_tracedgeneralizationsets;
    }


    public uml_TracedClassifier getUml_tracedclassifier() {
        return uml_tracedclassifier;
    }

    public void setUml_tracedclassifier(uml_TracedClassifier uml_tracedclassifier) {
        this.uml_tracedclassifier = uml_tracedclassifier;
    }
    public uml_TracedClassifier getUml_tracedclassifier() {
        return uml_tracedclassifier;
    }

    public void setUml_tracedclassifier(uml_TracedClassifier uml_tracedclassifier) {
        this.uml_tracedclassifier = uml_tracedclassifier;
    }
    public List<uml_TracedGeneralizationSet> getUml_tracedgeneralizationsets() {
        return uml_tracedgeneralizationsets;
    }

    public void addUml_tracedgeneralizationset(Uml_tracedgeneralizationset uml_tracedgeneralizationset) {
        this.uml_tracedgeneralizationsets.add(uml_tracedgeneralizationset);
    }

}