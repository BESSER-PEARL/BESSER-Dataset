





import java.util.List;
import java.util.ArrayList;

public class aadl2_Classifier extends Namespace, Type {

    private String noPrototypes;
    private String noProperties;
    private String noAnnexes;





    private aadl2_ClassifierFeature aadl2_classifierfeature;




    private aadl2_Classifier aadl2_classifier;




    private List<aadl2_NamedElement> aadl2_namedelements;




    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;




    private aadl2_RefinableElement aadl2_refinableelement;




    private aadl2_PropertyAssociation aadl2_propertyassociation;




    private List<aadl2_ClassifierFeature> aadl2_classifierfeatures;




    private aadl2_Property aadl2_property;


    public aadl2_Classifier(
        String noPrototypes,        String noProperties,        String noAnnexes    ) {
        super(
        );
        this.noPrototypes = noPrototypes;
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.aadl2_namedelements = new ArrayList<>();
        this.aadl2_prototypebindings = new ArrayList<>();
        this.aadl2_classifierfeatures = new ArrayList<>();
    }

    public aadl2_Classifier(
        String noPrototypes,        String noProperties,        String noAnnexes        ArrayList<aadl2_NamedElement> aadl2_namedelements,        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings,        ArrayList<aadl2_ClassifierFeature> aadl2_classifierfeatures    ) {
        this.noPrototypes = noPrototypes;
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.aadl2_namedelements = aadl2_namedelements;
        this.aadl2_prototypebindings = aadl2_prototypebindings;
        this.aadl2_classifierfeatures = aadl2_classifierfeatures;
    }

    public String getNoprototypes() {
        return noPrototypes;
    }

    public void setNoprototypes(String noPrototypes) {
        this.noPrototypes = noPrototypes;
    }
    public String getNoproperties() {
        return noProperties;
    }

    public void setNoproperties(String noProperties) {
        this.noProperties = noProperties;
    }
    public String getNoannexes() {
        return noAnnexes;
    }

    public void setNoannexes(String noAnnexes) {
        this.noAnnexes = noAnnexes;
    }

    public aadl2_ClassifierFeature getAadl2_classifierfeature() {
        return aadl2_classifierfeature;
    }

    public void setAadl2_classifierfeature(aadl2_ClassifierFeature aadl2_classifierfeature) {
        this.aadl2_classifierfeature = aadl2_classifierfeature;
    }
    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public List<aadl2_NamedElement> getAadl2_namedelements() {
        return aadl2_namedelements;
    }

    public void addAadl2_namedelement(Aadl2_namedelement aadl2_namedelement) {
        this.aadl2_namedelements.add(aadl2_namedelement);
    }
    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }
    public aadl2_RefinableElement getAadl2_refinableelement() {
        return aadl2_refinableelement;
    }

    public void setAadl2_refinableelement(aadl2_RefinableElement aadl2_refinableelement) {
        this.aadl2_refinableelement = aadl2_refinableelement;
    }
    public aadl2_PropertyAssociation getAadl2_propertyassociation() {
        return aadl2_propertyassociation;
    }

    public void setAadl2_propertyassociation(aadl2_PropertyAssociation aadl2_propertyassociation) {
        this.aadl2_propertyassociation = aadl2_propertyassociation;
    }
    public List<aadl2_ClassifierFeature> getAadl2_classifierfeatures() {
        return aadl2_classifierfeatures;
    }

    public void addAadl2_classifierfeature(Aadl2_classifierfeature aadl2_classifierfeature) {
        this.aadl2_classifierfeatures.add(aadl2_classifierfeature);
    }
    public aadl2_Property getAadl2_property() {
        return aadl2_property;
    }

    public void setAadl2_property(aadl2_Property aadl2_property) {
        this.aadl2_property = aadl2_property;
    }

}