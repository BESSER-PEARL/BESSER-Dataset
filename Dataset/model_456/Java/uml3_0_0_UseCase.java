





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_UseCase extends BehavioredClassifier {






    private List<uml3_0_0_Include> uml3_0_0_includes;




    private uml3_0_0_Include uml3_0_0_include;




    private uml3_0_0_Include uml3_0_0_include;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private uml3_0_0_ExtensionPoint uml3_0_0_extensionpoint;




    private uml3_0_0_Extend uml3_0_0_extend;




    private uml3_0_0_Extend uml3_0_0_extend;




    private List<uml3_0_0_ExtensionPoint> uml3_0_0_extensionpoints;




    private List<uml3_0_0_Extend> uml3_0_0_extends;




    private uml3_0_0_Classifier uml3_0_0_classifier;


    public uml3_0_0_UseCase(
    ) {
        super(
        );
        this.uml3_0_0_includes = new ArrayList<>();
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_extensionpoints = new ArrayList<>();
        this.uml3_0_0_extends = new ArrayList<>();
    }

    public uml3_0_0_UseCase(
        ArrayList<uml3_0_0_Include> uml3_0_0_includes,        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_ExtensionPoint> uml3_0_0_extensionpoints,        ArrayList<uml3_0_0_Extend> uml3_0_0_extends    ) {
        this.uml3_0_0_includes = uml3_0_0_includes;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_extensionpoints = uml3_0_0_extensionpoints;
        this.uml3_0_0_extends = uml3_0_0_extends;
    }


    public List<uml3_0_0_Include> getUml3_0_0_includes() {
        return uml3_0_0_includes;
    }

    public void addUml3_0_0_include(Uml3_0_0_include uml3_0_0_include) {
        this.uml3_0_0_includes.add(uml3_0_0_include);
    }
    public uml3_0_0_Include getUml3_0_0_include() {
        return uml3_0_0_include;
    }

    public void setUml3_0_0_include(uml3_0_0_Include uml3_0_0_include) {
        this.uml3_0_0_include = uml3_0_0_include;
    }
    public uml3_0_0_Include getUml3_0_0_include() {
        return uml3_0_0_include;
    }

    public void setUml3_0_0_include(uml3_0_0_Include uml3_0_0_include) {
        this.uml3_0_0_include = uml3_0_0_include;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public uml3_0_0_ExtensionPoint getUml3_0_0_extensionpoint() {
        return uml3_0_0_extensionpoint;
    }

    public void setUml3_0_0_extensionpoint(uml3_0_0_ExtensionPoint uml3_0_0_extensionpoint) {
        this.uml3_0_0_extensionpoint = uml3_0_0_extensionpoint;
    }
    public uml3_0_0_Extend getUml3_0_0_extend() {
        return uml3_0_0_extend;
    }

    public void setUml3_0_0_extend(uml3_0_0_Extend uml3_0_0_extend) {
        this.uml3_0_0_extend = uml3_0_0_extend;
    }
    public uml3_0_0_Extend getUml3_0_0_extend() {
        return uml3_0_0_extend;
    }

    public void setUml3_0_0_extend(uml3_0_0_Extend uml3_0_0_extend) {
        this.uml3_0_0_extend = uml3_0_0_extend;
    }
    public List<uml3_0_0_ExtensionPoint> getUml3_0_0_extensionpoints() {
        return uml3_0_0_extensionpoints;
    }

    public void addUml3_0_0_extensionpoint(Uml3_0_0_extensionpoint uml3_0_0_extensionpoint) {
        this.uml3_0_0_extensionpoints.add(uml3_0_0_extensionpoint);
    }
    public List<uml3_0_0_Extend> getUml3_0_0_extends() {
        return uml3_0_0_extends;
    }

    public void addUml3_0_0_extend(Uml3_0_0_extend uml3_0_0_extend) {
        this.uml3_0_0_extends.add(uml3_0_0_extend);
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }

}