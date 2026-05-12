





import java.util.List;
import java.util.ArrayList;

public class Weidegang2  {

    private String weideName;
    private boolean istAusgefallen;
    private String herdeFarbe;
    private String datum;
    private String herdeName;
    private String tierName;
    private String weideSchlagnummer;
    private String ausfallgrund;
    private String weideFACTCode;



    public Weidegang2(
        String weideName,        boolean istAusgefallen,        String herdeFarbe,        String datum,        String herdeName,        String tierName,        String weideSchlagnummer,        String ausfallgrund,        String weideFACTCode    ) {
        this.weideName = weideName;
        this.istAusgefallen = istAusgefallen;
        this.herdeFarbe = herdeFarbe;
        this.datum = datum;
        this.herdeName = herdeName;
        this.tierName = tierName;
        this.weideSchlagnummer = weideSchlagnummer;
        this.ausfallgrund = ausfallgrund;
        this.weideFACTCode = weideFACTCode;
    }


    public String getWeidename() {
        return weideName;
    }

    public void setWeidename(String weideName) {
        this.weideName = weideName;
    }
    public boolean getIstausgefallen() {
        return istAusgefallen;
    }

    public void setIstausgefallen(boolean istAusgefallen) {
        this.istAusgefallen = istAusgefallen;
    }
    public String getHerdefarbe() {
        return herdeFarbe;
    }

    public void setHerdefarbe(String herdeFarbe) {
        this.herdeFarbe = herdeFarbe;
    }
    public String getDatum() {
        return datum;
    }

    public void setDatum(String datum) {
        this.datum = datum;
    }
    public String getHerdename() {
        return herdeName;
    }

    public void setHerdename(String herdeName) {
        this.herdeName = herdeName;
    }
    public String getTiername() {
        return tierName;
    }

    public void setTiername(String tierName) {
        this.tierName = tierName;
    }
    public String getWeideschlagnummer() {
        return weideSchlagnummer;
    }

    public void setWeideschlagnummer(String weideSchlagnummer) {
        this.weideSchlagnummer = weideSchlagnummer;
    }
    public String getAusfallgrund() {
        return ausfallgrund;
    }

    public void setAusfallgrund(String ausfallgrund) {
        this.ausfallgrund = ausfallgrund;
    }
    public String getWeidefactcode() {
        return weideFACTCode;
    }

    public void setWeidefactcode(String weideFACTCode) {
        this.weideFACTCode = weideFACTCode;
    }


}