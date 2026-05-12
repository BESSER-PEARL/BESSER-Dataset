





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private None password;
    private String fname;
    private String lname;





    private Utilisateur utilisateur;


    public Registration(
        String userName,        None password,        String fname,        String lname    ) {
        this.userName = userName;
        this.password = password;
        this.fname = fname;
        this.lname = lname;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}