





import java.util.List;
import java.util.ArrayList;

public class Blackjack  {

    private None croupier;
    private String joueurs;



    public Blackjack(
        None croupier,        String joueurs    ) {
        this.croupier = croupier;
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


}