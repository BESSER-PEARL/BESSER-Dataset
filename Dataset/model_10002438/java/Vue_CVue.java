





import java.util.List;
import java.util.ArrayList;

public class Vue_CVue  {

    private String frame;
    private None commande;
    private None grille;





    private Vue_VueGrille vue_vuegrille;




    private Vue_VueCommande vue_vuecommande;


    public Vue_CVue(
        String frame,        None commande,        None grille    ) {
        this.frame = frame;
        this.commande = commande;
        this.grille = grille;
    }


    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }
    public None getCommande() {
        return commande;
    }

    public void setCommande(None commande) {
        this.commande = commande;
    }
    public None getGrille() {
        return grille;
    }

    public void setGrille(None grille) {
        this.grille = grille;
    }

    public Vue_VueGrille getVue_vuegrille() {
        return vue_vuegrille;
    }

    public void setVue_vuegrille(Vue_VueGrille vue_vuegrille) {
        this.vue_vuegrille = vue_vuegrille;
    }
    public Vue_VueCommande getVue_vuecommande() {
        return vue_vuecommande;
    }

    public void setVue_vuecommande(Vue_VueCommande vue_vuecommande) {
        this.vue_vuecommande = vue_vuecommande;
    }

}