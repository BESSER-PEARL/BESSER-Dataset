





import java.util.List;
import java.util.ArrayList;

public class core_COREImpactModel extends COREModel {






    private core_COREConcern core_coreconcern;




    private List<core_LayoutContainerMap> core_layoutcontainermaps;




    private List<core_COREContribution> core_corecontributions;




    private List<core_COREImpactNode> core_coreimpactnodes;


    public core_COREImpactModel(
    ) {
        super(
        );
        this.core_layoutcontainermaps = new ArrayList<>();
        this.core_corecontributions = new ArrayList<>();
        this.core_coreimpactnodes = new ArrayList<>();
    }

    public core_COREImpactModel(
        ArrayList<core_LayoutContainerMap> core_layoutcontainermaps,        ArrayList<core_COREContribution> core_corecontributions,        ArrayList<core_COREImpactNode> core_coreimpactnodes    ) {
        this.core_layoutcontainermaps = core_layoutcontainermaps;
        this.core_corecontributions = core_corecontributions;
        this.core_coreimpactnodes = core_coreimpactnodes;
    }


    public core_COREConcern getCore_coreconcern() {
        return core_coreconcern;
    }

    public void setCore_coreconcern(core_COREConcern core_coreconcern) {
        this.core_coreconcern = core_coreconcern;
    }
    public List<core_LayoutContainerMap> getCore_layoutcontainermaps() {
        return core_layoutcontainermaps;
    }

    public void addCore_layoutcontainermap(Core_layoutcontainermap core_layoutcontainermap) {
        this.core_layoutcontainermaps.add(core_layoutcontainermap);
    }
    public List<core_COREContribution> getCore_corecontributions() {
        return core_corecontributions;
    }

    public void addCore_corecontribution(Core_corecontribution core_corecontribution) {
        this.core_corecontributions.add(core_corecontribution);
    }
    public List<core_COREImpactNode> getCore_coreimpactnodes() {
        return core_coreimpactnodes;
    }

    public void addCore_coreimpactnode(Core_coreimpactnode core_coreimpactnode) {
        this.core_coreimpactnodes.add(core_coreimpactnode);
    }

}