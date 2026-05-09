





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends Unit {

    private boolean injectiveMatching;
    private boolean checkDangling;
    private String javaImports;





    private List<henshin_Mapping> henshin_mappings;




    private henshin_Graph henshin_graph;




    private List<henshin_Rule> henshin_rules;




    private henshin_Graph henshin_graph;




    private List<henshin_Mapping> henshin_mappings;


    public henshin_Rule(
        boolean injectiveMatching,        boolean checkDangling,        String javaImports    ) {
        super(
        );
        this.injectiveMatching = injectiveMatching;
        this.checkDangling = checkDangling;
        this.javaImports = javaImports;
        this.henshin_mappings = new ArrayList<>();
        this.henshin_rules = new ArrayList<>();
        this.henshin_mappings = new ArrayList<>();
    }

    public henshin_Rule(
        boolean injectiveMatching,        boolean checkDangling,        String javaImports        ArrayList<henshin_Mapping> henshin_mappings,        ArrayList<henshin_Rule> henshin_rules,        ArrayList<henshin_Mapping> henshin_mappings    ) {
        this.injectiveMatching = injectiveMatching;
        this.checkDangling = checkDangling;
        this.javaImports = javaImports;
        this.henshin_mappings = henshin_mappings;
        this.henshin_rules = henshin_rules;
        this.henshin_mappings = henshin_mappings;
    }

    public boolean getInjectivematching() {
        return injectiveMatching;
    }

    public void setInjectivematching(boolean injectiveMatching) {
        this.injectiveMatching = injectiveMatching;
    }
    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }
    public String getJavaimports() {
        return javaImports;
    }

    public void setJavaimports(String javaImports) {
        this.javaImports = javaImports;
    }

    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public List<henshin_Rule> getHenshin_rules() {
        return henshin_rules;
    }

    public void addHenshin_rule(Henshin_rule henshin_rule) {
        this.henshin_rules.add(henshin_rule);
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }

}