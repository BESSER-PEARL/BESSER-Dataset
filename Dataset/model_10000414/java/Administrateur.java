





import java.util.List;
import java.util.ArrayList;

public class Administrateur  {

    private boolean actif;
    private int id_administrateur;





    private List<Personne> personnes;


    public Administrateur(
        boolean actif,        int id_administrateur    ) {
        this.actif = actif;
        this.id_administrateur = id_administrateur;
        this.personnes = new ArrayList<>();
    }

    public Administrateur(
        boolean actif,        int id_administrateur        ArrayList<Personne> personnes    ) {
        this.actif = actif;
        this.id_administrateur = id_administrateur;
        this.personnes = personnes;
    }

    public boolean getActif() {
        return actif;
    }

    public void setActif(boolean actif) {
        this.actif = actif;
    }
    public int getId_administrateur() {
        return id_administrateur;
    }

    public void setId_administrateur(int id_administrateur) {
        this.id_administrateur = id_administrateur;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}