





import java.util.List;
import java.util.ArrayList;

public class Modele_Cellule  {

    private int x;
    private None modele;
    private boolean prochaineEtat;
    private int y;
    private boolean etat;





    private Modele_CModele modele_cmodele;


    public Modele_Cellule(
        int x,        None modele,        boolean prochaineEtat,        int y,        boolean etat    ) {
        this.x = x;
        this.modele = modele;
        this.prochaineEtat = prochaineEtat;
        this.y = y;
        this.etat = etat;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public boolean getProchaineetat() {
        return prochaineEtat;
    }

    public void setProchaineetat(boolean prochaineEtat) {
        this.prochaineEtat = prochaineEtat;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public boolean getEtat() {
        return etat;
    }

    public void setEtat(boolean etat) {
        this.etat = etat;
    }

    public Modele_CModele getModele_cmodele() {
        return modele_cmodele;
    }

    public void setModele_cmodele(Modele_CModele modele_cmodele) {
        this.modele_cmodele = modele_cmodele;
    }

}