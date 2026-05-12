





import java.util.List;
import java.util.ArrayList;

public class AvisGlobal  {

    private String diagramme;
    private String Commentaires;
    private int nbAvis;
    private String note;





    private FicheRestaurant ficherestaurant;


    public AvisGlobal(
        String diagramme,        String Commentaires,        int nbAvis,        String note    ) {
        this.diagramme = diagramme;
        this.Commentaires = Commentaires;
        this.nbAvis = nbAvis;
        this.note = note;
    }


    public String getDiagramme() {
        return diagramme;
    }

    public void setDiagramme(String diagramme) {
        this.diagramme = diagramme;
    }
    public String getCommentaires() {
        return Commentaires;
    }

    public void setCommentaires(String Commentaires) {
        this.Commentaires = Commentaires;
    }
    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public FicheRestaurant getFicherestaurant() {
        return ficherestaurant;
    }

    public void setFicherestaurant(FicheRestaurant ficherestaurant) {
        this.ficherestaurant = ficherestaurant;
    }

}