





import java.util.List;
import java.util.ArrayList;

public class core_COREConfiguration extends CORENamedElement {






    private core_COREReuse core_corereuse;




    private core_COREReuse core_corereuse;




    private List<core_COREFeature> core_corefeatures;




    private List<core_COREFeature> core_corefeatures;


    public core_COREConfiguration(
    ) {
        super(
        );
        this.core_corefeatures = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREConfiguration(
        ArrayList<core_COREFeature> core_corefeatures,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_corefeatures = core_corefeatures;
        this.core_corefeatures = core_corefeatures;
    }


    public core_COREReuse getCore_corereuse() {
        return core_corereuse;
    }

    public void setCore_corereuse(core_COREReuse core_corereuse) {
        this.core_corereuse = core_corereuse;
    }
    public core_COREReuse getCore_corereuse() {
        return core_corereuse;
    }

    public void setCore_corereuse(core_COREReuse core_corereuse) {
        this.core_corereuse = core_corereuse;
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }

}