





import java.util.List;
import java.util.ArrayList;

public class henshin_TransformationSystem extends NamedElement {






    private List<henshin_Rule> henshin_rules;




    private List<henshin_Graph> henshin_graphs;




    private List<henshin_TransformationUnit> henshin_transformationunits;




    private List<henshin_EPackage> henshin_epackages;


    public henshin_TransformationSystem(
    ) {
        super(
        );
        this.henshin_rules = new ArrayList<>();
        this.henshin_graphs = new ArrayList<>();
        this.henshin_transformationunits = new ArrayList<>();
        this.henshin_epackages = new ArrayList<>();
    }

    public henshin_TransformationSystem(
        ArrayList<henshin_Rule> henshin_rules,        ArrayList<henshin_Graph> henshin_graphs,        ArrayList<henshin_TransformationUnit> henshin_transformationunits,        ArrayList<henshin_EPackage> henshin_epackages    ) {
        this.henshin_rules = henshin_rules;
        this.henshin_graphs = henshin_graphs;
        this.henshin_transformationunits = henshin_transformationunits;
        this.henshin_epackages = henshin_epackages;
    }


    public List<henshin_Rule> getHenshin_rules() {
        return henshin_rules;
    }

    public void addHenshin_rule(Henshin_rule henshin_rule) {
        this.henshin_rules.add(henshin_rule);
    }
    public List<henshin_Graph> getHenshin_graphs() {
        return henshin_graphs;
    }

    public void addHenshin_graph(Henshin_graph henshin_graph) {
        this.henshin_graphs.add(henshin_graph);
    }
    public List<henshin_TransformationUnit> getHenshin_transformationunits() {
        return henshin_transformationunits;
    }

    public void addHenshin_transformationunit(Henshin_transformationunit henshin_transformationunit) {
        this.henshin_transformationunits.add(henshin_transformationunit);
    }
    public List<henshin_EPackage> getHenshin_epackages() {
        return henshin_epackages;
    }

    public void addHenshin_epackage(Henshin_epackage henshin_epackage) {
        this.henshin_epackages.add(henshin_epackage);
    }

}