





import java.util.List;
import java.util.ArrayList;

public class WIS_Weidegang  {

    private String tierLOM;
    private boolean istAusgefallen;
    private String weideSchlagnummer;
    private String tierName;
    private String ausfallgrund;
    private String herdeName;
    private String weideFACTCode;
    private String weideName;
    private String herdeFarbe;
    private String datum;





    private WIS_Weide wis_weide;




    private Benutzer benutzer;


    public WIS_Weidegang(
        String tierLOM,        boolean istAusgefallen,        String weideSchlagnummer,        String tierName,        String ausfallgrund,        String herdeName,        String weideFACTCode,        String weideName,        String herdeFarbe,        String datum    ) {
        this.tierLOM = tierLOM;
        this.istAusgefallen = istAusgefallen;
        this.weideSchlagnummer = weideSchlagnummer;
        this.tierName = tierName;
        this.ausfallgrund = ausfallgrund;
        this.herdeName = herdeName;
        this.weideFACTCode = weideFACTCode;
        this.weideName = weideName;
        this.herdeFarbe = herdeFarbe;
        this.datum = datum;
    }


    public String getTierlom() {
        return tierLOM;
    }

    public void setTierlom(String tierLOM) {
        this.tierLOM = tierLOM;
    }
    public boolean getIstausgefallen() {
        return istAusgefallen;
    }

    public void setIstausgefallen(boolean istAusgefallen) {
        this.istAusgefallen = istAusgefallen;
    }
    public String getWeideschlagnummer() {
        return weideSchlagnummer;
    }

    public void setWeideschlagnummer(String weideSchlagnummer) {
        this.weideSchlagnummer = weideSchlagnummer;
    }
    public String getTiername() {
        return tierName;
    }

    public void setTiername(String tierName) {
        this.tierName = tierName;
    }
    public String getAusfallgrund() {
        return ausfallgrund;
    }

    public void setAusfallgrund(String ausfallgrund) {
        this.ausfallgrund = ausfallgrund;
    }
    public String getHerdename() {
        return herdeName;
    }

    public void setHerdename(String herdeName) {
        this.herdeName = herdeName;
    }
    public String getWeidefactcode() {
        return weideFACTCode;
    }

    public void setWeidefactcode(String weideFACTCode) {
        this.weideFACTCode = weideFACTCode;
    }
    public String getWeidename() {
        return weideName;
    }

    public void setWeidename(String weideName) {
        this.weideName = weideName;
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

    public WIS_Weide getWis_weide() {
        return wis_weide;
    }

    public void setWis_weide(WIS_Weide wis_weide) {
        this.wis_weide = wis_weide;
    }
    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}