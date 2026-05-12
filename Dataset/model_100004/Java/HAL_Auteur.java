





import java.util.List;
import java.util.ArrayList;

public class HAL_Auteur  {

    private String email;
    private String urlPerso;
    private String prenom;
    private String autrePrenom;
    private String nom;





    private Laboratoire laboratoire;


    public HAL_Auteur(
        String email,        String urlPerso,        String prenom,        String autrePrenom,        String nom    ) {
        this.email = email;
        this.urlPerso = urlPerso;
        this.prenom = prenom;
        this.autrePrenom = autrePrenom;
        this.nom = nom;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUrlperso() {
        return urlPerso;
    }

    public void setUrlperso(String urlPerso) {
        this.urlPerso = urlPerso;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getAutreprenom() {
        return autrePrenom;
    }

    public void setAutreprenom(String autrePrenom) {
        this.autrePrenom = autrePrenom;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public Laboratoire getLaboratoire() {
        return laboratoire;
    }

    public void setLaboratoire(Laboratoire laboratoire) {
        this.laboratoire = laboratoire;
    }

}