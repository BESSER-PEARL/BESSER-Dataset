





import java.util.List;
import java.util.ArrayList;

public class Main  {

    private String bet;
    private String cartes;
    private int value;





    private Croupier croupier;




    private Joueur joueur;


    public Main(
        String bet,        String cartes,        int value    ) {
        this.bet = bet;
        this.cartes = cartes;
        this.value = value;
    }


    public String getBet() {
        return bet;
    }

    public void setBet(String bet) {
        this.bet = bet;
    }
    public String getCartes() {
        return cartes;
    }

    public void setCartes(String cartes) {
        this.cartes = cartes;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Croupier getCroupier() {
        return croupier;
    }

    public void setCroupier(Croupier croupier) {
        this.croupier = croupier;
    }
    public Joueur getJoueur() {
        return joueur;
    }

    public void setJoueur(Joueur joueur) {
        this.joueur = joueur;
    }

}