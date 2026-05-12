





import java.util.List;
import java.util.ArrayList;

public class Union  {

    private String dateUnion;





    private List<Personne> personnes;




    private List<Personne> personnes;


    public Union(
        String dateUnion    ) {
        this.dateUnion = dateUnion;
        this.personnes = new ArrayList<>();
        this.personnes = new ArrayList<>();
    }

    public Union(
        String dateUnion        ArrayList<Personne> personnes,        ArrayList<Personne> personnes    ) {
        this.dateUnion = dateUnion;
        this.personnes = personnes;
        this.personnes = personnes;
    }

    public String getDateunion() {
        return dateUnion;
    }

    public void setDateunion(String dateUnion) {
        this.dateUnion = dateUnion;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }
    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}