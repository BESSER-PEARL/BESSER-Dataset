





import java.util.List;
import java.util.ArrayList;

public class Groupe  {

    private int id;
    private int numeroGroupe;
    private String libelle;





    private List<Candidat> candidats;


    public Groupe(
        int id,        int numeroGroupe,        String libelle    ) {
        this.id = id;
        this.numeroGroupe = numeroGroupe;
        this.libelle = libelle;
        this.candidats = new ArrayList<>();
    }

    public Groupe(
        int id,        int numeroGroupe,        String libelle        ArrayList<Candidat> candidats    ) {
        this.id = id;
        this.numeroGroupe = numeroGroupe;
        this.libelle = libelle;
        this.candidats = candidats;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getNumerogroupe() {
        return numeroGroupe;
    }

    public void setNumerogroupe(int numeroGroupe) {
        this.numeroGroupe = numeroGroupe;
    }
    public String getLibelle() {
        return libelle;
    }

    public void setLibelle(String libelle) {
        this.libelle = libelle;
    }

    public List<Candidat> getCandidats() {
        return candidats;
    }

    public void addCandidat(Candidat candidat) {
        this.candidats.add(candidat);
    }

}