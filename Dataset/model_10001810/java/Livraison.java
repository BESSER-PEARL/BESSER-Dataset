





import java.util.List;
import java.util.ArrayList;

public class Livraison  {

    private int commande_id;
    private int id;
    private int livreur_id;
    private String geocode;
    private int client_id;





    private Commande commande;




    private Utilisateur utilisateur;




    private Utilisateur utilisateur;


    public Livraison(
        int commande_id,        int id,        int livreur_id,        String geocode,        int client_id    ) {
        this.commande_id = commande_id;
        this.id = id;
        this.livreur_id = livreur_id;
        this.geocode = geocode;
        this.client_id = client_id;
    }


    public int getCommande_id() {
        return commande_id;
    }

    public void setCommande_id(int commande_id) {
        this.commande_id = commande_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLivreur_id() {
        return livreur_id;
    }

    public void setLivreur_id(int livreur_id) {
        this.livreur_id = livreur_id;
    }
    public String getGeocode() {
        return geocode;
    }

    public void setGeocode(String geocode) {
        this.geocode = geocode;
    }
    public int getClient_id() {
        return client_id;
    }

    public void setClient_id(int client_id) {
        this.client_id = client_id;
    }

    public Commande getCommande() {
        return commande;
    }

    public void setCommande(Commande commande) {
        this.commande = commande;
    }
    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }
    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}