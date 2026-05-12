





import java.util.List;
import java.util.ArrayList;

public class Piece  {

    private String type;
    private int id;
    private String name;





    private List<Commande> commandes;


    public Piece(
        String type,        int id,        String name    ) {
        this.type = type;
        this.id = id;
        this.name = name;
        this.commandes = new ArrayList<>();
    }

    public Piece(
        String type,        int id,        String name        ArrayList<Commande> commandes    ) {
        this.type = type;
        this.id = id;
        this.name = name;
        this.commandes = commandes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Commande> getCommandes() {
        return commandes;
    }

    public void addCommande(Commande commande) {
        this.commandes.add(commande);
    }

}