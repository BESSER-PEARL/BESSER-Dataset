





import java.util.List;
import java.util.ArrayList;

public class Personne  {






    private List<Personne> personnes;


    public Personne(
    ) {
        this.personnes = new ArrayList<>();
    }

    public Personne(
        ArrayList<Personne> personnes    ) {
        this.personnes = personnes;
    }


    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}