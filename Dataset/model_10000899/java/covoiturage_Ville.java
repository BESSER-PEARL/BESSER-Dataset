





import java.util.List;
import java.util.ArrayList;

public class covoiturage_Ville  {

    private int id;
    private String nom;
    private String cp;





    private List<covoiturage_Personne> covoiturage_personnes;




    private covoiturage_Reservations covoiturage_reservations;


    public covoiturage_Ville(
        int id,        String nom,        String cp    ) {
        this.id = id;
        this.nom = nom;
        this.cp = cp;
        this.covoiturage_personnes = new ArrayList<>();
    }

    public covoiturage_Ville(
        int id,        String nom,        String cp        ArrayList<covoiturage_Personne> covoiturage_personnes    ) {
        this.id = id;
        this.nom = nom;
        this.cp = cp;
        this.covoiturage_personnes = covoiturage_personnes;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getCp() {
        return cp;
    }

    public void setCp(String cp) {
        this.cp = cp;
    }

    public List<covoiturage_Personne> getCovoiturage_personnes() {
        return covoiturage_personnes;
    }

    public void addCovoiturage_personne(Covoiturage_personne covoiturage_personne) {
        this.covoiturage_personnes.add(covoiturage_personne);
    }
    public covoiturage_Reservations getCovoiturage_reservations() {
        return covoiturage_reservations;
    }

    public void setCovoiturage_reservations(covoiturage_Reservations covoiturage_reservations) {
        this.covoiturage_reservations = covoiturage_reservations;
    }

}