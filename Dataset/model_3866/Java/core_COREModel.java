





import java.util.List;
import java.util.ArrayList;

public class core_COREModel extends CORENamedElement {






    private List<core_COREFeature> core_corefeatures;




    private core_COREFeature core_corefeature;


    public core_COREModel(
    ) {
        super(
        );
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREModel(
        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_corefeatures = core_corefeatures;
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

}