




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String photo;
    private String telephone;
    private LocalDate naissance;
    private String prenom;
    private String mail;
    private String nom;
    private int id;



    public Personne(
        String photo,        String telephone,        LocalDate naissance,        String prenom,        String mail,        String nom,        int id    ) {
        this.photo = photo;
        this.telephone = telephone;
        this.naissance = naissance;
        this.prenom = prenom;
        this.mail = mail;
        this.nom = nom;
        this.id = id;
    }


    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public LocalDate getNaissance() {
        return naissance;
    }

    public void setNaissance(LocalDate naissance) {
        this.naissance = naissance;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
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


}