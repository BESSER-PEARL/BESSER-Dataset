





import java.util.List;
import java.util.ArrayList;

public class UMLModel_UseCase extends BehavioredClassifier {

    private String subject;





    private List<UMLModel_Include> umlmodel_includes;




    private UMLModel_Classifier umlmodel_classifier;




    private List<UMLModel_Extend> umlmodel_extends;




    private List<UMLModel_ExtensionPoint> umlmodel_extensionpoints;


    public UMLModel_UseCase(
        String subject    ) {
        super(
        );
        this.subject = subject;
        this.umlmodel_includes = new ArrayList<>();
        this.umlmodel_extends = new ArrayList<>();
        this.umlmodel_extensionpoints = new ArrayList<>();
    }

    public UMLModel_UseCase(
        String subject        ArrayList<UMLModel_Include> umlmodel_includes,        ArrayList<UMLModel_Extend> umlmodel_extends,        ArrayList<UMLModel_ExtensionPoint> umlmodel_extensionpoints    ) {
        this.subject = subject;
        this.umlmodel_includes = umlmodel_includes;
        this.umlmodel_extends = umlmodel_extends;
        this.umlmodel_extensionpoints = umlmodel_extensionpoints;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public List<UMLModel_Include> getUmlmodel_includes() {
        return umlmodel_includes;
    }

    public void addUmlmodel_include(Umlmodel_include umlmodel_include) {
        this.umlmodel_includes.add(umlmodel_include);
    }
    public UMLModel_Classifier getUmlmodel_classifier() {
        return umlmodel_classifier;
    }

    public void setUmlmodel_classifier(UMLModel_Classifier umlmodel_classifier) {
        this.umlmodel_classifier = umlmodel_classifier;
    }
    public List<UMLModel_Extend> getUmlmodel_extends() {
        return umlmodel_extends;
    }

    public void addUmlmodel_extend(Umlmodel_extend umlmodel_extend) {
        this.umlmodel_extends.add(umlmodel_extend);
    }
    public List<UMLModel_ExtensionPoint> getUmlmodel_extensionpoints() {
        return umlmodel_extensionpoints;
    }

    public void addUmlmodel_extensionpoint(Umlmodel_extensionpoint umlmodel_extensionpoint) {
        this.umlmodel_extensionpoints.add(umlmodel_extensionpoint);
    }

}