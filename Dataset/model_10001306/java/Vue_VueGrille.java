





import java.util.List;
import java.util.ArrayList;

public class Vue_VueGrille  {

    private None modele;
    private int TAILLE;
    private String update;



    public Vue_VueGrille(
        None modele,        int TAILLE,        String update    ) {
        this.modele = modele;
        this.TAILLE = TAILLE;
        this.update = update;
    }


    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public int getTaille() {
        return TAILLE;
    }

    public void setTaille(int TAILLE) {
        this.TAILLE = TAILLE;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }


}