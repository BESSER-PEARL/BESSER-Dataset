





import java.util.List;
import java.util.ArrayList;

public class Modele_Cellule  {

    private boolean prochaineEtat;
    private boolean etat;
    private int y;
    private None modele;
    private int x;





    private Modele_CModele modele_cmodele;


    public Modele_Cellule(
        boolean prochaineEtat,        boolean etat,        int y,        None modele,        int x    ) {
        this.prochaineEtat = prochaineEtat;
        this.etat = etat;
        this.y = y;
        this.modele = modele;
        this.x = x;
    }


    public boolean getProchaineetat() {
        return prochaineEtat;
    }

    public void setProchaineetat(boolean prochaineEtat) {
        this.prochaineEtat = prochaineEtat;
    }
    public boolean getEtat() {
        return etat;
    }

    public void setEtat(boolean etat) {
        this.etat = etat;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public Modele_CModele getModele_cmodele() {
        return modele_cmodele;
    }

    public void setModele_cmodele(Modele_CModele modele_cmodele) {
        this.modele_cmodele = modele_cmodele;
    }

}