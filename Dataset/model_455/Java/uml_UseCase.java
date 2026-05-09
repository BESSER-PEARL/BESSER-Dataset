





import java.util.List;
import java.util.ArrayList;

public class uml_UseCase extends BehavioredClassifier {






    private List<uml_Extend> uml_extends;




    private uml_Classifier uml_classifier;




    private uml_ExtensionPoint uml_extensionpoint;




    private uml_Include uml_include;




    private uml_Extend uml_extend;




    private List<uml_Classifier> uml_classifiers;




    private List<uml_ExtensionPoint> uml_extensionpoints;




    private uml_Include uml_include;




    private uml_Extend uml_extend;




    private uml_Classifier uml_classifier;




    private List<uml_Include> uml_includes;


    public uml_UseCase(
    ) {
        super(
        );
        this.uml_extends = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
        this.uml_extensionpoints = new ArrayList<>();
        this.uml_includes = new ArrayList<>();
    }

    public uml_UseCase(
        ArrayList<uml_Extend> uml_extends,        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_ExtensionPoint> uml_extensionpoints,        ArrayList<uml_Include> uml_includes    ) {
        this.uml_extends = uml_extends;
        this.uml_classifiers = uml_classifiers;
        this.uml_extensionpoints = uml_extensionpoints;
        this.uml_includes = uml_includes;
    }


    public List<uml_Extend> getUml_extends() {
        return uml_extends;
    }

    public void addUml_extend(Uml_extend uml_extend) {
        this.uml_extends.add(uml_extend);
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public uml_ExtensionPoint getUml_extensionpoint() {
        return uml_extensionpoint;
    }

    public void setUml_extensionpoint(uml_ExtensionPoint uml_extensionpoint) {
        this.uml_extensionpoint = uml_extensionpoint;
    }
    public uml_Include getUml_include() {
        return uml_include;
    }

    public void setUml_include(uml_Include uml_include) {
        this.uml_include = uml_include;
    }
    public uml_Extend getUml_extend() {
        return uml_extend;
    }

    public void setUml_extend(uml_Extend uml_extend) {
        this.uml_extend = uml_extend;
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public List<uml_ExtensionPoint> getUml_extensionpoints() {
        return uml_extensionpoints;
    }

    public void addUml_extensionpoint(Uml_extensionpoint uml_extensionpoint) {
        this.uml_extensionpoints.add(uml_extensionpoint);
    }
    public uml_Include getUml_include() {
        return uml_include;
    }

    public void setUml_include(uml_Include uml_include) {
        this.uml_include = uml_include;
    }
    public uml_Extend getUml_extend() {
        return uml_extend;
    }

    public void setUml_extend(uml_Extend uml_extend) {
        this.uml_extend = uml_extend;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_Include> getUml_includes() {
        return uml_includes;
    }

    public void addUml_include(Uml_include uml_include) {
        this.uml_includes.add(uml_include);
    }

}