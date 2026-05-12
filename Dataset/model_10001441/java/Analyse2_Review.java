





import java.util.List;
import java.util.ArrayList;

public class Analyse2_Review  {

    private String lesNotes;
    private String Commentaire;
    private String utilite;





    private Analyse2_Fast_Food analyse2_fast_food;


    public Analyse2_Review(
        String lesNotes,        String Commentaire,        String utilite    ) {
        this.lesNotes = lesNotes;
        this.Commentaire = Commentaire;
        this.utilite = utilite;
    }


    public String getLesnotes() {
        return lesNotes;
    }

    public void setLesnotes(String lesNotes) {
        this.lesNotes = lesNotes;
    }
    public String getCommentaire() {
        return Commentaire;
    }

    public void setCommentaire(String Commentaire) {
        this.Commentaire = Commentaire;
    }
    public String getUtilite() {
        return utilite;
    }

    public void setUtilite(String utilite) {
        this.utilite = utilite;
    }

    public Analyse2_Fast_Food getAnalyse2_fast_food() {
        return analyse2_fast_food;
    }

    public void setAnalyse2_fast_food(Analyse2_Fast_Food analyse2_fast_food) {
        this.analyse2_fast_food = analyse2_fast_food;
    }

}