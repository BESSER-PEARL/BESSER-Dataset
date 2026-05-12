





import java.util.List;
import java.util.ArrayList;

public class Registrieren  {

    private String nachname;
    private String geburtsdatum;
    private String passwort;
    private String email;
    private String vorname;
    private String geschlecht;





    private Benutzer benutzer;


    public Registrieren(
        String nachname,        String geburtsdatum,        String passwort,        String email,        String vorname,        String geschlecht    ) {
        this.nachname = nachname;
        this.geburtsdatum = geburtsdatum;
        this.passwort = passwort;
        this.email = email;
        this.vorname = vorname;
        this.geschlecht = geschlecht;
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
    public String getPasswort() {
        return passwort;
    }

    public void setPasswort(String passwort) {
        this.passwort = passwort;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getVorname() {
        return vorname;
    }

    public void setVorname(String vorname) {
        this.vorname = vorname;
    }
    public String getGeschlecht() {
        return geschlecht;
    }

    public void setGeschlecht(String geschlecht) {
        this.geschlecht = geschlecht;
    }

    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}