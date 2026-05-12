





import java.util.List;
import java.util.ArrayList;

public class Personne  {






    private List<Union> unions;




    private List<Personne> personnes;


    public Personne(
    ) {
        this.unions = new ArrayList<>();
        this.personnes = new ArrayList<>();
    }

    public Personne(
        ArrayList<Union> unions,        ArrayList<Personne> personnes    ) {
        this.unions = unions;
        this.personnes = personnes;
    }


    public List<Union> getUnions() {
        return unions;
    }

    public void addUnion(Union union) {
        this.unions.add(union);
    }
    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}