





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Model  {






    private List<odemcustom_Module> odemcustom_modules;


    public odemcustom_Model(
    ) {
        this.odemcustom_modules = new ArrayList<>();
    }

    public odemcustom_Model(
        ArrayList<odemcustom_Module> odemcustom_modules    ) {
        this.odemcustom_modules = odemcustom_modules;
    }


    public List<odemcustom_Module> getOdemcustom_modules() {
        return odemcustom_modules;
    }

    public void addOdemcustom_module(Odemcustom_module odemcustom_module) {
        this.odemcustom_modules.add(odemcustom_module);
    }

}