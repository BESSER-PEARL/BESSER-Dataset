





import java.util.List;
import java.util.ArrayList;

public class Avis1  {

    private String description;
    private int note;





    private Utilisateur utilisateur;


    public Avis1(
        String description,        int note    ) {
        this.description = description;
        this.note = note;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNote() {
        return note;
    }

    public void setNote(int note) {
        this.note = note;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}