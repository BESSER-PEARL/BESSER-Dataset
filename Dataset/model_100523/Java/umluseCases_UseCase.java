





import java.util.List;
import java.util.ArrayList;

public class umluseCases_UseCase extends BehavioredClassifier {






    private umluseCases_Classifier umlusecases_classifier;




    private List<umluseCases_Include> umlusecases_includes;




    private List<umluseCases_Classifier> umlusecases_classifiers;




    private List<umluseCases_ExtensionPoint> umlusecases_extensionpoints;




    private umluseCases_Include umlusecases_include;




    private umluseCases_Classifier umlusecases_classifier;




    private umluseCases_Extend umlusecases_extend;




    private List<umluseCases_Extend> umlusecases_extends;




    private umluseCases_ExtensionPoint umlusecases_extensionpoint;




    private umluseCases_Include umlusecases_include;




    private umluseCases_Extend umlusecases_extend;


    public umluseCases_UseCase(
    ) {
        super(
        );
        this.umlusecases_includes = new ArrayList<>();
        this.umlusecases_classifiers = new ArrayList<>();
        this.umlusecases_extensionpoints = new ArrayList<>();
        this.umlusecases_extends = new ArrayList<>();
    }

    public umluseCases_UseCase(
        ArrayList<umluseCases_Include> umlusecases_includes,        ArrayList<umluseCases_Classifier> umlusecases_classifiers,        ArrayList<umluseCases_ExtensionPoint> umlusecases_extensionpoints,        ArrayList<umluseCases_Extend> umlusecases_extends    ) {
        this.umlusecases_includes = umlusecases_includes;
        this.umlusecases_classifiers = umlusecases_classifiers;
        this.umlusecases_extensionpoints = umlusecases_extensionpoints;
        this.umlusecases_extends = umlusecases_extends;
    }


    public umluseCases_Classifier getUmlusecases_classifier() {
        return umlusecases_classifier;
    }

    public void setUmlusecases_classifier(umluseCases_Classifier umlusecases_classifier) {
        this.umlusecases_classifier = umlusecases_classifier;
    }
    public List<umluseCases_Include> getUmlusecases_includes() {
        return umlusecases_includes;
    }

    public void addUmlusecases_include(Umlusecases_include umlusecases_include) {
        this.umlusecases_includes.add(umlusecases_include);
    }
    public List<umluseCases_Classifier> getUmlusecases_classifiers() {
        return umlusecases_classifiers;
    }

    public void addUmlusecases_classifier(Umlusecases_classifier umlusecases_classifier) {
        this.umlusecases_classifiers.add(umlusecases_classifier);
    }
    public List<umluseCases_ExtensionPoint> getUmlusecases_extensionpoints() {
        return umlusecases_extensionpoints;
    }

    public void addUmlusecases_extensionpoint(Umlusecases_extensionpoint umlusecases_extensionpoint) {
        this.umlusecases_extensionpoints.add(umlusecases_extensionpoint);
    }
    public umluseCases_Include getUmlusecases_include() {
        return umlusecases_include;
    }

    public void setUmlusecases_include(umluseCases_Include umlusecases_include) {
        this.umlusecases_include = umlusecases_include;
    }
    public umluseCases_Classifier getUmlusecases_classifier() {
        return umlusecases_classifier;
    }

    public void setUmlusecases_classifier(umluseCases_Classifier umlusecases_classifier) {
        this.umlusecases_classifier = umlusecases_classifier;
    }
    public umluseCases_Extend getUmlusecases_extend() {
        return umlusecases_extend;
    }

    public void setUmlusecases_extend(umluseCases_Extend umlusecases_extend) {
        this.umlusecases_extend = umlusecases_extend;
    }
    public List<umluseCases_Extend> getUmlusecases_extends() {
        return umlusecases_extends;
    }

    public void addUmlusecases_extend(Umlusecases_extend umlusecases_extend) {
        this.umlusecases_extends.add(umlusecases_extend);
    }
    public umluseCases_ExtensionPoint getUmlusecases_extensionpoint() {
        return umlusecases_extensionpoint;
    }

    public void setUmlusecases_extensionpoint(umluseCases_ExtensionPoint umlusecases_extensionpoint) {
        this.umlusecases_extensionpoint = umlusecases_extensionpoint;
    }
    public umluseCases_Include getUmlusecases_include() {
        return umlusecases_include;
    }

    public void setUmlusecases_include(umluseCases_Include umlusecases_include) {
        this.umlusecases_include = umlusecases_include;
    }
    public umluseCases_Extend getUmlusecases_extend() {
        return umlusecases_extend;
    }

    public void setUmlusecases_extend(umluseCases_Extend umlusecases_extend) {
        this.umlusecases_extend = umlusecases_extend;
    }

}