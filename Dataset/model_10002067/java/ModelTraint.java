





import java.util.List;
import java.util.ArrayList;

public class ModelTraint  {

    private None listeWagon__;
    private None cellule____;
    private int indiceWagonCourant;
    private int indiceJoueurCourant;
    private None joueurs__;



    public ModelTraint(
        None listeWagon__,        None cellule____,        int indiceWagonCourant,        int indiceJoueurCourant,        None joueurs__    ) {
        this.listeWagon__ = listeWagon__;
        this.cellule____ = cellule____;
        this.indiceWagonCourant = indiceWagonCourant;
        this.indiceJoueurCourant = indiceJoueurCourant;
        this.joueurs__ = joueurs__;
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
    public None getJoueurs__() {
        return joueurs__;
    }

    public void setJoueurs__(None joueurs__) {
        this.joueurs__ = joueurs__;
    }


}