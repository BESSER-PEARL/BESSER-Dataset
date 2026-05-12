





import java.util.List;
import java.util.ArrayList;

public class Membres  {

    private String mdp;
    private String email;
    private String idM;
    private String nom;
    private String prenom;
    private int telephone;



    public Membres(
        String mdp,        String email,        String idM,        String nom,        String prenom,        int telephone    ) {
        this.mdp = mdp;
        this.email = email;
        this.idM = idM;
        this.nom = nom;
        this.prenom = prenom;
        this.telephone = telephone;
    }


    public String getMdp() {
        return mdp;
    }

    public void setMdp(String mdp) {
        this.mdp = mdp;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getIdm() {
        return idM;
    }

    public void setIdm(String idM) {
        this.idM = idM;
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
    public int getTelephone() {
        return telephone;
    }

    public void setTelephone(int telephone) {
        this.telephone = telephone;
    }


}