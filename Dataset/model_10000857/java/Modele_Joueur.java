





import java.util.List;
import java.util.ArrayList;

public class Modele_Joueur  {

    private int y;
    private int cles;
    private int x;
    private String artefacts;
    private boolean vivant;



    public Modele_Joueur(
        int y,        int cles,        int x,        String artefacts,        boolean vivant    ) {
        this.y = y;
        this.cles = cles;
        this.x = x;
        this.artefacts = artefacts;
        this.vivant = vivant;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getCles() {
        return cles;
    }

    public void setCles(int cles) {
        this.cles = cles;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public String getArtefacts() {
        return artefacts;
    }

    public void setArtefacts(String artefacts) {
        this.artefacts = artefacts;
    }
    public boolean getVivant() {
        return vivant;
    }

    public void setVivant(boolean vivant) {
        this.vivant = vivant;
    }


}