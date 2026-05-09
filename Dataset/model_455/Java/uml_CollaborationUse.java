





import java.util.List;
import java.util.ArrayList;

public class uml_CollaborationUse extends NamedElement {






    private List<uml_Dependency> uml_dependencys;




    private uml_Classifier uml_classifier;




    private uml_Classifier uml_classifier;


    public uml_CollaborationUse(
    ) {
        super(
        );
        this.uml_dependencys = new ArrayList<>();
    }

    public uml_CollaborationUse(
        ArrayList<uml_Dependency> uml_dependencys    ) {
        this.uml_dependencys = uml_dependencys;
    }


    public List<uml_Dependency> getUml_dependencys() {
        return uml_dependencys;
    }

    public void addUml_dependency(Uml_dependency uml_dependency) {
        this.uml_dependencys.add(uml_dependency);
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }

}