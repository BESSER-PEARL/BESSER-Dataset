





import java.util.List;
import java.util.ArrayList;

public class Sport  {

    private int id;
    private String nom;





    private List<Personne> personnes;


    public Sport(
        int id,        String nom    ) {
        this.id = id;
        this.nom = nom;
        this.personnes = new ArrayList<>();
    }

    public Sport(
        int id,        String nom        ArrayList<Personne> personnes    ) {
        this.id = id;
        this.nom = nom;
        this.personnes = personnes;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}