





import java.util.List;
import java.util.ArrayList;

public class Personne  {






    private List<Personne> personnes;




    private List<Union> unions;




    private Union union;


    public Personne(
    ) {
        this.personnes = new ArrayList<>();
        this.unions = new ArrayList<>();
    }

    public Personne(
        ArrayList<Personne> personnes,        ArrayList<Union> unions    ) {
        this.personnes = personnes;
        this.unions = unions;
    }


    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }
    public List<Union> getUnions() {
        return unions;
    }

    public void addUnion(Union union) {
        this.unions.add(union);
    }
    public Union getUnion() {
        return union;
    }

    public void setUnion(Union union) {
        this.union = union;
    }

}