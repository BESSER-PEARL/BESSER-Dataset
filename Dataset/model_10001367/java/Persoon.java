





import java.util.List;
import java.util.ArrayList;

public class Persoon  {

    private String voornaam;
    private String wachtwoord;
    private String tussenvoegsel;
    private String achternaam;
    private String e_mail;



    public Persoon(
        String voornaam,        String wachtwoord,        String tussenvoegsel,        String achternaam,        String e_mail    ) {
        this.voornaam = voornaam;
        this.wachtwoord = wachtwoord;
        this.tussenvoegsel = tussenvoegsel;
        this.achternaam = achternaam;
        this.e_mail = e_mail;
    }


    public String getVoornaam() {
        return voornaam;
    }

    public void setVoornaam(String voornaam) {
        this.voornaam = voornaam;
    }
    public String getWachtwoord() {
        return wachtwoord;
    }

    public void setWachtwoord(String wachtwoord) {
        this.wachtwoord = wachtwoord;
    }
    public String getTussenvoegsel() {
        return tussenvoegsel;
    }

    public void setTussenvoegsel(String tussenvoegsel) {
        this.tussenvoegsel = tussenvoegsel;
    }
    public String getAchternaam() {
        return achternaam;
    }

    public void setAchternaam(String achternaam) {
        this.achternaam = achternaam;
    }
    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }


}