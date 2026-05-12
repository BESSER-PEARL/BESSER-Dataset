





import java.util.List;
import java.util.ArrayList;

public class Joueur  {

    private None model;
    private int a_b;
    private int x_y;
    private None positionBandit;
    private String nomJoueur;
    private String attribute;





    private ModelTraint modeltraint;


    public Joueur(
        None model,        int a_b,        int x_y,        None positionBandit,        String nomJoueur,        String attribute    ) {
        this.model = model;
        this.a_b = a_b;
        this.x_y = x_y;
        this.positionBandit = positionBandit;
        this.nomJoueur = nomJoueur;
        this.attribute = attribute;
    }


    public None getModel() {
        return model;
    }

    public void setModel(None model) {
        this.model = model;
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
    public None getPositionbandit() {
        return positionBandit;
    }

    public void setPositionbandit(None positionBandit) {
        this.positionBandit = positionBandit;
    }
    public String getNomjoueur() {
        return nomJoueur;
    }

    public void setNomjoueur(String nomJoueur) {
        this.nomJoueur = nomJoueur;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public ModelTraint getModeltraint() {
        return modeltraint;
    }

    public void setModeltraint(ModelTraint modeltraint) {
        this.modeltraint = modeltraint;
    }

}