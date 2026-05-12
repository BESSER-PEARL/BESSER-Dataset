





import java.util.List;
import java.util.ArrayList;

public class Modele_Cellule  {

    private None modele;
    private int x;
    private int y;
    private boolean etat;
    private boolean prochaineEtat;





    private Modele_CModele modele_cmodele;


    public Modele_Cellule(
        None modele,        int x,        int y,        boolean etat,        boolean prochaineEtat    ) {
        this.modele = modele;
        this.x = x;
        this.y = y;
        this.etat = etat;
        this.prochaineEtat = prochaineEtat;
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
    public boolean getProchaineetat() {
        return prochaineEtat;
    }

    public void setProchaineetat(boolean prochaineEtat) {
        this.prochaineEtat = prochaineEtat;
    }

    public Modele_CModele getModele_cmodele() {
        return modele_cmodele;
    }

    public void setModele_cmodele(Modele_CModele modele_cmodele) {
        this.modele_cmodele = modele_cmodele;
    }

}