





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_ModuleCache  {

    private String version;





    private mancoosimm_Module mancoosimm_module;




    private mancoosimm_Environment mancoosimm_environment;




    private List<mancoosimm_Module> mancoosimm_modules;




    private mancoosimm_Environment mancoosimm_environment;


    public mancoosimm_ModuleCache(
        String version    ) {
        this.version = version;
        this.mancoosimm_modules = new ArrayList<>();
    }

    public mancoosimm_ModuleCache(
        String version        ArrayList<mancoosimm_Module> mancoosimm_modules    ) {
        this.version = version;
        this.mancoosimm_modules = mancoosimm_modules;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public mancoosimm_Module getMancoosimm_module() {
        return mancoosimm_module;
    }

    public void setMancoosimm_module(mancoosimm_Module mancoosimm_module) {
        this.mancoosimm_module = mancoosimm_module;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public List<mancoosimm_Module> getMancoosimm_modules() {
        return mancoosimm_modules;
    }

    public void addMancoosimm_module(Mancoosimm_module mancoosimm_module) {
        this.mancoosimm_modules.add(mancoosimm_module);
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }

}