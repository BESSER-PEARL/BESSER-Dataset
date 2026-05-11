





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroupType extends FeatureType, Classifier {






    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename;




    private aadl2_FeatureGroup aadl2_featuregroup;




    private List<aadl2_FeatureGroup> aadl2_featuregroups;




    private List<aadl2_SubprogramAccess> aadl2_subprogramaccesss;




    private List<aadl2_AbstractFeature> aadl2_abstractfeatures;




    private List<aadl2_Feature> aadl2_features;


    public aadl2_FeatureGroupType(
    ) {
        super(
        );
        this.aadl2_featuregroups = new ArrayList<>();
        this.aadl2_subprogramaccesss = new ArrayList<>();
        this.aadl2_abstractfeatures = new ArrayList<>();
        this.aadl2_features = new ArrayList<>();
    }

    public aadl2_FeatureGroupType(
        ArrayList<aadl2_FeatureGroup> aadl2_featuregroups,        ArrayList<aadl2_SubprogramAccess> aadl2_subprogramaccesss,        ArrayList<aadl2_AbstractFeature> aadl2_abstractfeatures,        ArrayList<aadl2_Feature> aadl2_features    ) {
        this.aadl2_featuregroups = aadl2_featuregroups;
        this.aadl2_subprogramaccesss = aadl2_subprogramaccesss;
        this.aadl2_abstractfeatures = aadl2_abstractfeatures;
        this.aadl2_features = aadl2_features;
    }


    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_FeatureGroupTypeRename getAadl2_featuregrouptyperename() {
        return aadl2_featuregrouptyperename;
    }

    public void setAadl2_featuregrouptyperename(aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename) {
        this.aadl2_featuregrouptyperename = aadl2_featuregrouptyperename;
    }
    public aadl2_FeatureGroup getAadl2_featuregroup() {
        return aadl2_featuregroup;
    }

    public void setAadl2_featuregroup(aadl2_FeatureGroup aadl2_featuregroup) {
        this.aadl2_featuregroup = aadl2_featuregroup;
    }
    public List<aadl2_FeatureGroup> getAadl2_featuregroups() {
        return aadl2_featuregroups;
    }

    public void addAadl2_featuregroup(Aadl2_featuregroup aadl2_featuregroup) {
        this.aadl2_featuregroups.add(aadl2_featuregroup);
    }
    public List<aadl2_SubprogramAccess> getAadl2_subprogramaccesss() {
        return aadl2_subprogramaccesss;
    }

    public void addAadl2_subprogramaccess(Aadl2_subprogramaccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccesss.add(aadl2_subprogramaccess);
    }
    public List<aadl2_AbstractFeature> getAadl2_abstractfeatures() {
        return aadl2_abstractfeatures;
    }

    public void addAadl2_abstractfeature(Aadl2_abstractfeature aadl2_abstractfeature) {
        this.aadl2_abstractfeatures.add(aadl2_abstractfeature);
    }
    public List<aadl2_Feature> getAadl2_features() {
        return aadl2_features;
    }

    public void addAadl2_feature(Aadl2_feature aadl2_feature) {
        this.aadl2_features.add(aadl2_feature);
    }

}