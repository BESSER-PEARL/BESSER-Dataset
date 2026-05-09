





import java.util.List;
import java.util.ArrayList;

public class graphbt_BEModel  {

    private String subtitle;
    private String name;
    private String version;





    private graphbt_AuthorList graphbt_authorlist;




    private graphbt_RequirementList graphbt_requirementlist;




    private List<graphbt_StandardNode> graphbt_standardnodes;




    private graphbt_ComponentList graphbt_componentlist;




    private graphbt_Libraries graphbt_libraries;




    private List<graphbt_StandardNode> graphbt_standardnodes;




    private graphbt_FormulaList graphbt_formulalist;




    private graphbt_LayoutList graphbt_layoutlist;


    public graphbt_BEModel(
        String subtitle,        String name,        String version    ) {
        this.subtitle = subtitle;
        this.name = name;
        this.version = version;
        this.graphbt_standardnodes = new ArrayList<>();
        this.graphbt_standardnodes = new ArrayList<>();
    }

    public graphbt_BEModel(
        String subtitle,        String name,        String version        ArrayList<graphbt_StandardNode> graphbt_standardnodes,        ArrayList<graphbt_StandardNode> graphbt_standardnodes    ) {
        this.subtitle = subtitle;
        this.name = name;
        this.version = version;
        this.graphbt_standardnodes = graphbt_standardnodes;
        this.graphbt_standardnodes = graphbt_standardnodes;
    }

    public String getSubtitle() {
        return subtitle;
    }

    public void setSubtitle(String subtitle) {
        this.subtitle = subtitle;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public graphbt_AuthorList getGraphbt_authorlist() {
        return graphbt_authorlist;
    }

    public void setGraphbt_authorlist(graphbt_AuthorList graphbt_authorlist) {
        this.graphbt_authorlist = graphbt_authorlist;
    }
    public graphbt_RequirementList getGraphbt_requirementlist() {
        return graphbt_requirementlist;
    }

    public void setGraphbt_requirementlist(graphbt_RequirementList graphbt_requirementlist) {
        this.graphbt_requirementlist = graphbt_requirementlist;
    }
    public List<graphbt_StandardNode> getGraphbt_standardnodes() {
        return graphbt_standardnodes;
    }

    public void addGraphbt_standardnode(Graphbt_standardnode graphbt_standardnode) {
        this.graphbt_standardnodes.add(graphbt_standardnode);
    }
    public graphbt_ComponentList getGraphbt_componentlist() {
        return graphbt_componentlist;
    }

    public void setGraphbt_componentlist(graphbt_ComponentList graphbt_componentlist) {
        this.graphbt_componentlist = graphbt_componentlist;
    }
    public graphbt_Libraries getGraphbt_libraries() {
        return graphbt_libraries;
    }

    public void setGraphbt_libraries(graphbt_Libraries graphbt_libraries) {
        this.graphbt_libraries = graphbt_libraries;
    }
    public List<graphbt_StandardNode> getGraphbt_standardnodes() {
        return graphbt_standardnodes;
    }

    public void addGraphbt_standardnode(Graphbt_standardnode graphbt_standardnode) {
        this.graphbt_standardnodes.add(graphbt_standardnode);
    }
    public graphbt_FormulaList getGraphbt_formulalist() {
        return graphbt_formulalist;
    }

    public void setGraphbt_formulalist(graphbt_FormulaList graphbt_formulalist) {
        this.graphbt_formulalist = graphbt_formulalist;
    }
    public graphbt_LayoutList getGraphbt_layoutlist() {
        return graphbt_layoutlist;
    }

    public void setGraphbt_layoutlist(graphbt_LayoutList graphbt_layoutlist) {
        this.graphbt_layoutlist = graphbt_layoutlist;
    }

}