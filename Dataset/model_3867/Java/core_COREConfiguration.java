





import java.util.List;
import java.util.ArrayList;

public class core_COREConfiguration  {






    private core_COREInterface core_coreinterface;




    private core_COREReuse core_corereuse;




    private List<core_COREConfiguration> core_coreconfigurations;




    private core_COREReuse core_corereuse;




    private List<core_COREFeature> core_corefeatures;




    private List<core_COREFeature> core_corefeatures;


    public core_COREConfiguration(
    ) {
        this.core_coreconfigurations = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREConfiguration(
        ArrayList<core_COREConfiguration> core_coreconfigurations,        ArrayList<core_COREFeature> core_corefeatures,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_coreconfigurations = core_coreconfigurations;
        this.core_corefeatures = core_corefeatures;
        this.core_corefeatures = core_corefeatures;
    }


    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
    }
    public core_COREReuse getCore_corereuse() {
        return core_corereuse;
    }

    public void setCore_corereuse(core_COREReuse core_corereuse) {
        this.core_corereuse = core_corereuse;
    }
    public List<core_COREConfiguration> getCore_coreconfigurations() {
        return core_coreconfigurations;
    }

    public void addCore_coreconfiguration(Core_coreconfiguration core_coreconfiguration) {
        this.core_coreconfigurations.add(core_coreconfiguration);
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