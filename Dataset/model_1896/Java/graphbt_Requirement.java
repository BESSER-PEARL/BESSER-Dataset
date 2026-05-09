





import java.util.List;
import java.util.ArrayList;

public class graphbt_Requirement  {

    private String Key;
    private String Id;
    private String Requirement;
    private String Description;





    private List<graphbt_StandardNode> graphbt_standardnodes;


    public graphbt_Requirement(
        String Key,        String Id,        String Requirement,        String Description    ) {
        this.Key = Key;
        this.Id = Id;
        this.Requirement = Requirement;
        this.Description = Description;
        this.graphbt_standardnodes = new ArrayList<>();
    }

    public graphbt_Requirement(
        String Key,        String Id,        String Requirement,        String Description        ArrayList<graphbt_StandardNode> graphbt_standardnodes    ) {
        this.Key = Key;
        this.Id = Id;
        this.Requirement = Requirement;
        this.Description = Description;
        this.graphbt_standardnodes = graphbt_standardnodes;
    }

    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getRequirement() {
        return Requirement;
    }

    public void setRequirement(String Requirement) {
        this.Requirement = Requirement;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public List<graphbt_StandardNode> getGraphbt_standardnodes() {
        return graphbt_standardnodes;
    }

    public void addGraphbt_standardnode(Graphbt_standardnode graphbt_standardnode) {
        this.graphbt_standardnodes.add(graphbt_standardnode);
    }

}