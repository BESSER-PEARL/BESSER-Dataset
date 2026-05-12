





import java.util.List;
import java.util.ArrayList;

public class domain_Profil  {

    private String mail;
    private String nom;
    private String tel;
    private int id;
    private None role;
    private String prenom;



    public domain_Profil(
        String mail,        String nom,        String tel,        int id,        None role,        String prenom    ) {
        this.mail = mail;
        this.nom = nom;
        this.tel = tel;
        this.id = id;
        this.role = role;
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
    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getRole() {
        return role;
    }

    public void setRole(None role) {
        this.role = role;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }


}