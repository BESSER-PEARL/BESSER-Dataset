





import java.util.List;
import java.util.ArrayList;

public class UML2_CollaborationOccurrence extends NamedElement {






    private List<UML2_Dependency> uml2_dependencys;




    private UML2_Classifier uml2_classifier;




    private UML2_Classifier uml2_classifier;


    public UML2_CollaborationOccurrence(
    ) {
        super(
        );
        this.uml2_dependencys = new ArrayList<>();
    }

    public UML2_CollaborationOccurrence(
        ArrayList<UML2_Dependency> uml2_dependencys    ) {
        this.uml2_dependencys = uml2_dependencys;
    }


    public List<UML2_Dependency> getUml2_dependencys() {
        return uml2_dependencys;
    }

    public void addUml2_dependency(Uml2_dependency uml2_dependency) {
        this.uml2_dependencys.add(uml2_dependency);
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}