





import java.util.List;
import java.util.ArrayList;

public class personne  {






    private List<personne> personnes;


    public personne(
    ) {
        this.personnes = new ArrayList<>();
    }

    public personne(
        ArrayList<personne> personnes    ) {
        this.personnes = personnes;
    }


    public List<personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}