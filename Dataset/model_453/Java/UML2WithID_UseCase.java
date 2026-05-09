





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_UseCase extends BehavioredClassifier {






    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_Extend uml2withid_extend;




    private UML2WithID_Extend uml2withid_extend;




    private List<UML2WithID_Include> uml2withid_includes;




    private List<UML2WithID_Extend> uml2withid_extends;




    private UML2WithID_Include uml2withid_include;




    private UML2WithID_Include uml2withid_include;




    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private UML2WithID_Classifier uml2withid_classifier;


    public UML2WithID_UseCase(
    ) {
        super(
        );
        this.uml2withid_includes = new ArrayList<>();
        this.uml2withid_extends = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_UseCase(
        ArrayList<UML2WithID_Include> uml2withid_includes,        ArrayList<UML2WithID_Extend> uml2withid_extends,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.uml2withid_includes = uml2withid_includes;
        this.uml2withid_extends = uml2withid_extends;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }


    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_Extend getUml2withid_extend() {
        return uml2withid_extend;
    }

    public void setUml2withid_extend(UML2WithID_Extend uml2withid_extend) {
        this.uml2withid_extend = uml2withid_extend;
    }
    public UML2WithID_Extend getUml2withid_extend() {
        return uml2withid_extend;
    }

    public void setUml2withid_extend(UML2WithID_Extend uml2withid_extend) {
        this.uml2withid_extend = uml2withid_extend;
    }
    public List<UML2WithID_Include> getUml2withid_includes() {
        return uml2withid_includes;
    }

    public void addUml2withid_include(Uml2withid_include uml2withid_include) {
        this.uml2withid_includes.add(uml2withid_include);
    }
    public List<UML2WithID_Extend> getUml2withid_extends() {
        return uml2withid_extends;
    }

    public void addUml2withid_extend(Uml2withid_extend uml2withid_extend) {
        this.uml2withid_extends.add(uml2withid_extend);
    }
    public UML2WithID_Include getUml2withid_include() {
        return uml2withid_include;
    }

    public void setUml2withid_include(UML2WithID_Include uml2withid_include) {
        this.uml2withid_include = uml2withid_include;
    }
    public UML2WithID_Include getUml2withid_include() {
        return uml2withid_include;
    }

    public void setUml2withid_include(UML2WithID_Include uml2withid_include) {
        this.uml2withid_include = uml2withid_include;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }

}