





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends Unit {

    private boolean checkDangling;
    private boolean injectiveMatching;
    private String javaImports;





    private henshin_AttributeCondition henshin_attributecondition;




    private henshin_Graph henshin_graph;




    private List<henshin_AttributeCondition> henshin_attributeconditions;




    private henshin_Graph henshin_graph;




    private henshin_Rule henshin_rule;


    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String javaImports    ) {
        super(
        );
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.javaImports = javaImports;
        this.henshin_attributeconditions = new ArrayList<>();
    }

    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String javaImports        ArrayList<henshin_AttributeCondition> henshin_attributeconditions    ) {
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.javaImports = javaImports;
        this.henshin_attributeconditions = henshin_attributeconditions;
    }

    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }
    public boolean getInjectivematching() {
        return injectiveMatching;
    }

    public void setInjectivematching(boolean injectiveMatching) {
        this.injectiveMatching = injectiveMatching;
    }
    public String getJavaimports() {
        return javaImports;
    }

    public void setJavaimports(String javaImports) {
        this.javaImports = javaImports;
    }

    public henshin_AttributeCondition getHenshin_attributecondition() {
        return henshin_attributecondition;
    }

    public void setHenshin_attributecondition(henshin_AttributeCondition henshin_attributecondition) {
        this.henshin_attributecondition = henshin_attributecondition;
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public List<henshin_AttributeCondition> getHenshin_attributeconditions() {
        return henshin_attributeconditions;
    }

    public void addHenshin_attributecondition(Henshin_attributecondition henshin_attributecondition) {
        this.henshin_attributeconditions.add(henshin_attributecondition);
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }

}