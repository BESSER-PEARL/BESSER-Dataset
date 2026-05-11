





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroupType extends Classifier {

    private String feature;





    private List<aadl2_Parameter> aadl2_parameters;




    private aadl2_FeatureGroup aadl2_featuregroup;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private List<aadl2_Feature> aadl2_features;




    private aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename;




    private List<aadl2_FeatureGroup> aadl2_featuregroups;




    private List<aadl2_DataAccess> aadl2_dataaccesss;




    private aadl2_PackageSection aadl2_packagesection;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_FeatureGroupPrototype aadl2_featuregroupprototype;




    private List<aadl2_AbstractFeature> aadl2_abstractfeatures;




    private aadl2_FeatureGroupReference aadl2_featuregroupreference;


    public aadl2_FeatureGroupType(
        String feature    ) {
        super(
        );
        this.feature = feature;
        this.aadl2_parameters = new ArrayList<>();
        this.aadl2_features = new ArrayList<>();
        this.aadl2_featuregroups = new ArrayList<>();
        this.aadl2_dataaccesss = new ArrayList<>();
        this.aadl2_abstractfeatures = new ArrayList<>();
    }

    public aadl2_FeatureGroupType(
        String feature        ArrayList<aadl2_Parameter> aadl2_parameters,        ArrayList<aadl2_Feature> aadl2_features,        ArrayList<aadl2_FeatureGroup> aadl2_featuregroups,        ArrayList<aadl2_DataAccess> aadl2_dataaccesss,        ArrayList<aadl2_AbstractFeature> aadl2_abstractfeatures    ) {
        this.feature = feature;
        this.aadl2_parameters = aadl2_parameters;
        this.aadl2_features = aadl2_features;
        this.aadl2_featuregroups = aadl2_featuregroups;
        this.aadl2_dataaccesss = aadl2_dataaccesss;
        this.aadl2_abstractfeatures = aadl2_abstractfeatures;
    }

    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public List<aadl2_Parameter> getAadl2_parameters() {
        return aadl2_parameters;
    }

    public void addAadl2_parameter(Aadl2_parameter aadl2_parameter) {
        this.aadl2_parameters.add(aadl2_parameter);
    }
    public aadl2_FeatureGroup getAadl2_featuregroup() {
        return aadl2_featuregroup;
    }

    public void setAadl2_featuregroup(aadl2_FeatureGroup aadl2_featuregroup) {
        this.aadl2_featuregroup = aadl2_featuregroup;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public List<aadl2_Feature> getAadl2_features() {
        return aadl2_features;
    }

    public void addAadl2_feature(Aadl2_feature aadl2_feature) {
        this.aadl2_features.add(aadl2_feature);
    }
    public aadl2_FeatureGroupTypeRename getAadl2_featuregrouptyperename() {
        return aadl2_featuregrouptyperename;
    }

    public void setAadl2_featuregrouptyperename(aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename) {
        this.aadl2_featuregrouptyperename = aadl2_featuregrouptyperename;
    }
    public List<aadl2_FeatureGroup> getAadl2_featuregroups() {
        return aadl2_featuregroups;
    }

    public void addAadl2_featuregroup(Aadl2_featuregroup aadl2_featuregroup) {
        this.aadl2_featuregroups.add(aadl2_featuregroup);
    }
    public List<aadl2_DataAccess> getAadl2_dataaccesss() {
        return aadl2_dataaccesss;
    }

    public void addAadl2_dataaccess(Aadl2_dataaccess aadl2_dataaccess) {
        this.aadl2_dataaccesss.add(aadl2_dataaccess);
    }
    public aadl2_PackageSection getAadl2_packagesection() {
        return aadl2_packagesection;
    }

    public void setAadl2_packagesection(aadl2_PackageSection aadl2_packagesection) {
        this.aadl2_packagesection = aadl2_packagesection;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_FeatureGroupPrototype getAadl2_featuregroupprototype() {
        return aadl2_featuregroupprototype;
    }

    public void setAadl2_featuregroupprototype(aadl2_FeatureGroupPrototype aadl2_featuregroupprototype) {
        this.aadl2_featuregroupprototype = aadl2_featuregroupprototype;
    }
    public List<aadl2_AbstractFeature> getAadl2_abstractfeatures() {
        return aadl2_abstractfeatures;
    }

    public void addAadl2_abstractfeature(Aadl2_abstractfeature aadl2_abstractfeature) {
        this.aadl2_abstractfeatures.add(aadl2_abstractfeature);
    }
    public aadl2_FeatureGroupReference getAadl2_featuregroupreference() {
        return aadl2_featuregroupreference;
    }

    public void setAadl2_featuregroupreference(aadl2_FeatureGroupReference aadl2_featuregroupreference) {
        this.aadl2_featuregroupreference = aadl2_featuregroupreference;
    }

}