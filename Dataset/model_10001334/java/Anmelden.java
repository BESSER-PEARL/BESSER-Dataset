





import java.util.List;
import java.util.ArrayList;

public class Anmelden  {

    private String email;
    private String passwort;





    private Benutzer benutzer;


    public Anmelden(
        String email,        String passwort    ) {
        this.email = email;
        this.passwort = passwort;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPasswort() {
        return passwort;
    }

    public void setPasswort(String passwort) {
        this.passwort = passwort;
    }

    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}