





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroupType extends FeatureType, Classifier {






    private List<aadl2_DataPort> aadl2_dataports;




    private List<aadl2_Parameter> aadl2_parameters;




    private List<aadl2_FeatureGroup> aadl2_featuregroups;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private List<aadl2_AbstractFeature> aadl2_abstractfeatures;




    private aadl2_FeatureGroupPrototype aadl2_featuregroupprototype;




    private aadl2_GroupExtension aadl2_groupextension;




    private List<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss;




    private aadl2_FeatureGroup aadl2_featuregroup;




    private aadl2_GroupExtension aadl2_groupextension;




    private List<aadl2_Feature> aadl2_features;




    private aadl2_FeatureGroupTypeRename aadl2_featuregrouptyperename;




    private List<aadl2_DataAccess> aadl2_dataaccesss;




    private List<aadl2_EventDataPort> aadl2_eventdataports;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;


    public aadl2_FeatureGroupType(
    ) {
        super(
        );
        this.aadl2_dataports = new ArrayList<>();
        this.aadl2_parameters = new ArrayList<>();
        this.aadl2_featuregroups = new ArrayList<>();
        this.aadl2_abstractfeatures = new ArrayList<>();
        this.aadl2_subprogramgroupaccesss = new ArrayList<>();
        this.aadl2_features = new ArrayList<>();
        this.aadl2_dataaccesss = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
    }

    public aadl2_FeatureGroupType(
        ArrayList<aadl2_DataPort> aadl2_dataports,        ArrayList<aadl2_Parameter> aadl2_parameters,        ArrayList<aadl2_FeatureGroup> aadl2_featuregroups,        ArrayList<aadl2_AbstractFeature> aadl2_abstractfeatures,        ArrayList<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss,        ArrayList<aadl2_Feature> aadl2_features,        ArrayList<aadl2_DataAccess> aadl2_dataaccesss,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports    ) {
        this.aadl2_dataports = aadl2_dataports;
        this.aadl2_parameters = aadl2_parameters;
        this.aadl2_featuregroups = aadl2_featuregroups;
        this.aadl2_abstractfeatures = aadl2_abstractfeatures;
        this.aadl2_subprogramgroupaccesss = aadl2_subprogramgroupaccesss;
        this.aadl2_features = aadl2_features;
        this.aadl2_dataaccesss = aadl2_dataaccesss;
        this.aadl2_eventdataports = aadl2_eventdataports;
    }


    public List<aadl2_DataPort> getAadl2_dataports() {
        return aadl2_dataports;
    }

    public void addAadl2_dataport(Aadl2_dataport aadl2_dataport) {
        this.aadl2_dataports.add(aadl2_dataport);
    }
    public List<aadl2_Parameter> getAadl2_parameters() {
        return aadl2_parameters;
    }

    public void addAadl2_parameter(Aadl2_parameter aadl2_parameter) {
        this.aadl2_parameters.add(aadl2_parameter);
    }
    public List<aadl2_FeatureGroup> getAadl2_featuregroups() {
        return aadl2_featuregroups;
    }

    public void addAadl2_featuregroup(Aadl2_featuregroup aadl2_featuregroup) {
        this.aadl2_featuregroups.add(aadl2_featuregroup);
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public List<aadl2_AbstractFeature> getAadl2_abstractfeatures() {
        return aadl2_abstractfeatures;
    }

    public void addAadl2_abstractfeature(Aadl2_abstractfeature aadl2_abstractfeature) {
        this.aadl2_abstractfeatures.add(aadl2_abstractfeature);
    }
    public aadl2_FeatureGroupPrototype getAadl2_featuregroupprototype() {
        return aadl2_featuregroupprototype;
    }

    public void setAadl2_featuregroupprototype(aadl2_FeatureGroupPrototype aadl2_featuregroupprototype) {
        this.aadl2_featuregroupprototype = aadl2_featuregroupprototype;
    }
    public aadl2_GroupExtension getAadl2_groupextension() {
        return aadl2_groupextension;
    }

    public void setAadl2_groupextension(aadl2_GroupExtension aadl2_groupextension) {
        this.aadl2_groupextension = aadl2_groupextension;
    }
    public List<aadl2_SubprogramGroupAccess> getAadl2_subprogramgroupaccesss() {
        return aadl2_subprogramgroupaccesss;
    }

    public void addAadl2_subprogramgroupaccess(Aadl2_subprogramgroupaccess aadl2_subprogramgroupaccess) {
        this.aadl2_subprogramgroupaccesss.add(aadl2_subprogramgroupaccess);
    }
    public aadl2_FeatureGroup getAadl2_featuregroup() {
        return aadl2_featuregroup;
    }

    public void setAadl2_featuregroup(aadl2_FeatureGroup aadl2_featuregroup) {
        this.aadl2_featuregroup = aadl2_featuregroup;
    }
    public aadl2_GroupExtension getAadl2_groupextension() {
        return aadl2_groupextension;
    }

    public void setAadl2_groupextension(aadl2_GroupExtension aadl2_groupextension) {
        this.aadl2_groupextension = aadl2_groupextension;
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
    public List<aadl2_DataAccess> getAadl2_dataaccesss() {
        return aadl2_dataaccesss;
    }

    public void addAadl2_dataaccess(Aadl2_dataaccess aadl2_dataaccess) {
        this.aadl2_dataaccesss.add(aadl2_dataaccess);
    }
    public List<aadl2_EventDataPort> getAadl2_eventdataports() {
        return aadl2_eventdataports;
    }

    public void addAadl2_eventdataport(Aadl2_eventdataport aadl2_eventdataport) {
        this.aadl2_eventdataports.add(aadl2_eventdataport);
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }

}