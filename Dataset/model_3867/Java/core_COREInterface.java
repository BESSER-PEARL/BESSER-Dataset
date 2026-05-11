





import java.util.List;
import java.util.ArrayList;

public class core_COREInterface  {






    private List<core_COREFeature> core_corefeatures;




    private core_COREConcern core_coreconcern;




    private List<core_COREImpactModelElement> core_coreimpactmodelelements;




    private List<core_COREModelElement> core_coremodelelements;




    private List<core_COREModelElement> core_coremodelelements;


    public core_COREInterface(
    ) {
        this.core_corefeatures = new ArrayList<>();
        this.core_coreimpactmodelelements = new ArrayList<>();
        this.core_coremodelelements = new ArrayList<>();
        this.core_coremodelelements = new ArrayList<>();
    }

    public core_COREInterface(
        ArrayList<core_COREFeature> core_corefeatures,        ArrayList<core_COREImpactModelElement> core_coreimpactmodelelements,        ArrayList<core_COREModelElement> core_coremodelelements,        ArrayList<core_COREModelElement> core_coremodelelements    ) {
        this.core_corefeatures = core_corefeatures;
        this.core_coreimpactmodelelements = core_coreimpactmodelelements;
        this.core_coremodelelements = core_coremodelelements;
        this.core_coremodelelements = core_coremodelelements;
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
    public List<core_COREImpactModelElement> getCore_coreimpactmodelelements() {
        return core_coreimpactmodelelements;
    }

    public void addCore_coreimpactmodelelement(Core_coreimpactmodelelement core_coreimpactmodelelement) {
        this.core_coreimpactmodelelements.add(core_coreimpactmodelelement);
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

}