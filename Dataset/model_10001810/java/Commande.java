





import java.util.List;
import java.util.ArrayList;

public class Commande  {

    private String paiement;
    private int _tat;
    private int date;
    private int utilisateur_id;
    private int id;





    private Utilisateur utilisateur;


    public Commande(
        String paiement,        int _tat,        int date,        int utilisateur_id,        int id    ) {
        this.paiement = paiement;
        this._tat = _tat;
        this.date = date;
        this.utilisateur_id = utilisateur_id;
        this.id = id;
    }


    public String getPaiement() {
        return paiement;
    }

    public void setPaiement(String paiement) {
        this.paiement = paiement;
    }
    public int get_tat() {
        return _tat;
    }

    public void set_tat(int _tat) {
        this._tat = _tat;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public int getUtilisateur_id() {
        return utilisateur_id;
    }

    public void setUtilisateur_id(int utilisateur_id) {
        this.utilisateur_id = utilisateur_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}