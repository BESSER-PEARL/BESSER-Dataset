





import java.util.List;
import java.util.ArrayList;

public class Joueur  {

    private String nom;
    private String main;
    private int playerbank;





    private Blackjack blackjack;


    public Joueur(
        String nom,        String main,        int playerbank    ) {
        this.nom = nom;
        this.main = main;
        this.playerbank = playerbank;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getMain() {
        return main;
    }

    public void setMain(String main) {
        this.main = main;
    }
    public int getPlayerbank() {
        return playerbank;
    }

    public void setPlayerbank(int playerbank) {
        this.playerbank = playerbank;
    }

    public Blackjack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(Blackjack blackjack) {
        this.blackjack = blackjack;
    }

}