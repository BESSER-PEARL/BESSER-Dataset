





import java.util.List;
import java.util.ArrayList;

public class graphbt_BEModel  {

    private String version;
    private String name;
    private String subtitle;





    private graphbt_RequirementList graphbt_requirementlist;




    private graphbt_ComponentList graphbt_componentlist;


    public graphbt_BEModel(
        String version,        String name,        String subtitle    ) {
        this.version = version;
        this.name = name;
        this.subtitle = subtitle;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubtitle() {
        return subtitle;
    }

    public void setSubtitle(String subtitle) {
        this.subtitle = subtitle;
    }

    public graphbt_RequirementList getGraphbt_requirementlist() {
        return graphbt_requirementlist;
    }

    public void setGraphbt_requirementlist(graphbt_RequirementList graphbt_requirementlist) {
        this.graphbt_requirementlist = graphbt_requirementlist;
    }
    public graphbt_ComponentList getGraphbt_componentlist() {
        return graphbt_componentlist;
    }

    public void setGraphbt_componentlist(graphbt_ComponentList graphbt_componentlist) {
        this.graphbt_componentlist = graphbt_componentlist;
    }

}