





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Menu  {






    private mancoosimm_MenuEntry mancoosimm_menuentry;




    private mancoosimm_ApplicationMenuCatalog mancoosimm_applicationmenucatalog;




    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_Environment mancoosimm_environment;




    private List<mancoosimm_MenuEntry> mancoosimm_menuentrys;




    private mancoosimm_ApplicationMenuCatalog mancoosimm_applicationmenucatalog;


    public mancoosimm_Menu(
    ) {
        this.mancoosimm_menuentrys = new ArrayList<>();
    }

    public mancoosimm_Menu(
        ArrayList<mancoosimm_MenuEntry> mancoosimm_menuentrys    ) {
        this.mancoosimm_menuentrys = mancoosimm_menuentrys;
    }


    public mancoosimm_MenuEntry getMancoosimm_menuentry() {
        return mancoosimm_menuentry;
    }

    public void setMancoosimm_menuentry(mancoosimm_MenuEntry mancoosimm_menuentry) {
        this.mancoosimm_menuentry = mancoosimm_menuentry;
    }
    public mancoosimm_ApplicationMenuCatalog getMancoosimm_applicationmenucatalog() {
        return mancoosimm_applicationmenucatalog;
    }

    public void setMancoosimm_applicationmenucatalog(mancoosimm_ApplicationMenuCatalog mancoosimm_applicationmenucatalog) {
        this.mancoosimm_applicationmenucatalog = mancoosimm_applicationmenucatalog;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public List<mancoosimm_MenuEntry> getMancoosimm_menuentrys() {
        return mancoosimm_menuentrys;
    }

    public void addMancoosimm_menuentry(Mancoosimm_menuentry mancoosimm_menuentry) {
        this.mancoosimm_menuentrys.add(mancoosimm_menuentry);
    }
    public mancoosimm_ApplicationMenuCatalog getMancoosimm_applicationmenucatalog() {
        return mancoosimm_applicationmenucatalog;
    }

    public void setMancoosimm_applicationmenucatalog(mancoosimm_ApplicationMenuCatalog mancoosimm_applicationmenucatalog) {
        this.mancoosimm_applicationmenucatalog = mancoosimm_applicationmenucatalog;
    }

}