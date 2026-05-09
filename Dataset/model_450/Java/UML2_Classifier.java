





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Namespace, Type, RedefinableElement {

    private boolean isAbstract;





    private List<UML2_Classifier> uml2_classifiers;




    private UML2_Class uml2_class;




    private UML2_Classifier uml2_classifier;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.isAbstract = isAbstract;
        this.uml2_classifiers = uml2_classifiers;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}