





import java.util.List;
import java.util.ArrayList;

public class Vue_VueGrille  {

    private int TAILLE;
    private None modele;
    private String update;



    public Vue_VueGrille(
        int TAILLE,        None modele,        String update    ) {
        this.TAILLE = TAILLE;
        this.modele = modele;
        this.update = update;
    }


    public int getTaille() {
        return TAILLE;
    }

    public void setTaille(int TAILLE) {
        this.TAILLE = TAILLE;
    }
    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }


}