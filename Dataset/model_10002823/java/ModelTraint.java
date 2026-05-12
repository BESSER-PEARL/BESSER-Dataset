





import java.util.List;
import java.util.ArrayList;

public class ModelTraint  {

    private int nombreWagon;
    private int nombreJoueur;
    private int indiceWagonCourant;
    private int indiceJoueurCourant;
    private None listeWagon__;
    private None cellule____;
    private None joueurs__;



    public ModelTraint(
        int nombreWagon,        int nombreJoueur,        int indiceWagonCourant,        int indiceJoueurCourant,        None listeWagon__,        None cellule____,        None joueurs__    ) {
        this.nombreWagon = nombreWagon;
        this.nombreJoueur = nombreJoueur;
        this.indiceWagonCourant = indiceWagonCourant;
        this.indiceJoueurCourant = indiceJoueurCourant;
        this.listeWagon__ = listeWagon__;
        this.cellule____ = cellule____;
        this.joueurs__ = joueurs__;
    }


    public int getNombrewagon() {
        return nombreWagon;
    }

    public void setNombrewagon(int nombreWagon) {
        this.nombreWagon = nombreWagon;
    }
    public int getNombrejoueur() {
        return nombreJoueur;
    }

    public void setNombrejoueur(int nombreJoueur) {
        this.nombreJoueur = nombreJoueur;
    }
    public int getIndicewagoncourant() {
        return indiceWagonCourant;
    }

    public void setIndicewagoncourant(int indiceWagonCourant) {
        this.indiceWagonCourant = indiceWagonCourant;
    }
    public int getIndicejoueurcourant() {
        return indiceJoueurCourant;
    }

    public void setIndicejoueurcourant(int indiceJoueurCourant) {
        this.indiceJoueurCourant = indiceJoueurCourant;
    }
    public None getListewagon__() {
        return listeWagon__;
    }

    public void setListewagon__(None listeWagon__) {
        this.listeWagon__ = listeWagon__;
    }
    public None getCellule____() {
        return cellule____;
    }

    public void setCellule____(None cellule____) {
        this.cellule____ = cellule____;
    }
    public None getJoueurs__() {
        return joueurs__;
    }

    public void setJoueurs__(None joueurs__) {
        this.joueurs__ = joueurs__;
    }


}