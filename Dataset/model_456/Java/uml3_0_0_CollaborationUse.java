





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_CollaborationUse extends NamedElement {






    private uml3_0_0_Classifier uml3_0_0_classifier;




    private List<uml3_0_0_Dependency> uml3_0_0_dependencys;




    private uml3_0_0_Classifier uml3_0_0_classifier;


    public uml3_0_0_CollaborationUse(
    ) {
        super(
        );
        this.uml3_0_0_dependencys = new ArrayList<>();
    }

    public uml3_0_0_CollaborationUse(
        ArrayList<uml3_0_0_Dependency> uml3_0_0_dependencys    ) {
        this.uml3_0_0_dependencys = uml3_0_0_dependencys;
    }


    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public List<uml3_0_0_Dependency> getUml3_0_0_dependencys() {
        return uml3_0_0_dependencys;
    }

    public void addUml3_0_0_dependency(Uml3_0_0_dependency uml3_0_0_dependency) {
        this.uml3_0_0_dependencys.add(uml3_0_0_dependency);
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }

}