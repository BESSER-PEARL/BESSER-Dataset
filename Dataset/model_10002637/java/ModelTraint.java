





import java.util.List;
import java.util.ArrayList;

public class ModelTraint  {

    private None cellule____;
    private None joueurs__;
    private None listeWagon__;
    private int indiceJoueurCourant;
    private int indiceWagonCourant;



    public ModelTraint(
        None cellule____,        None joueurs__,        None listeWagon__,        int indiceJoueurCourant,        int indiceWagonCourant    ) {
        this.cellule____ = cellule____;
        this.joueurs__ = joueurs__;
        this.listeWagon__ = listeWagon__;
        this.indiceJoueurCourant = indiceJoueurCourant;
        this.indiceWagonCourant = indiceWagonCourant;
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
    public None getListewagon__() {
        return listeWagon__;
    }

    public void setListewagon__(None listeWagon__) {
        this.listeWagon__ = listeWagon__;
    }
    public int getIndicejoueurcourant() {
        return indiceJoueurCourant;
    }

    public void setIndicejoueurcourant(int indiceJoueurCourant) {
        this.indiceJoueurCourant = indiceJoueurCourant;
    }
    public int getIndicewagoncourant() {
        return indiceWagonCourant;
    }

    public void setIndicewagoncourant(int indiceWagonCourant) {
        this.indiceWagonCourant = indiceWagonCourant;
    }


}