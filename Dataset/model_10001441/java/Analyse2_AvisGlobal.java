





import java.util.List;
import java.util.ArrayList;

public class Analyse2_AvisGlobal  {

    private String Commentaires;
    private String notes;
    private int nbAvis;





    private Analyse2_Fast_Food analyse2_fast_food;


    public Analyse2_AvisGlobal(
        String Commentaires,        String notes,        int nbAvis    ) {
        this.Commentaires = Commentaires;
        this.notes = notes;
        this.nbAvis = nbAvis;
    }


    public String getCommentaires() {
        return Commentaires;
    }

    public void setCommentaires(String Commentaires) {
        this.Commentaires = Commentaires;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }

    public Analyse2_Fast_Food getAnalyse2_fast_food() {
        return analyse2_fast_food;
    }

    public void setAnalyse2_fast_food(Analyse2_Fast_Food analyse2_fast_food) {
        this.analyse2_fast_food = analyse2_fast_food;
    }

}