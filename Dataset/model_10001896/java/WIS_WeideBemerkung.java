





import java.util.List;
import java.util.ArrayList;

public class WIS_WeideBemerkung  {

    private String weideSchlagnummer;
    private String bemerkung;
    private String weideName;
    private String datum;
    private String weideFACTCode;



    public WIS_WeideBemerkung(
        String weideSchlagnummer,        String bemerkung,        String weideName,        String datum,        String weideFACTCode    ) {
        this.weideSchlagnummer = weideSchlagnummer;
        this.bemerkung = bemerkung;
        this.weideName = weideName;
        this.datum = datum;
        this.weideFACTCode = weideFACTCode;
    }


    public String getWeideschlagnummer() {
        return weideSchlagnummer;
    }

    public void setWeideschlagnummer(String weideSchlagnummer) {
        this.weideSchlagnummer = weideSchlagnummer;
    }
    public String getBemerkung() {
        return bemerkung;
    }

    public void setBemerkung(String bemerkung) {
        this.bemerkung = bemerkung;
    }
    public String getWeidename() {
        return weideName;
    }

    public void setWeidename(String weideName) {
        this.weideName = weideName;
    }
    public String getDatum() {
        return datum;
    }

    public void setDatum(String datum) {
        this.datum = datum;
    }
    public String getWeidefactcode() {
        return weideFACTCode;
    }

    public void setWeidefactcode(String weideFACTCode) {
        this.weideFACTCode = weideFACTCode;
    }


}