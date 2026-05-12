





import java.util.List;
import java.util.ArrayList;

public class EtatConge  {

    private int idEtat;
    private String nom;





    private List<Conge> conges;


    public EtatConge(
        int idEtat,        String nom    ) {
        this.idEtat = idEtat;
        this.nom = nom;
        this.conges = new ArrayList<>();
    }

    public EtatConge(
        int idEtat,        String nom        ArrayList<Conge> conges    ) {
        this.idEtat = idEtat;
        this.nom = nom;
        this.conges = conges;
    }

    public int getIdetat() {
        return idEtat;
    }

    public void setIdetat(int idEtat) {
        this.idEtat = idEtat;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<Conge> getConges() {
        return conges;
    }

    public void addConge(Conge conge) {
        this.conges.add(conge);
    }

}