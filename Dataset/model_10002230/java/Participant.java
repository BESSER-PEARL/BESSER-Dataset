





import java.util.List;
import java.util.ArrayList;

public class Participant  {

    private String date_naissance;
    private int id_session;
    private String nom;
    private String prenom;





    private List<Prestation> prestations;


    public Participant(
        String date_naissance,        int id_session,        String nom,        String prenom    ) {
        this.date_naissance = date_naissance;
        this.id_session = id_session;
        this.nom = nom;
        this.prenom = prenom;
        this.prestations = new ArrayList<>();
    }

    public Participant(
        String date_naissance,        int id_session,        String nom,        String prenom        ArrayList<Prestation> prestations    ) {
        this.date_naissance = date_naissance;
        this.id_session = id_session;
        this.nom = nom;
        this.prenom = prenom;
        this.prestations = prestations;
    }

    public String getDate_naissance() {
        return date_naissance;
    }

    public void setDate_naissance(String date_naissance) {
        this.date_naissance = date_naissance;
    }
    public int getId_session() {
        return id_session;
    }

    public void setId_session(int id_session) {
        this.id_session = id_session;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public List<Prestation> getPrestations() {
        return prestations;
    }

    public void addPrestation(Prestation prestation) {
        this.prestations.add(prestation);
    }

}