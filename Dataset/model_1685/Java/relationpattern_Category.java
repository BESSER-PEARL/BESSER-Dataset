





import java.util.List;
import java.util.ArrayList;

public class relationpattern_Category  {

    private String nom;





    private List<relationpattern_TargetNode> relationpattern_targetnodes;




    private List<relationpattern_SourceNode> relationpattern_sourcenodes;




    private List<relationpattern_Arrow> relationpattern_arrows;


    public relationpattern_Category(
        String nom    ) {
        this.nom = nom;
        this.relationpattern_targetnodes = new ArrayList<>();
        this.relationpattern_sourcenodes = new ArrayList<>();
        this.relationpattern_arrows = new ArrayList<>();
    }

    public relationpattern_Category(
        String nom        ArrayList<relationpattern_TargetNode> relationpattern_targetnodes,        ArrayList<relationpattern_SourceNode> relationpattern_sourcenodes,        ArrayList<relationpattern_Arrow> relationpattern_arrows    ) {
        this.nom = nom;
        this.relationpattern_targetnodes = relationpattern_targetnodes;
        this.relationpattern_sourcenodes = relationpattern_sourcenodes;
        this.relationpattern_arrows = relationpattern_arrows;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<relationpattern_TargetNode> getRelationpattern_targetnodes() {
        return relationpattern_targetnodes;
    }

    public void addRelationpattern_targetnode(Relationpattern_targetnode relationpattern_targetnode) {
        this.relationpattern_targetnodes.add(relationpattern_targetnode);
    }
    public List<relationpattern_SourceNode> getRelationpattern_sourcenodes() {
        return relationpattern_sourcenodes;
    }

    public void addRelationpattern_sourcenode(Relationpattern_sourcenode relationpattern_sourcenode) {
        this.relationpattern_sourcenodes.add(relationpattern_sourcenode);
    }
    public List<relationpattern_Arrow> getRelationpattern_arrows() {
        return relationpattern_arrows;
    }

    public void addRelationpattern_arrow(Relationpattern_arrow relationpattern_arrow) {
        this.relationpattern_arrows.add(relationpattern_arrow);
    }

}