





import java.util.List;
import java.util.ArrayList;

public class Modele_Joueur  {

    private boolean vivant;
    private int x;
    private int y;
    private String artefacts;
    private int cles;



    public Modele_Joueur(
        boolean vivant,        int x,        int y,        String artefacts,        int cles    ) {
        this.vivant = vivant;
        this.x = x;
        this.y = y;
        this.artefacts = artefacts;
        this.cles = cles;
    }


    public boolean getVivant() {
        return vivant;
    }

    public void setVivant(boolean vivant) {
        this.vivant = vivant;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getArtefacts() {
        return artefacts;
    }

    public void setArtefacts(String artefacts) {
        this.artefacts = artefacts;
    }
    public int getCles() {
        return cles;
    }

    public void setCles(int cles) {
        this.cles = cles;
    }


}