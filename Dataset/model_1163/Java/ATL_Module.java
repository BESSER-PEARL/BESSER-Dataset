





import java.util.List;
import java.util.ArrayList;

public class ATL_Module extends Unit {

    private String isRefining;





    private List<OclModel> oclmodels;




    private List<OclModel> oclmodels;




    private List<ModuleElement> moduleelements;


    public ATL_Module(
        String isRefining    ) {
        super(
        );
        this.isRefining = isRefining;
        this.oclmodels = new ArrayList<>();
        this.oclmodels = new ArrayList<>();
        this.moduleelements = new ArrayList<>();
    }

    public ATL_Module(
        String isRefining        ArrayList<OclModel> oclmodels,        ArrayList<OclModel> oclmodels,        ArrayList<ModuleElement> moduleelements    ) {
        this.isRefining = isRefining;
        this.oclmodels = oclmodels;
        this.oclmodels = oclmodels;
        this.moduleelements = moduleelements;
    }

    public String getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(String isRefining) {
        this.isRefining = isRefining;
    }

    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }
    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }
    public List<ModuleElement> getModuleelements() {
        return moduleelements;
    }

    public void addModuleelement(Moduleelement moduleelement) {
        this.moduleelements.add(moduleelement);
    }

}