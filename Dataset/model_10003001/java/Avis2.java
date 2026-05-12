





import java.util.List;
import java.util.ArrayList;

public class Avis2  {

    private String description;
    private int note;





    private Utilisateur2 utilisateur2;


    public Avis2(
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

    public Utilisateur2 getUtilisateur2() {
        return utilisateur2;
    }

    public void setUtilisateur2(Utilisateur2 utilisateur2) {
        this.utilisateur2 = utilisateur2;
    }

}