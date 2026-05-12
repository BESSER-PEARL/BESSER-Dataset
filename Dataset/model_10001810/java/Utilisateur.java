





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private int pizzeria_id;
    private int role_id;
    private String civilit_;
    private String date_naissance;
    private String email;
    private String prenom;
    private String nom;
    private int id;
    private String mot_de_passe;



    public Utilisateur(
        int pizzeria_id,        int role_id,        String civilit_,        String date_naissance,        String email,        String prenom,        String nom,        int id,        String mot_de_passe    ) {
        this.pizzeria_id = pizzeria_id;
        this.role_id = role_id;
        this.civilit_ = civilit_;
        this.date_naissance = date_naissance;
        this.email = email;
        this.prenom = prenom;
        this.nom = nom;
        this.id = id;
        this.mot_de_passe = mot_de_passe;
    }


    public int getPizzeria_id() {
        return pizzeria_id;
    }

    public void setPizzeria_id(int pizzeria_id) {
        this.pizzeria_id = pizzeria_id;
    }
    public int getRole_id() {
        return role_id;
    }

    public void setRole_id(int role_id) {
        this.role_id = role_id;
    }
    public String getCivilit_() {
        return civilit_;
    }

    public void setCivilit_(String civilit_) {
        this.civilit_ = civilit_;
    }
    public String getDate_naissance() {
        return date_naissance;
    }

    public void setDate_naissance(String date_naissance) {
        this.date_naissance = date_naissance;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getMot_de_passe() {
        return mot_de_passe;
    }

    public void setMot_de_passe(String mot_de_passe) {
        this.mot_de_passe = mot_de_passe;
    }


}