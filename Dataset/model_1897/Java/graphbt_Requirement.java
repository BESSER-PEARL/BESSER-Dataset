





import java.util.List;
import java.util.ArrayList;

public class graphbt_Requirement  {

    private String Requirement;
    private String Id;
    private String Key;
    private String Description;





    private graphbt_RequirementList graphbt_requirementlist;




    private List<graphbt_StandardNode> graphbt_standardnodes;


    public graphbt_Requirement(
        String Requirement,        String Id,        String Key,        String Description    ) {
        this.Requirement = Requirement;
        this.Id = Id;
        this.Key = Key;
        this.Description = Description;
        this.graphbt_standardnodes = new ArrayList<>();
    }

    public graphbt_Requirement(
        String Requirement,        String Id,        String Key,        String Description        ArrayList<graphbt_StandardNode> graphbt_standardnodes    ) {
        this.Requirement = Requirement;
        this.Id = Id;
        this.Key = Key;
        this.Description = Description;
        this.graphbt_standardnodes = graphbt_standardnodes;
    }

    public String getRequirement() {
        return Requirement;
    }

    public void setRequirement(String Requirement) {
        this.Requirement = Requirement;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
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

}