





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Passager  {

    private String nom;
    private int id;
    private int tel;
    private String mail;
    private String prenom;



    public Covoiturage_Passager(
        String nom,        int id,        int tel,        String mail,        String prenom    ) {
        this.nom = nom;
        this.id = id;
        this.tel = tel;
        this.mail = mail;
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
    public int getTel() {
        return tel;
    }

    public void setTel(int tel) {
        this.tel = tel;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }


}