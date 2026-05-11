





import java.util.List;
import java.util.ArrayList;

public class feature_HyFeatureModel  {






    private List<feature_HyEnum> feature_hyenums;




    private feature_HyGroup feature_hygroup;




    private List<feature_HyFeature> feature_hyfeatures;




    private List<feature_HyContextModel> feature_hycontextmodels;




    private List<feature_HyGroup> feature_hygroups;




    private feature_HyFeature feature_hyfeature;


    public feature_HyFeatureModel(
    ) {
        this.feature_hyenums = new ArrayList<>();
        this.feature_hyfeatures = new ArrayList<>();
        this.feature_hycontextmodels = new ArrayList<>();
        this.feature_hygroups = new ArrayList<>();
    }

    public feature_HyFeatureModel(
        ArrayList<feature_HyEnum> feature_hyenums,        ArrayList<feature_HyFeature> feature_hyfeatures,        ArrayList<feature_HyContextModel> feature_hycontextmodels,        ArrayList<feature_HyGroup> feature_hygroups    ) {
        this.feature_hyenums = feature_hyenums;
        this.feature_hyfeatures = feature_hyfeatures;
        this.feature_hycontextmodels = feature_hycontextmodels;
        this.feature_hygroups = feature_hygroups;
    }


    public List<feature_HyEnum> getFeature_hyenums() {
        return feature_hyenums;
    }

    public void addFeature_hyenum(Feature_hyenum feature_hyenum) {
        this.feature_hyenums.add(feature_hyenum);
    }
    public feature_HyGroup getFeature_hygroup() {
        return feature_hygroup;
    }

    public void setFeature_hygroup(feature_HyGroup feature_hygroup) {
        this.feature_hygroup = feature_hygroup;
    }
    public List<feature_HyFeature> getFeature_hyfeatures() {
        return feature_hyfeatures;
    }

    public void addFeature_hyfeature(Feature_hyfeature feature_hyfeature) {
        this.feature_hyfeatures.add(feature_hyfeature);
    }
    public List<feature_HyContextModel> getFeature_hycontextmodels() {
        return feature_hycontextmodels;
    }

    public void addFeature_hycontextmodel(Feature_hycontextmodel feature_hycontextmodel) {
        this.feature_hycontextmodels.add(feature_hycontextmodel);
    }
    public List<feature_HyGroup> getFeature_hygroups() {
        return feature_hygroups;
    }

    public void addFeature_hygroup(Feature_hygroup feature_hygroup) {
        this.feature_hygroups.add(feature_hygroup);
    }
    public feature_HyFeature getFeature_hyfeature() {
        return feature_hyfeature;
    }

    public void setFeature_hyfeature(feature_HyFeature feature_hyfeature) {
        this.feature_hyfeature = feature_hyfeature;
    }

}