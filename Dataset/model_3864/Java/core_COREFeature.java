





import java.util.List;
import java.util.ArrayList;

public class core_COREFeature extends COREModelElement {






    private core_COREModel core_coremodel;




    private core_COREReuse core_corereuse;




    private core_COREConfiguration core_coreconfiguration;




    private List<core_COREModel> core_coremodels;




    private List<core_COREStrategy> core_corestrategys;




    private List<core_COREConfiguration> core_coreconfigurations;


    public core_COREFeature(
    ) {
        super(
        );
        this.core_coremodels = new ArrayList<>();
        this.core_corestrategys = new ArrayList<>();
        this.core_coreconfigurations = new ArrayList<>();
    }

    public core_COREFeature(
        ArrayList<core_COREModel> core_coremodels,        ArrayList<core_COREStrategy> core_corestrategys,        ArrayList<core_COREConfiguration> core_coreconfigurations    ) {
        this.core_coremodels = core_coremodels;
        this.core_corestrategys = core_corestrategys;
        this.core_coreconfigurations = core_coreconfigurations;
    }


    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }
    public core_COREReuse getCore_corereuse() {
        return core_corereuse;
    }

    public void setCore_corereuse(core_COREReuse core_corereuse) {
        this.core_corereuse = core_corereuse;
    }
    public core_COREConfiguration getCore_coreconfiguration() {
        return core_coreconfiguration;
    }

    public void setCore_coreconfiguration(core_COREConfiguration core_coreconfiguration) {
        this.core_coreconfiguration = core_coreconfiguration;
    }
    public List<core_COREModel> getCore_coremodels() {
        return core_coremodels;
    }

    public void addCore_coremodel(Core_coremodel core_coremodel) {
        this.core_coremodels.add(core_coremodel);
    }
    public List<core_COREStrategy> getCore_corestrategys() {
        return core_corestrategys;
    }

    public void addCore_corestrategy(Core_corestrategy core_corestrategy) {
        this.core_corestrategys.add(core_corestrategy);
    }
    public List<core_COREConfiguration> getCore_coreconfigurations() {
        return core_coreconfigurations;
    }

    public void addCore_coreconfiguration(Core_coreconfiguration core_coreconfiguration) {
        this.core_coreconfigurations.add(core_coreconfiguration);
    }

}