





import java.util.List;
import java.util.ArrayList;

public class Etat  {

    private String nom;
    private boolean verrouillage;
    private int id;





    private Commande commande;


    public Etat(
        String nom,        boolean verrouillage,        int id    ) {
        this.nom = nom;
        this.verrouillage = verrouillage;
        this.id = id;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public boolean getVerrouillage() {
        return verrouillage;
    }

    public void setVerrouillage(boolean verrouillage) {
        this.verrouillage = verrouillage;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Commande getCommande() {
        return commande;
    }

    public void setCommande(Commande commande) {
        this.commande = commande;
    }

}