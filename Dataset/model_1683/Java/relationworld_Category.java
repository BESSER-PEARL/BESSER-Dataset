





import java.util.List;
import java.util.ArrayList;

public class relationworld_Category  {

    private String nom;





    private List<relationworld_SourceNode> relationworld_sourcenodes;




    private List<relationworld_TargetNode> relationworld_targetnodes;




    private List<relationworld_Arrow> relationworld_arrows;


    public relationworld_Category(
        String nom    ) {
        this.nom = nom;
        this.relationworld_sourcenodes = new ArrayList<>();
        this.relationworld_targetnodes = new ArrayList<>();
        this.relationworld_arrows = new ArrayList<>();
    }

    public relationworld_Category(
        String nom        ArrayList<relationworld_SourceNode> relationworld_sourcenodes,        ArrayList<relationworld_TargetNode> relationworld_targetnodes,        ArrayList<relationworld_Arrow> relationworld_arrows    ) {
        this.nom = nom;
        this.relationworld_sourcenodes = relationworld_sourcenodes;
        this.relationworld_targetnodes = relationworld_targetnodes;
        this.relationworld_arrows = relationworld_arrows;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<relationworld_SourceNode> getRelationworld_sourcenodes() {
        return relationworld_sourcenodes;
    }

    public void addRelationworld_sourcenode(Relationworld_sourcenode relationworld_sourcenode) {
        this.relationworld_sourcenodes.add(relationworld_sourcenode);
    }
    public List<relationworld_TargetNode> getRelationworld_targetnodes() {
        return relationworld_targetnodes;
    }

    public void addRelationworld_targetnode(Relationworld_targetnode relationworld_targetnode) {
        this.relationworld_targetnodes.add(relationworld_targetnode);
    }
    public List<relationworld_Arrow> getRelationworld_arrows() {
        return relationworld_arrows;
    }

    public void addRelationworld_arrow(Relationworld_arrow relationworld_arrow) {
        this.relationworld_arrows.add(relationworld_arrow);
    }

}