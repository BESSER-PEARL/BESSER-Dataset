





import java.util.List;
import java.util.ArrayList;

public class henshin_Module extends NamedElement {






    private henshin_Module henshin_module;




    private List<henshin_Module> henshin_modules;


    public henshin_Module(
    ) {
        super(
        );
        this.henshin_modules = new ArrayList<>();
    }

    public henshin_Module(
        ArrayList<henshin_Module> henshin_modules    ) {
        this.henshin_modules = henshin_modules;
    }


    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }
    public List<henshin_Module> getHenshin_modules() {
        return henshin_modules;
    }

    public void addHenshin_module(Henshin_module henshin_module) {
        this.henshin_modules.add(henshin_module);
    }

}