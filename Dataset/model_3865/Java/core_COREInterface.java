





import java.util.List;
import java.util.ArrayList;

public class core_COREInterface  {






    private List<core_COREImpactNode> core_coreimpactnodes;




    private List<core_COREModelElement> core_coremodelelements;




    private List<core_COREModelElement> core_coremodelelements;




    private core_COREConcern core_coreconcern;




    private List<core_COREFeature> core_corefeatures;


    public core_COREInterface(
    ) {
        this.core_coreimpactnodes = new ArrayList<>();
        this.core_coremodelelements = new ArrayList<>();
        this.core_coremodelelements = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREInterface(
        ArrayList<core_COREImpactNode> core_coreimpactnodes,        ArrayList<core_COREModelElement> core_coremodelelements,        ArrayList<core_COREModelElement> core_coremodelelements,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_coreimpactnodes = core_coreimpactnodes;
        this.core_coremodelelements = core_coremodelelements;
        this.core_coremodelelements = core_coremodelelements;
        this.core_corefeatures = core_corefeatures;
    }


    public List<core_COREImpactNode> getCore_coreimpactnodes() {
        return core_coreimpactnodes;
    }

    public void addCore_coreimpactnode(Core_coreimpactnode core_coreimpactnode) {
        this.core_coreimpactnodes.add(core_coreimpactnode);
    }
    public List<core_COREModelElement> getCore_coremodelelements() {
        return core_coremodelelements;
    }

    public void addCore_coremodelelement(Core_coremodelelement core_coremodelelement) {
        this.core_coremodelelements.add(core_coremodelelement);
    }
    public List<core_COREModelElement> getCore_coremodelelements() {
        return core_coremodelelements;
    }

    public void addCore_coremodelelement(Core_coremodelelement core_coremodelelement) {
        this.core_coremodelelements.add(core_coremodelelement);
    }
    public core_COREConcern getCore_coreconcern() {
        return core_coreconcern;
    }

    public void setCore_coreconcern(core_COREConcern core_coreconcern) {
        this.core_coreconcern = core_coreconcern;
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }

}