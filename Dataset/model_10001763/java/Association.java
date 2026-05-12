





import java.util.List;
import java.util.ArrayList;

public class Association  {

    private String nom___unicef;





    private List<Membre> membres;


    public Association(
        String nom___unicef    ) {
        this.nom___unicef = nom___unicef;
        this.membres = new ArrayList<>();
    }

    public Association(
        String nom___unicef        ArrayList<Membre> membres    ) {
        this.nom___unicef = nom___unicef;
        this.membres = membres;
    }

    public String getNom___unicef() {
        return nom___unicef;
    }

    public void setNom___unicef(String nom___unicef) {
        this.nom___unicef = nom___unicef;
    }

    public List<Membre> getMembres() {
        return membres;
    }

    public void addMembre(Membre membre) {
        this.membres.add(membre);
    }

}