





import java.util.List;
import java.util.ArrayList;

public class core_COREConcern extends CORENamedElement {






    private core_COREModel core_coremodel;




    private List<core_COREModel> core_coremodels;




    private core_COREFeatureModel core_corefeaturemodel;




    private core_COREInterface core_coreinterface;




    private core_COREReuse core_corereuse;


    public core_COREConcern(
    ) {
        super(
        );
        this.core_coremodels = new ArrayList<>();
    }

    public core_COREConcern(
        ArrayList<core_COREModel> core_coremodels    ) {
        this.core_coremodels = core_coremodels;
    }


    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }
    public List<core_COREModel> getCore_coremodels() {
        return core_coremodels;
    }

    public void addCore_coremodel(Core_coremodel core_coremodel) {
        this.core_coremodels.add(core_coremodel);
    }
    public core_COREFeatureModel getCore_corefeaturemodel() {
        return core_corefeaturemodel;
    }

    public void setCore_corefeaturemodel(core_COREFeatureModel core_corefeaturemodel) {
        this.core_corefeaturemodel = core_corefeaturemodel;
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

}