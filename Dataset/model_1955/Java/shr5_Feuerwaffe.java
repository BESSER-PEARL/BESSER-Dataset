





import java.util.List;
import java.util.ArrayList;

public class shr5_Feuerwaffe extends AbstaktFernKampfwaffe {

    private String erweiterung;
    private int rueckstoss;
    private String modie;
    private String munitionstyp;
    private int kapazitaet;





    private shr5_Magazin shr5_magazin;




    private shr5_Magazin shr5_magazin;




    private List<shr5_FernkampfwaffeModifikator> shr5_fernkampfwaffemodifikators;


    public shr5_Feuerwaffe(
        String erweiterung,        int rueckstoss,        String modie,        String munitionstyp,        int kapazitaet    ) {
        super(
        );
        this.erweiterung = erweiterung;
        this.rueckstoss = rueckstoss;
        this.modie = modie;
        this.munitionstyp = munitionstyp;
        this.kapazitaet = kapazitaet;
        this.shr5_fernkampfwaffemodifikators = new ArrayList<>();
    }

    public shr5_Feuerwaffe(
        String erweiterung,        int rueckstoss,        String modie,        String munitionstyp,        int kapazitaet        ArrayList<shr5_FernkampfwaffeModifikator> shr5_fernkampfwaffemodifikators    ) {
        this.erweiterung = erweiterung;
        this.rueckstoss = rueckstoss;
        this.modie = modie;
        this.munitionstyp = munitionstyp;
        this.kapazitaet = kapazitaet;
        this.shr5_fernkampfwaffemodifikators = shr5_fernkampfwaffemodifikators;
    }

    public String getErweiterung() {
        return erweiterung;
    }

    public void setErweiterung(String erweiterung) {
        this.erweiterung = erweiterung;
    }
    public int getRueckstoss() {
        return rueckstoss;
    }

    public void setRueckstoss(int rueckstoss) {
        this.rueckstoss = rueckstoss;
    }
    public String getModie() {
        return modie;
    }

    public void setModie(String modie) {
        this.modie = modie;
    }
    public String getMunitionstyp() {
        return munitionstyp;
    }

    public void setMunitionstyp(String munitionstyp) {
        this.munitionstyp = munitionstyp;
    }
    public int getKapazitaet() {
        return kapazitaet;
    }

    public void setKapazitaet(int kapazitaet) {
        this.kapazitaet = kapazitaet;
    }

    public shr5_Magazin getShr5_magazin() {
        return shr5_magazin;
    }

    public void setShr5_magazin(shr5_Magazin shr5_magazin) {
        this.shr5_magazin = shr5_magazin;
    }
    public shr5_Magazin getShr5_magazin() {
        return shr5_magazin;
    }

    public void setShr5_magazin(shr5_Magazin shr5_magazin) {
        this.shr5_magazin = shr5_magazin;
    }
    public List<shr5_FernkampfwaffeModifikator> getShr5_fernkampfwaffemodifikators() {
        return shr5_fernkampfwaffemodifikators;
    }

    public void addShr5_fernkampfwaffemodifikator(Shr5_fernkampfwaffemodifikator shr5_fernkampfwaffemodifikator) {
        this.shr5_fernkampfwaffemodifikators.add(shr5_fernkampfwaffemodifikator);
    }

}