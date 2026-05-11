





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroupType extends Classifier, FeatureType {






    private List<aadl2_Feature> aadl2_features;




    private aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;


    public aadl2_FeatureGroupType(
    ) {
        super(
        );
        this.aadl2_features = new ArrayList<>();
    }

    public aadl2_FeatureGroupType(
        ArrayList<aadl2_Feature> aadl2_features    ) {
        this.aadl2_features = aadl2_features;
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

}