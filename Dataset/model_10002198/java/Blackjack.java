





import java.util.List;
import java.util.ArrayList;

public class Blackjack  {

    private None croupier;
    private String joueurs;





    private Croupier croupier;




    private List<Joueur> joueurs;


    public Blackjack(
        None croupier,        String joueurs    ) {
        this.croupier = croupier;
        this.joueurs = joueurs;
        this.joueurs = new ArrayList<>();
    }

    public Blackjack(
        None croupier,        String joueurs        ArrayList<Joueur> joueurs    ) {
        this.croupier = croupier;
        this.joueurs = joueurs;
        this.joueurs = joueurs;
    }

    public None getCroupier() {
        return croupier;
    }

    public void setCroupier(None croupier) {
        this.croupier = croupier;
    }
    public String getJoueurs() {
        return joueurs;
    }

    public void setJoueurs(String joueurs) {
        this.joueurs = joueurs;
    }

    public Croupier getCroupier() {
        return croupier;
    }

    public void setCroupier(Croupier croupier) {
        this.croupier = croupier;
    }
    public List<Joueur> getJoueurs() {
        return joueurs;
    }

    public void addJoueur(Joueur joueur) {
        this.joueurs.add(joueur);
    }

}