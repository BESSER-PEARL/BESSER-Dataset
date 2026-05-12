





import java.util.List;
import java.util.ArrayList;

public class ModelTraint  {

    private None joueurs__;
    private None listeWagon__;
    private int indiceWagonCourant;
    private int nombreJoueur;
    private None cellule____;
    private int indiceJoueurCourant;
    private int nombreWagon;



    public ModelTraint(
        None joueurs__,        None listeWagon__,        int indiceWagonCourant,        int nombreJoueur,        None cellule____,        int indiceJoueurCourant,        int nombreWagon    ) {
        this.joueurs__ = joueurs__;
        this.listeWagon__ = listeWagon__;
        this.indiceWagonCourant = indiceWagonCourant;
        this.nombreJoueur = nombreJoueur;
        this.cellule____ = cellule____;
        this.indiceJoueurCourant = indiceJoueurCourant;
        this.nombreWagon = nombreWagon;
    }


    public None getJoueurs__() {
        return joueurs__;
    }

    public void setJoueurs__(None joueurs__) {
        this.joueurs__ = joueurs__;
    }
    public None getListewagon__() {
        return listeWagon__;
    }

    public void setListewagon__(None listeWagon__) {
        this.listeWagon__ = listeWagon__;
    }
    public int getIndicewagoncourant() {
        return indiceWagonCourant;
    }

    public void setIndicewagoncourant(int indiceWagonCourant) {
        this.indiceWagonCourant = indiceWagonCourant;
    }
    public int getNombrejoueur() {
        return nombreJoueur;
    }

    public void setNombrejoueur(int nombreJoueur) {
        this.nombreJoueur = nombreJoueur;
    }
    public None getCellule____() {
        return cellule____;
    }

    public void setCellule____(None cellule____) {
        this.cellule____ = cellule____;
    }
    public int getIndicejoueurcourant() {
        return indiceJoueurCourant;
    }

    public void setIndicejoueurcourant(int indiceJoueurCourant) {
        this.indiceJoueurCourant = indiceJoueurCourant;
    }
    public int getNombrewagon() {
        return nombreWagon;
    }

    public void setNombrewagon(int nombreWagon) {
        this.nombreWagon = nombreWagon;
    }


}