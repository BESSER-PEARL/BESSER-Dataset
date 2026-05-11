





import java.util.List;
import java.util.ArrayList;

public class core_COREConfiguration  {






    private List<core_COREFeature> core_corefeatures;




    private core_COREInterface core_coreinterface;


    public core_COREConfiguration(
    ) {
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREConfiguration(
        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_corefeatures = core_corefeatures;
    }


    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
    }

}