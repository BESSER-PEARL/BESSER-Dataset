





import java.util.List;
import java.util.ArrayList;

public class myDsl_Commandes  {






    private List<myDsl_Commande> mydsl_commandes;




    private myDsl_Commande mydsl_commande;




    private myDsl_Fonction mydsl_fonction;


    public myDsl_Commandes(
    ) {
        this.mydsl_commandes = new ArrayList<>();
    }

    public myDsl_Commandes(
        ArrayList<myDsl_Commande> mydsl_commandes    ) {
        this.mydsl_commandes = mydsl_commandes;
    }


    public List<myDsl_Commande> getMydsl_commandes() {
        return mydsl_commandes;
    }

    public void addMydsl_commande(Mydsl_commande mydsl_commande) {
        this.mydsl_commandes.add(mydsl_commande);
    }
    public myDsl_Commande getMydsl_commande() {
        return mydsl_commande;
    }

    public void setMydsl_commande(myDsl_Commande mydsl_commande) {
        this.mydsl_commande = mydsl_commande;
    }
    public myDsl_Fonction getMydsl_fonction() {
        return mydsl_fonction;
    }

    public void setMydsl_fonction(myDsl_Fonction mydsl_fonction) {
        this.mydsl_fonction = mydsl_fonction;
    }

}