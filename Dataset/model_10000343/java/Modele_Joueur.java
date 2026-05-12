





import java.util.List;
import java.util.ArrayList;

public class Modele_Joueur  {

    private int x;
    private int cles;
    private boolean vivant;
    private String artefacts;
    private int y;



    public Modele_Joueur(
        int x,        int cles,        boolean vivant,        String artefacts,        int y    ) {
        this.x = x;
        this.cles = cles;
        this.vivant = vivant;
        this.artefacts = artefacts;
        this.y = y;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getCles() {
        return cles;
    }

    public void setCles(int cles) {
        this.cles = cles;
    }
    public boolean getVivant() {
        return vivant;
    }

    public void setVivant(boolean vivant) {
        this.vivant = vivant;
    }
    public String getArtefacts() {
        return artefacts;
    }

    public void setArtefacts(String artefacts) {
        this.artefacts = artefacts;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


}