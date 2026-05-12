





import java.util.List;
import java.util.ArrayList;

public class Benutzer  {

    private String Vorname;
    private String Nachname;
    private String Info;
    private String profilbild;



    public Benutzer(
        String Vorname,        String Nachname,        String Info,        String profilbild    ) {
        this.Vorname = Vorname;
        this.Nachname = Nachname;
        this.Info = Info;
        this.profilbild = profilbild;
    }


    public String getVorname() {
        return Vorname;
    }

    public void setVorname(String Vorname) {
        this.Vorname = Vorname;
    }
    public String getNachname() {
        return Nachname;
    }

    public void setNachname(String Nachname) {
        this.Nachname = Nachname;
    }
    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }
    public String getProfilbild() {
        return profilbild;
    }

    public void setProfilbild(String profilbild) {
        this.profilbild = profilbild;
    }


}