





import java.util.List;
import java.util.ArrayList;

public class covoiturage_Personne  {

    private String mail;
    private String nom;
    private String prenom;
    private String tel;
    private int id;



    public covoiturage_Personne(
        String mail,        String nom,        String prenom,        String tel,        int id    ) {
        this.mail = mail;
        this.nom = nom;
        this.prenom = prenom;
        this.tel = tel;
        this.id = id;
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
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
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


}