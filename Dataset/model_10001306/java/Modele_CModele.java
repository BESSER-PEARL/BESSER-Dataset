





import java.util.List;
import java.util.ArrayList;

public class Modele_CModele  {

    private None attribute;
    private int hauteur;
    private int largeur;





    private List<Vue_VueGrille> vue_vuegrilles;




    private List<Vue_VueCommande> vue_vuecommandes;


    public Modele_CModele(
        None attribute,        int hauteur,        int largeur    ) {
        this.attribute = attribute;
        this.hauteur = hauteur;
        this.largeur = largeur;
        this.vue_vuegrilles = new ArrayList<>();
        this.vue_vuecommandes = new ArrayList<>();
    }

    public Modele_CModele(
        None attribute,        int hauteur,        int largeur        ArrayList<Vue_VueGrille> vue_vuegrilles,        ArrayList<Vue_VueCommande> vue_vuecommandes    ) {
        this.attribute = attribute;
        this.hauteur = hauteur;
        this.largeur = largeur;
        this.vue_vuegrilles = vue_vuegrilles;
        this.vue_vuecommandes = vue_vuecommandes;
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
    public int getLargeur() {
        return largeur;
    }

    public void setLargeur(int largeur) {
        this.largeur = largeur;
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