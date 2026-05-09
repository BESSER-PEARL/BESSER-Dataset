





import java.util.List;
import java.util.ArrayList;

public class henshin_Module extends NamedElement {






    private List<henshin_Unit> henshin_units;




    private List<henshin_Graph> henshin_graphs;




    private List<henshin_EPackage> henshin_epackages;




    private henshin_Module henshin_module;




    private List<henshin_Module> henshin_modules;


    public henshin_Module(
    ) {
        super(
        );
        this.henshin_units = new ArrayList<>();
        this.henshin_graphs = new ArrayList<>();
        this.henshin_epackages = new ArrayList<>();
        this.henshin_modules = new ArrayList<>();
    }

    public henshin_Module(
        ArrayList<henshin_Unit> henshin_units,        ArrayList<henshin_Graph> henshin_graphs,        ArrayList<henshin_EPackage> henshin_epackages,        ArrayList<henshin_Module> henshin_modules    ) {
        this.henshin_units = henshin_units;
        this.henshin_graphs = henshin_graphs;
        this.henshin_epackages = henshin_epackages;
        this.henshin_modules = henshin_modules;
    }


    public List<henshin_Unit> getHenshin_units() {
        return henshin_units;
    }

    public void addHenshin_unit(Henshin_unit henshin_unit) {
        this.henshin_units.add(henshin_unit);
    }
    public List<henshin_Graph> getHenshin_graphs() {
        return henshin_graphs;
    }

    public void addHenshin_graph(Henshin_graph henshin_graph) {
        this.henshin_graphs.add(henshin_graph);
    }
    public List<henshin_EPackage> getHenshin_epackages() {
        return henshin_epackages;
    }

    public void addHenshin_epackage(Henshin_epackage henshin_epackage) {
        this.henshin_epackages.add(henshin_epackage);
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