





import java.util.List;
import java.util.ArrayList;

public class Registrieren  {

    private String geschlecht;
    private String passwort;
    private String vorname;
    private String email1;
    private String nachname;
    private String geburtsdatum;
    private String email;



    public Registrieren(
        String geschlecht,        String passwort,        String vorname,        String email1,        String nachname,        String geburtsdatum,        String email    ) {
        this.geschlecht = geschlecht;
        this.passwort = passwort;
        this.vorname = vorname;
        this.email1 = email1;
        this.nachname = nachname;
        this.geburtsdatum = geburtsdatum;
        this.email = email;
    }


    public String getGeschlecht() {
        return geschlecht;
    }

    public void setGeschlecht(String geschlecht) {
        this.geschlecht = geschlecht;
    }
    public String getPasswort() {
        return passwort;
    }

    public void setPasswort(String passwort) {
        this.passwort = passwort;
    }
    public String getVorname() {
        return vorname;
    }

    public void setVorname(String vorname) {
        this.vorname = vorname;
    }
    public String getEmail1() {
        return email1;
    }

    public void setEmail1(String email1) {
        this.email1 = email1;
    }
    public String getNachname() {
        return nachname;
    }

    public void setNachname(String nachname) {
        this.nachname = nachname;
    }
    public String getGeburtsdatum() {
        return geburtsdatum;
    }

    public void setGeburtsdatum(String geburtsdatum) {
        this.geburtsdatum = geburtsdatum;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}