





import java.util.List;
import java.util.ArrayList;

public class core_COREConcern extends CORENamedElement {






    private List<core_COREModel> core_coremodels;




    private core_COREModel core_coremodel;


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


    public List<core_COREModel> getCore_coremodels() {
        return core_coremodels;
    }

    public void addCore_coremodel(Core_coremodel core_coremodel) {
        this.core_coremodels.add(core_coremodel);
    }
    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }

}