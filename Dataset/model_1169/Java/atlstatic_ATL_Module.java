





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_Module extends Unit {

    private String isRefining;





    private List<ModuleElement> moduleelements;


    public atlstatic_ATL_Module(
        String isRefining    ) {
        super(
        );
        this.isRefining = isRefining;
        this.moduleelements = new ArrayList<>();
    }

    public atlstatic_ATL_Module(
        String isRefining        ArrayList<ModuleElement> moduleelements    ) {
        this.isRefining = isRefining;
        this.moduleelements = moduleelements;
    }

    public String getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(String isRefining) {
        this.isRefining = isRefining;
    }

    public List<ModuleElement> getModuleelements() {
        return moduleelements;
    }

    public void addModuleelement(Moduleelement moduleelement) {
        this.moduleelements.add(moduleelement);
    }

}