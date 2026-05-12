





import java.util.List;
import java.util.ArrayList;

public class Vue_CVue  {

    private None grille;
    private None commande;
    private String frame;





    private Vue_VueCommande vue_vuecommande;




    private Vue_VueGrille vue_vuegrille;


    public Vue_CVue(
        None grille,        None commande,        String frame    ) {
        this.grille = grille;
        this.commande = commande;
        this.frame = frame;
    }


    public None getGrille() {
        return grille;
    }

    public void setGrille(None grille) {
        this.grille = grille;
    }
    public None getCommande() {
        return commande;
    }

    public void setCommande(None commande) {
        this.commande = commande;
    }
    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }

    public Vue_VueCommande getVue_vuecommande() {
        return vue_vuecommande;
    }

    public void setVue_vuecommande(Vue_VueCommande vue_vuecommande) {
        this.vue_vuecommande = vue_vuecommande;
    }
    public Vue_VueGrille getVue_vuegrille() {
        return vue_vuegrille;
    }

    public void setVue_vuegrille(Vue_VueGrille vue_vuegrille) {
        this.vue_vuegrille = vue_vuegrille;
    }

}