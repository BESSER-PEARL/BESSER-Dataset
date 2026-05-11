





import java.util.List;
import java.util.ArrayList;

public class core_COREFeatureModel extends COREModel {






    private core_COREFeature core_corefeature;




    private List<core_COREFeature> core_corefeatures;




    private core_COREConcern core_coreconcern;


    public core_COREFeatureModel(
    ) {
        super(
        );
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREFeatureModel(
        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_corefeatures = core_corefeatures;
    }


    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public core_COREConcern getCore_coreconcern() {
        return core_coreconcern;
    }

    public void setCore_coreconcern(core_COREConcern core_coreconcern) {
        this.core_coreconcern = core_coreconcern;
    }

}