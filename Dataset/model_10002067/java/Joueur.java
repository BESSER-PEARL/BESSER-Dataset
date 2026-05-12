





import java.util.List;
import java.util.ArrayList;

public class Joueur  {

    private None wagon;
    private int a_b;
    private int x_y;
    private None model;
    private String nomJoueur;





    private ModelTraint modeltraint;


    public Joueur(
        None wagon,        int a_b,        int x_y,        None model,        String nomJoueur    ) {
        this.wagon = wagon;
        this.a_b = a_b;
        this.x_y = x_y;
        this.model = model;
        this.nomJoueur = nomJoueur;
    }


    public None getWagon() {
        return wagon;
    }

    public void setWagon(None wagon) {
        this.wagon = wagon;
    }
    public int getA_b() {
        return a_b;
    }

    public void setA_b(int a_b) {
        this.a_b = a_b;
    }
    public int getX_y() {
        return x_y;
    }

    public void setX_y(int x_y) {
        this.x_y = x_y;
    }
    public None getModel() {
        return model;
    }

    public void setModel(None model) {
        this.model = model;
    }
    public String getNomjoueur() {
        return nomJoueur;
    }

    public void setNomjoueur(String nomJoueur) {
        this.nomJoueur = nomJoueur;
    }

    public ModelTraint getModeltraint() {
        return modeltraint;
    }

    public void setModeltraint(ModelTraint modeltraint) {
        this.modeltraint = modeltraint;
    }

}