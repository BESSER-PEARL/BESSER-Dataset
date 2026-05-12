





import java.util.List;
import java.util.ArrayList;

public class Lieu  {






    private List<Personne> personnes;




    private List<Sport> sports;


    public Lieu(
    ) {
        this.personnes = new ArrayList<>();
        this.sports = new ArrayList<>();
    }

    public Lieu(
        ArrayList<Personne> personnes,        ArrayList<Sport> sports    ) {
        this.personnes = personnes;
        this.sports = sports;
    }


    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }
    public List<Sport> getSports() {
        return sports;
    }

    public void addSport(Sport sport) {
        this.sports.add(sport);
    }

}