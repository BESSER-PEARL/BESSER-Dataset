





import java.util.List;
import java.util.ArrayList;

public class zlvp_Legenda  {

    private String bemerkung;
    private String nachname;
    private String telNr;
    private String faxNr;
    private String firma;
    private String strasse;
    private String vorname;
    private String plz;
    private int id;
    private String email;
    private String handyNr;
    private String ort;





    private zlvp_Anrede zlvp_anrede;




    private zlvp_Lagerort zlvp_lagerort;


    public zlvp_Legenda(
        String bemerkung,        String nachname,        String telNr,        String faxNr,        String firma,        String strasse,        String vorname,        String plz,        int id,        String email,        String handyNr,        String ort    ) {
        this.bemerkung = bemerkung;
        this.nachname = nachname;
        this.telNr = telNr;
        this.faxNr = faxNr;
        this.firma = firma;
        this.strasse = strasse;
        this.vorname = vorname;
        this.plz = plz;
        this.id = id;
        this.email = email;
        this.handyNr = handyNr;
        this.ort = ort;
    }


    public String getBemerkung() {
        return bemerkung;
    }

    public void setBemerkung(String bemerkung) {
        this.bemerkung = bemerkung;
    }
    public String getNachname() {
        return nachname;
    }

    public void setNachname(String nachname) {
        this.nachname = nachname;
    }
    public String getTelnr() {
        return telNr;
    }

    public void setTelnr(String telNr) {
        this.telNr = telNr;
    }
    public String getFaxnr() {
        return faxNr;
    }

    public void setFaxnr(String faxNr) {
        this.faxNr = faxNr;
    }
    public String getFirma() {
        return firma;
    }

    public void setFirma(String firma) {
        this.firma = firma;
    }
    public String getStrasse() {
        return strasse;
    }

    public void setStrasse(String strasse) {
        this.strasse = strasse;
    }
    public String getVorname() {
        return vorname;
    }

    public void setVorname(String vorname) {
        this.vorname = vorname;
    }
    public String getPlz() {
        return plz;
    }

    public void setPlz(String plz) {
        this.plz = plz;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getHandynr() {
        return handyNr;
    }

    public void setHandynr(String handyNr) {
        this.handyNr = handyNr;
    }
    public String getOrt() {
        return ort;
    }

    public void setOrt(String ort) {
        this.ort = ort;
    }

    public zlvp_Anrede getZlvp_anrede() {
        return zlvp_anrede;
    }

    public void setZlvp_anrede(zlvp_Anrede zlvp_anrede) {
        this.zlvp_anrede = zlvp_anrede;
    }
    public zlvp_Lagerort getZlvp_lagerort() {
        return zlvp_lagerort;
    }

    public void setZlvp_lagerort(zlvp_Lagerort zlvp_lagerort) {
        this.zlvp_lagerort = zlvp_lagerort;
    }

}