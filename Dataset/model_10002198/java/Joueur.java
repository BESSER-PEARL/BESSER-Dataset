





import java.util.List;
import java.util.ArrayList;

public class Joueur  {

    private String nom;
    private String main;
    private int playerbank;





    private List<Main> mains;


    public Joueur(
        String nom,        String main,        int playerbank    ) {
        this.nom = nom;
        this.main = main;
        this.playerbank = playerbank;
        this.mains = new ArrayList<>();
    }

    public Joueur(
        String nom,        String main,        int playerbank        ArrayList<Main> mains    ) {
        this.nom = nom;
        this.main = main;
        this.playerbank = playerbank;
        this.mains = mains;
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

    public List<Main> getMains() {
        return mains;
    }

    public void addMain(Main main) {
        this.mains.add(main);
    }

}