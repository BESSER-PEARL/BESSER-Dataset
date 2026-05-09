





import java.util.List;
import java.util.ArrayList;

public class relationworld_Category  {

    private String nom;





    private List<relationworld_Arrow> relationworld_arrows;




    private List<relationworld_TargetNode> relationworld_targetnodes;


    public relationworld_Category(
        String nom    ) {
        this.nom = nom;
        this.relationworld_arrows = new ArrayList<>();
        this.relationworld_targetnodes = new ArrayList<>();
    }

    public relationworld_Category(
        String nom        ArrayList<relationworld_Arrow> relationworld_arrows,        ArrayList<relationworld_TargetNode> relationworld_targetnodes    ) {
        this.nom = nom;
        this.relationworld_arrows = relationworld_arrows;
        this.relationworld_targetnodes = relationworld_targetnodes;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<relationworld_Arrow> getRelationworld_arrows() {
        return relationworld_arrows;
    }

    public void addRelationworld_arrow(Relationworld_arrow relationworld_arrow) {
        this.relationworld_arrows.add(relationworld_arrow);
    }
    public List<relationworld_TargetNode> getRelationworld_targetnodes() {
        return relationworld_targetnodes;
    }

    public void addRelationworld_targetnode(Relationworld_targetnode relationworld_targetnode) {
        this.relationworld_targetnodes.add(relationworld_targetnode);
    }

}