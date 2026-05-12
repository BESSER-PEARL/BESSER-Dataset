





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Ville  {

    private int id;
    private int cp;
    private String nom;





    private List<Covoiturage_Passager> covoiturage_passagers;




    private List<Covoiturage_Trajet> covoiturage_trajets;


    public Covoiturage_Ville(
        int id,        int cp,        String nom    ) {
        this.id = id;
        this.cp = cp;
        this.nom = nom;
        this.covoiturage_passagers = new ArrayList<>();
        this.covoiturage_trajets = new ArrayList<>();
    }

    public Covoiturage_Ville(
        int id,        int cp,        String nom        ArrayList<Covoiturage_Passager> covoiturage_passagers,        ArrayList<Covoiturage_Trajet> covoiturage_trajets    ) {
        this.id = id;
        this.cp = cp;
        this.nom = nom;
        this.covoiturage_passagers = covoiturage_passagers;
        this.covoiturage_trajets = covoiturage_trajets;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getCp() {
        return cp;
    }

    public void setCp(int cp) {
        this.cp = cp;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<Covoiturage_Passager> getCovoiturage_passagers() {
        return covoiturage_passagers;
    }

    public void addCovoiturage_passager(Covoiturage_passager covoiturage_passager) {
        this.covoiturage_passagers.add(covoiturage_passager);
    }
    public List<Covoiturage_Trajet> getCovoiturage_trajets() {
        return covoiturage_trajets;
    }

    public void addCovoiturage_trajet(Covoiturage_trajet covoiturage_trajet) {
        this.covoiturage_trajets.add(covoiturage_trajet);
    }

}