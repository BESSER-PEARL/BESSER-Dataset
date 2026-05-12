





import java.util.List;
import java.util.ArrayList;

public class Formateur  {

    private boolean actif;
    private int id_formateur;





    private List<Personne> personnes;


    public Formateur(
        boolean actif,        int id_formateur    ) {
        this.actif = actif;
        this.id_formateur = id_formateur;
        this.personnes = new ArrayList<>();
    }

    public Formateur(
        boolean actif,        int id_formateur        ArrayList<Personne> personnes    ) {
        this.actif = actif;
        this.id_formateur = id_formateur;
        this.personnes = personnes;
    }

    public boolean getActif() {
        return actif;
    }

    public void setActif(boolean actif) {
        this.actif = actif;
    }
    public int getId_formateur() {
        return id_formateur;
    }

    public void setId_formateur(int id_formateur) {
        this.id_formateur = id_formateur;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}