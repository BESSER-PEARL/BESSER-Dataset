





import java.util.List;
import java.util.ArrayList;

public class aadl2_Classifier extends Type, Namespace {

    private String noProperties;
    private String noAnnexes;
    private String noPrototypes;





    private List<aadl2_AnnexSubclause> aadl2_annexsubclauses;




    private List<aadl2_NamedElement> aadl2_namedelements;




    private aadl2_Feature aadl2_feature;




    private aadl2_PackageSection aadl2_packagesection;




    private aadl2_RefinableElement aadl2_refinableelement;




    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;




    private List<aadl2_Prototype> aadl2_prototypes;




    private aadl2_PropertyAssociation aadl2_propertyassociation;




    private List<aadl2_ClassifierFeature> aadl2_classifierfeatures;




    private List<aadl2_Classifier> aadl2_classifiers;




    private aadl2_ClassifierFeature aadl2_classifierfeature;


    public aadl2_Classifier(
        String noProperties,        String noAnnexes,        String noPrototypes    ) {
        super(
        );
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.noPrototypes = noPrototypes;
        this.aadl2_annexsubclauses = new ArrayList<>();
        this.aadl2_namedelements = new ArrayList<>();
        this.aadl2_prototypebindings = new ArrayList<>();
        this.aadl2_prototypes = new ArrayList<>();
        this.aadl2_classifierfeatures = new ArrayList<>();
        this.aadl2_classifiers = new ArrayList<>();
    }

    public aadl2_Classifier(
        String noProperties,        String noAnnexes,        String noPrototypes        ArrayList<aadl2_AnnexSubclause> aadl2_annexsubclauses,        ArrayList<aadl2_NamedElement> aadl2_namedelements,        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings,        ArrayList<aadl2_Prototype> aadl2_prototypes,        ArrayList<aadl2_ClassifierFeature> aadl2_classifierfeatures,        ArrayList<aadl2_Classifier> aadl2_classifiers    ) {
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.noPrototypes = noPrototypes;
        this.aadl2_annexsubclauses = aadl2_annexsubclauses;
        this.aadl2_namedelements = aadl2_namedelements;
        this.aadl2_prototypebindings = aadl2_prototypebindings;
        this.aadl2_prototypes = aadl2_prototypes;
        this.aadl2_classifierfeatures = aadl2_classifierfeatures;
        this.aadl2_classifiers = aadl2_classifiers;
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
    public String getNoprototypes() {
        return noPrototypes;
    }

    public void setNoprototypes(String noPrototypes) {
        this.noPrototypes = noPrototypes;
    }

    public List<aadl2_AnnexSubclause> getAadl2_annexsubclauses() {
        return aadl2_annexsubclauses;
    }

    public void addAadl2_annexsubclause(Aadl2_annexsubclause aadl2_annexsubclause) {
        this.aadl2_annexsubclauses.add(aadl2_annexsubclause);
    }
    public List<aadl2_NamedElement> getAadl2_namedelements() {
        return aadl2_namedelements;
    }

    public void addAadl2_namedelement(Aadl2_namedelement aadl2_namedelement) {
        this.aadl2_namedelements.add(aadl2_namedelement);
    }
    public aadl2_Feature getAadl2_feature() {
        return aadl2_feature;
    }

    public void setAadl2_feature(aadl2_Feature aadl2_feature) {
        this.aadl2_feature = aadl2_feature;
    }
    public aadl2_PackageSection getAadl2_packagesection() {
        return aadl2_packagesection;
    }

    public void setAadl2_packagesection(aadl2_PackageSection aadl2_packagesection) {
        this.aadl2_packagesection = aadl2_packagesection;
    }
    public aadl2_RefinableElement getAadl2_refinableelement() {
        return aadl2_refinableelement;
    }

    public void setAadl2_refinableelement(aadl2_RefinableElement aadl2_refinableelement) {
        this.aadl2_refinableelement = aadl2_refinableelement;
    }
    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }
    public List<aadl2_Prototype> getAadl2_prototypes() {
        return aadl2_prototypes;
    }

    public void addAadl2_prototype(Aadl2_prototype aadl2_prototype) {
        this.aadl2_prototypes.add(aadl2_prototype);
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
    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }
    public aadl2_ClassifierFeature getAadl2_classifierfeature() {
        return aadl2_classifierfeature;
    }

    public void setAadl2_classifierfeature(aadl2_ClassifierFeature aadl2_classifierfeature) {
        this.aadl2_classifierfeature = aadl2_classifierfeature;
    }

}