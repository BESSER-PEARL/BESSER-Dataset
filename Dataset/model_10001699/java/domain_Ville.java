





import java.util.List;
import java.util.ArrayList;

public class domain_Ville  {

    private String nom;
    private int cp;
    private int id;





    private List<domain_Profil> domain_profils;




    private domain_Trajet domain_trajet;


    public domain_Ville(
        String nom,        int cp,        int id    ) {
        this.nom = nom;
        this.cp = cp;
        this.id = id;
        this.domain_profils = new ArrayList<>();
    }

    public domain_Ville(
        String nom,        int cp,        int id        ArrayList<domain_Profil> domain_profils    ) {
        this.nom = nom;
        this.cp = cp;
        this.id = id;
        this.domain_profils = domain_profils;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getCp() {
        return cp;
    }

    public void setCp(int cp) {
        this.cp = cp;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<domain_Profil> getDomain_profils() {
        return domain_profils;
    }

    public void addDomain_profil(Domain_profil domain_profil) {
        this.domain_profils.add(domain_profil);
    }
    public domain_Trajet getDomain_trajet() {
        return domain_trajet;
    }

    public void setDomain_trajet(domain_Trajet domain_trajet) {
        this.domain_trajet = domain_trajet;
    }

}