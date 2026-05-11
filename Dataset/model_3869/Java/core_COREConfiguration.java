





import java.util.List;
import java.util.ArrayList;

public class core_COREConfiguration extends CORENamedElement {






    private List<core_COREConcern> core_coreconcerns;




    private List<core_COREFeature> core_corefeatures;




    private core_COREFeature core_corefeature;




    private core_COREStrategy core_corestrategy;


    public core_COREConfiguration(
    ) {
        super(
        );
        this.core_coreconcerns = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREConfiguration(
        ArrayList<core_COREConcern> core_coreconcerns,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_coreconcerns = core_coreconcerns;
        this.core_corefeatures = core_corefeatures;
    }


    public List<core_COREConcern> getCore_coreconcerns() {
        return core_coreconcerns;
    }

    public void addCore_coreconcern(Core_coreconcern core_coreconcern) {
        this.core_coreconcerns.add(core_coreconcern);
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public core_COREStrategy getCore_corestrategy() {
        return core_corestrategy;
    }

    public void setCore_corestrategy(core_COREStrategy core_corestrategy) {
        this.core_corestrategy = core_corestrategy;
    }

}