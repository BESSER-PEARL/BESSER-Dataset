





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Classifier extends TemplateableElement, RedefinableElement, Namespace, Type {

    private String representation;
    private String inheritedMember;
    private String general;
    private String redefinedClassifier;
    private String isAbstract;
    private String attribute;
    private String feature;
    private String useCase;
    private String powertypeExtent;





    private UMLModel_Interface umlmodel_interface;




    private List<UMLModel_CollaborationUse> umlmodel_collaborationuses;




    private List<UMLModel_Generalization> umlmodel_generalizations;


    public UMLModel_Classifier(
        String representation,        String inheritedMember,        String general,        String redefinedClassifier,        String isAbstract,        String attribute,        String feature,        String useCase,        String powertypeExtent    ) {
        super(
        );
        this.representation = representation;
        this.inheritedMember = inheritedMember;
        this.general = general;
        this.redefinedClassifier = redefinedClassifier;
        this.isAbstract = isAbstract;
        this.attribute = attribute;
        this.feature = feature;
        this.useCase = useCase;
        this.powertypeExtent = powertypeExtent;
        this.umlmodel_collaborationuses = new ArrayList<>();
        this.umlmodel_generalizations = new ArrayList<>();
    }

    public UMLModel_Classifier(
        String representation,        String inheritedMember,        String general,        String redefinedClassifier,        String isAbstract,        String attribute,        String feature,        String useCase,        String powertypeExtent        ArrayList<UMLModel_CollaborationUse> umlmodel_collaborationuses,        ArrayList<UMLModel_Generalization> umlmodel_generalizations    ) {
        this.representation = representation;
        this.inheritedMember = inheritedMember;
        this.general = general;
        this.redefinedClassifier = redefinedClassifier;
        this.isAbstract = isAbstract;
        this.attribute = attribute;
        this.feature = feature;
        this.useCase = useCase;
        this.powertypeExtent = powertypeExtent;
        this.umlmodel_collaborationuses = umlmodel_collaborationuses;
        this.umlmodel_generalizations = umlmodel_generalizations;
    }

    public String getRepresentation() {
        return representation;
    }

    public void setRepresentation(String representation) {
        this.representation = representation;
    }
    public String getInheritedmember() {
        return inheritedMember;
    }

    public void setInheritedmember(String inheritedMember) {
        this.inheritedMember = inheritedMember;
    }
    public String getGeneral() {
        return general;
    }

    public void setGeneral(String general) {
        this.general = general;
    }
    public String getRedefinedclassifier() {
        return redefinedClassifier;
    }

    public void setRedefinedclassifier(String redefinedClassifier) {
        this.redefinedClassifier = redefinedClassifier;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }
    public String getUsecase() {
        return useCase;
    }

    public void setUsecase(String useCase) {
        this.useCase = useCase;
    }
    public String getPowertypeextent() {
        return powertypeExtent;
    }

    public void setPowertypeextent(String powertypeExtent) {
        this.powertypeExtent = powertypeExtent;
    }

    public UMLModel_Interface getUmlmodel_interface() {
        return umlmodel_interface;
    }

    public void setUmlmodel_interface(UMLModel_Interface umlmodel_interface) {
        this.umlmodel_interface = umlmodel_interface;
    }
    public List<UMLModel_CollaborationUse> getUmlmodel_collaborationuses() {
        return umlmodel_collaborationuses;
    }

    public void addUmlmodel_collaborationuse(Umlmodel_collaborationuse umlmodel_collaborationuse) {
        this.umlmodel_collaborationuses.add(umlmodel_collaborationuse);
    }
    public List<UMLModel_Generalization> getUmlmodel_generalizations() {
        return umlmodel_generalizations;
    }

    public void addUmlmodel_generalization(Umlmodel_generalization umlmodel_generalization) {
        this.umlmodel_generalizations.add(umlmodel_generalization);
    }

}