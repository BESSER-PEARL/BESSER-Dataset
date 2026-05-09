





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_UseCase extends BehavioredClassifier {






    private List<CompleteDSLPckg_ExtensionPoint> completedslpckg_extensionpoints;




    private CompleteDSLPckg_Extend completedslpckg_extend;




    private CompleteDSLPckg_ExtensionPoint completedslpckg_extensionpoint;




    private List<CompleteDSLPckg_Include> completedslpckg_includes;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private CompleteDSLPckg_Include completedslpckg_include;




    private List<CompleteDSLPckg_Extend> completedslpckg_extends;




    private CompleteDSLPckg_Extend completedslpckg_extend;




    private CompleteDSLPckg_Include completedslpckg_include;


    public CompleteDSLPckg_UseCase(
    ) {
        super(
        );
        this.completedslpckg_extensionpoints = new ArrayList<>();
        this.completedslpckg_includes = new ArrayList<>();
        this.completedslpckg_classifiers = new ArrayList<>();
        this.completedslpckg_extends = new ArrayList<>();
    }

    public CompleteDSLPckg_UseCase(
        ArrayList<CompleteDSLPckg_ExtensionPoint> completedslpckg_extensionpoints,        ArrayList<CompleteDSLPckg_Include> completedslpckg_includes,        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers,        ArrayList<CompleteDSLPckg_Extend> completedslpckg_extends    ) {
        this.completedslpckg_extensionpoints = completedslpckg_extensionpoints;
        this.completedslpckg_includes = completedslpckg_includes;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
        this.completedslpckg_extends = completedslpckg_extends;
    }


    public List<CompleteDSLPckg_ExtensionPoint> getCompletedslpckg_extensionpoints() {
        return completedslpckg_extensionpoints;
    }

    public void addCompletedslpckg_extensionpoint(Completedslpckg_extensionpoint completedslpckg_extensionpoint) {
        this.completedslpckg_extensionpoints.add(completedslpckg_extensionpoint);
    }
    public CompleteDSLPckg_Extend getCompletedslpckg_extend() {
        return completedslpckg_extend;
    }

    public void setCompletedslpckg_extend(CompleteDSLPckg_Extend completedslpckg_extend) {
        this.completedslpckg_extend = completedslpckg_extend;
    }
    public CompleteDSLPckg_ExtensionPoint getCompletedslpckg_extensionpoint() {
        return completedslpckg_extensionpoint;
    }

    public void setCompletedslpckg_extensionpoint(CompleteDSLPckg_ExtensionPoint completedslpckg_extensionpoint) {
        this.completedslpckg_extensionpoint = completedslpckg_extensionpoint;
    }
    public List<CompleteDSLPckg_Include> getCompletedslpckg_includes() {
        return completedslpckg_includes;
    }

    public void addCompletedslpckg_include(Completedslpckg_include completedslpckg_include) {
        this.completedslpckg_includes.add(completedslpckg_include);
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public CompleteDSLPckg_Include getCompletedslpckg_include() {
        return completedslpckg_include;
    }

    public void setCompletedslpckg_include(CompleteDSLPckg_Include completedslpckg_include) {
        this.completedslpckg_include = completedslpckg_include;
    }
    public List<CompleteDSLPckg_Extend> getCompletedslpckg_extends() {
        return completedslpckg_extends;
    }

    public void addCompletedslpckg_extend(Completedslpckg_extend completedslpckg_extend) {
        this.completedslpckg_extends.add(completedslpckg_extend);
    }
    public CompleteDSLPckg_Extend getCompletedslpckg_extend() {
        return completedslpckg_extend;
    }

    public void setCompletedslpckg_extend(CompleteDSLPckg_Extend completedslpckg_extend) {
        this.completedslpckg_extend = completedslpckg_extend;
    }
    public CompleteDSLPckg_Include getCompletedslpckg_include() {
        return completedslpckg_include;
    }

    public void setCompletedslpckg_include(CompleteDSLPckg_Include completedslpckg_include) {
        this.completedslpckg_include = completedslpckg_include;
    }

}