





import java.util.List;
import java.util.ArrayList;

public class Direction  {

    private boolean actif;
    private int id_direction;





    private List<Personne> personnes;


    public Direction(
        boolean actif,        int id_direction    ) {
        this.actif = actif;
        this.id_direction = id_direction;
        this.personnes = new ArrayList<>();
    }

    public Direction(
        boolean actif,        int id_direction        ArrayList<Personne> personnes    ) {
        this.actif = actif;
        this.id_direction = id_direction;
        this.personnes = personnes;
    }

    public boolean getActif() {
        return actif;
    }

    public void setActif(boolean actif) {
        this.actif = actif;
    }
    public int getId_direction() {
        return id_direction;
    }

    public void setId_direction(int id_direction) {
        this.id_direction = id_direction;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}