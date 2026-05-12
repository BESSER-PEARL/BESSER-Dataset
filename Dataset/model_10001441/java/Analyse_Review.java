





import java.util.List;
import java.util.ArrayList;

public class Analyse_Review  {

    private int NoteGlobale;
    private String lesNotes;
    private String Commentaire;





    private Analyse_Fast_Food analyse_fast_food;


    public Analyse_Review(
        int NoteGlobale,        String lesNotes,        String Commentaire    ) {
        this.NoteGlobale = NoteGlobale;
        this.lesNotes = lesNotes;
        this.Commentaire = Commentaire;
    }


    public int getNoteglobale() {
        return NoteGlobale;
    }

    public void setNoteglobale(int NoteGlobale) {
        this.NoteGlobale = NoteGlobale;
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

    public Analyse_Fast_Food getAnalyse_fast_food() {
        return analyse_fast_food;
    }

    public void setAnalyse_fast_food(Analyse_Fast_Food analyse_fast_food) {
        this.analyse_fast_food = analyse_fast_food;
    }

}