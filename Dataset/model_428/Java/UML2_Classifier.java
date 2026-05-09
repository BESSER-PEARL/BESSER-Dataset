





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Type, Namespace, RedefinableElement {

    private boolean isAbstract;





    private UML2_Feature uml2_feature;




    private List<UML2_Feature> uml2_features;




    private List<UML2_Generalization> uml2_generalizations;




    private UML2_Generalization uml2_generalization;




    private List<UML2_NamedElement> uml2_namedelements;


    public UML2_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2_features = new ArrayList<>();
        this.uml2_generalizations = new ArrayList<>();
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Classifier(
        boolean isAbstract        ArrayList<UML2_Feature> uml2_features,        ArrayList<UML2_Generalization> uml2_generalizations,        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.isAbstract = isAbstract;
        this.uml2_features = uml2_features;
        this.uml2_generalizations = uml2_generalizations;
        this.uml2_namedelements = uml2_namedelements;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public UML2_Feature getUml2_feature() {
        return uml2_feature;
    }

    public void setUml2_feature(UML2_Feature uml2_feature) {
        this.uml2_feature = uml2_feature;
    }
    public List<UML2_Feature> getUml2_features() {
        return uml2_features;
    }

    public void addUml2_feature(Uml2_feature uml2_feature) {
        this.uml2_features.add(uml2_feature);
    }
    public List<UML2_Generalization> getUml2_generalizations() {
        return uml2_generalizations;
    }

    public void addUml2_generalization(Uml2_generalization uml2_generalization) {
        this.uml2_generalizations.add(uml2_generalization);
    }
    public UML2_Generalization getUml2_generalization() {
        return uml2_generalization;
    }

    public void setUml2_generalization(UML2_Generalization uml2_generalization) {
        this.uml2_generalization = uml2_generalization;
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }

}