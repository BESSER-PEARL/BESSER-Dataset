





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private String Nom;
    private String Pr_nom;
    private String Login;
    private String Telephone;
    private String Password;
    private String Mail;
    private int id_utilisateur;



    public Utilisateur(
        String Nom,        String Pr_nom,        String Login,        String Telephone,        String Password,        String Mail,        int id_utilisateur    ) {
        this.Nom = Nom;
        this.Pr_nom = Pr_nom;
        this.Login = Login;
        this.Telephone = Telephone;
        this.Password = Password;
        this.Mail = Mail;
        this.id_utilisateur = id_utilisateur;
    }


    public String getNom() {
        return Nom;
    }

    public void setNom(String Nom) {
        this.Nom = Nom;
    }
    public String getPr_nom() {
        return Pr_nom;
    }

    public void setPr_nom(String Pr_nom) {
        this.Pr_nom = Pr_nom;
    }
    public String getLogin() {
        return Login;
    }

    public void setLogin(String Login) {
        this.Login = Login;
    }
    public String getTelephone() {
        return Telephone;
    }

    public void setTelephone(String Telephone) {
        this.Telephone = Telephone;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }
    public int getId_utilisateur() {
        return id_utilisateur;
    }

    public void setId_utilisateur(int id_utilisateur) {
        this.id_utilisateur = id_utilisateur;
    }


}