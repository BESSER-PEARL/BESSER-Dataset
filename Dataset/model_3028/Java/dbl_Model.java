





import java.util.List;
import java.util.ArrayList;

public class dbl_Model  {






    private List<dbl_Module> dbl_modules;


    public dbl_Model(
    ) {
        this.dbl_modules = new ArrayList<>();
    }

    public dbl_Model(
        ArrayList<dbl_Module> dbl_modules    ) {
        this.dbl_modules = dbl_modules;
    }


    public List<dbl_Module> getDbl_modules() {
        return dbl_modules;
    }

    public void addDbl_module(Dbl_module dbl_module) {
        this.dbl_modules.add(dbl_module);
    }

}