





import java.util.List;
import java.util.ArrayList;

public class Modele_CModele  {

    private int largeur;
    private None attribute;
    private int hauteur;





    private List<Vue_VueGrille> vue_vuegrilles;




    private List<Vue_VueCommande> vue_vuecommandes;


    public Modele_CModele(
        int largeur,        None attribute,        int hauteur    ) {
        this.largeur = largeur;
        this.attribute = attribute;
        this.hauteur = hauteur;
        this.vue_vuegrilles = new ArrayList<>();
        this.vue_vuecommandes = new ArrayList<>();
    }

    public Modele_CModele(
        int largeur,        None attribute,        int hauteur        ArrayList<Vue_VueGrille> vue_vuegrilles,        ArrayList<Vue_VueCommande> vue_vuecommandes    ) {
        this.largeur = largeur;
        this.attribute = attribute;
        this.hauteur = hauteur;
        this.vue_vuegrilles = vue_vuegrilles;
        this.vue_vuecommandes = vue_vuecommandes;
    }

    public int getLargeur() {
        return largeur;
    }

    public void setLargeur(int largeur) {
        this.largeur = largeur;
    }
    public None getAttribute() {
        return attribute;
    }

    public void setAttribute(None attribute) {
        this.attribute = attribute;
    }
    public int getHauteur() {
        return hauteur;
    }

    public void setHauteur(int hauteur) {
        this.hauteur = hauteur;
    }

    public List<Vue_VueGrille> getVue_vuegrilles() {
        return vue_vuegrilles;
    }

    public void addVue_vuegrille(Vue_vuegrille vue_vuegrille) {
        this.vue_vuegrilles.add(vue_vuegrille);
    }
    public List<Vue_VueCommande> getVue_vuecommandes() {
        return vue_vuecommandes;
    }

    public void addVue_vuecommande(Vue_vuecommande vue_vuecommande) {
        this.vue_vuecommandes.add(vue_vuecommande);
    }

}