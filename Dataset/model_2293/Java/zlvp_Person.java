




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Person  {

    private String handyNr;
    private LocalDate gebDat;
    private String strasse;
    private String telNr;
    private String plz;
    private String version;
    private String nachname;
    private String email;
    private String vorname;
    private String ort;
    private int id;
    private String notTelNr;





    private zlvp_Geschlecht zlvp_geschlecht;


    public zlvp_Person(
        String handyNr,        LocalDate gebDat,        String strasse,        String telNr,        String plz,        String version,        String nachname,        String email,        String vorname,        String ort,        int id,        String notTelNr    ) {
        this.handyNr = handyNr;
        this.gebDat = gebDat;
        this.strasse = strasse;
        this.telNr = telNr;
        this.plz = plz;
        this.version = version;
        this.nachname = nachname;
        this.email = email;
        this.vorname = vorname;
        this.ort = ort;
        this.id = id;
        this.notTelNr = notTelNr;
    }


    public String getHandynr() {
        return handyNr;
    }

    public void setHandynr(String handyNr) {
        this.handyNr = handyNr;
    }
    public LocalDate getGebdat() {
        return gebDat;
    }

    public void setGebdat(LocalDate gebDat) {
        this.gebDat = gebDat;
    }
    public String getStrasse() {
        return strasse;
    }

    public void setStrasse(String strasse) {
        this.strasse = strasse;
    }
    public String getTelnr() {
        return telNr;
    }

    public void setTelnr(String telNr) {
        this.telNr = telNr;
    }
    public String getPlz() {
        return plz;
    }

    public void setPlz(String plz) {
        this.plz = plz;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getNachname() {
        return nachname;
    }

    public void setNachname(String nachname) {
        this.nachname = nachname;
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
    public String getOrt() {
        return ort;
    }

    public void setOrt(String ort) {
        this.ort = ort;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNottelnr() {
        return notTelNr;
    }

    public void setNottelnr(String notTelNr) {
        this.notTelNr = notTelNr;
    }

    public zlvp_Geschlecht getZlvp_geschlecht() {
        return zlvp_geschlecht;
    }

    public void setZlvp_geschlecht(zlvp_Geschlecht zlvp_geschlecht) {
        this.zlvp_geschlecht = zlvp_geschlecht;
    }

}