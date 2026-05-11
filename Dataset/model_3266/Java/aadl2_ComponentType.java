





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentType extends ComponentClassifier {

    private String noFeatures;





    private List<aadl2_FlowSpecification> aadl2_flowspecifications;




    private List<aadl2_FeatureGroup> aadl2_featuregroups;




    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private List<aadl2_Feature> aadl2_features;




    private aadl2_TypeExtension aadl2_typeextension;




    private aadl2_TypeExtension aadl2_typeextension;




    private aadl2_Realization aadl2_realization;




    private List<aadl2_AbstractFeature> aadl2_abstractfeatures;




    private aadl2_ComponentType aadl2_componenttype;




    private aadl2_ComponentTypeRename aadl2_componenttyperename;


    public aadl2_ComponentType(
        String noFeatures    ) {
        super(
        );
        this.noFeatures = noFeatures;
        this.aadl2_flowspecifications = new ArrayList<>();
        this.aadl2_featuregroups = new ArrayList<>();
        this.aadl2_features = new ArrayList<>();
        this.aadl2_abstractfeatures = new ArrayList<>();
    }

    public aadl2_ComponentType(
        String noFeatures        ArrayList<aadl2_FlowSpecification> aadl2_flowspecifications,        ArrayList<aadl2_FeatureGroup> aadl2_featuregroups,        ArrayList<aadl2_Feature> aadl2_features,        ArrayList<aadl2_AbstractFeature> aadl2_abstractfeatures    ) {
        this.noFeatures = noFeatures;
        this.aadl2_flowspecifications = aadl2_flowspecifications;
        this.aadl2_featuregroups = aadl2_featuregroups;
        this.aadl2_features = aadl2_features;
        this.aadl2_abstractfeatures = aadl2_abstractfeatures;
    }

    public String getNofeatures() {
        return noFeatures;
    }

    public void setNofeatures(String noFeatures) {
        this.noFeatures = noFeatures;
    }

    public List<aadl2_FlowSpecification> getAadl2_flowspecifications() {
        return aadl2_flowspecifications;
    }

    public void addAadl2_flowspecification(Aadl2_flowspecification aadl2_flowspecification) {
        this.aadl2_flowspecifications.add(aadl2_flowspecification);
    }
    public List<aadl2_FeatureGroup> getAadl2_featuregroups() {
        return aadl2_featuregroups;
    }

    public void addAadl2_featuregroup(Aadl2_featuregroup aadl2_featuregroup) {
        this.aadl2_featuregroups.add(aadl2_featuregroup);
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public List<aadl2_Feature> getAadl2_features() {
        return aadl2_features;
    }

    public void addAadl2_feature(Aadl2_feature aadl2_feature) {
        this.aadl2_features.add(aadl2_feature);
    }
    public aadl2_TypeExtension getAadl2_typeextension() {
        return aadl2_typeextension;
    }

    public void setAadl2_typeextension(aadl2_TypeExtension aadl2_typeextension) {
        this.aadl2_typeextension = aadl2_typeextension;
    }
    public aadl2_TypeExtension getAadl2_typeextension() {
        return aadl2_typeextension;
    }

    public void setAadl2_typeextension(aadl2_TypeExtension aadl2_typeextension) {
        this.aadl2_typeextension = aadl2_typeextension;
    }
    public aadl2_Realization getAadl2_realization() {
        return aadl2_realization;
    }

    public void setAadl2_realization(aadl2_Realization aadl2_realization) {
        this.aadl2_realization = aadl2_realization;
    }
    public List<aadl2_AbstractFeature> getAadl2_abstractfeatures() {
        return aadl2_abstractfeatures;
    }

    public void addAadl2_abstractfeature(Aadl2_abstractfeature aadl2_abstractfeature) {
        this.aadl2_abstractfeatures.add(aadl2_abstractfeature);
    }
    public aadl2_ComponentType getAadl2_componenttype() {
        return aadl2_componenttype;
    }

    public void setAadl2_componenttype(aadl2_ComponentType aadl2_componenttype) {
        this.aadl2_componenttype = aadl2_componenttype;
    }
    public aadl2_ComponentTypeRename getAadl2_componenttyperename() {
        return aadl2_componenttyperename;
    }

    public void setAadl2_componenttyperename(aadl2_ComponentTypeRename aadl2_componenttyperename) {
        this.aadl2_componenttyperename = aadl2_componenttyperename;
    }

}