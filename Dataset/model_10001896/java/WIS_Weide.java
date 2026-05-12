





import java.util.List;
import java.util.ArrayList;

public class WIS_Weide  {

    private String farbe;
    private String name;
    private boolean istAktiv;
    private boolean istBetriebsfremdeFlaeche;
    private String bemerkung;
    private int FACTCode;
    private int groesse;
    private String LPRVertrag;
    private int schlagnummer;





    private List<WIS_Weidefl_che> wis_weidefl_ches;




    private Benutzer benutzer;


    public WIS_Weide(
        String farbe,        String name,        boolean istAktiv,        boolean istBetriebsfremdeFlaeche,        String bemerkung,        int FACTCode,        int groesse,        String LPRVertrag,        int schlagnummer    ) {
        this.farbe = farbe;
        this.name = name;
        this.istAktiv = istAktiv;
        this.istBetriebsfremdeFlaeche = istBetriebsfremdeFlaeche;
        this.bemerkung = bemerkung;
        this.FACTCode = FACTCode;
        this.groesse = groesse;
        this.LPRVertrag = LPRVertrag;
        this.schlagnummer = schlagnummer;
        this.wis_weidefl_ches = new ArrayList<>();
    }

    public WIS_Weide(
        String farbe,        String name,        boolean istAktiv,        boolean istBetriebsfremdeFlaeche,        String bemerkung,        int FACTCode,        int groesse,        String LPRVertrag,        int schlagnummer        ArrayList<WIS_Weidefl_che> wis_weidefl_ches    ) {
        this.farbe = farbe;
        this.name = name;
        this.istAktiv = istAktiv;
        this.istBetriebsfremdeFlaeche = istBetriebsfremdeFlaeche;
        this.bemerkung = bemerkung;
        this.FACTCode = FACTCode;
        this.groesse = groesse;
        this.LPRVertrag = LPRVertrag;
        this.schlagnummer = schlagnummer;
        this.wis_weidefl_ches = wis_weidefl_ches;
    }

    public String getFarbe() {
        return farbe;
    }

    public void setFarbe(String farbe) {
        this.farbe = farbe;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIstaktiv() {
        return istAktiv;
    }

    public void setIstaktiv(boolean istAktiv) {
        this.istAktiv = istAktiv;
    }
    public boolean getIstbetriebsfremdeflaeche() {
        return istBetriebsfremdeFlaeche;
    }

    public void setIstbetriebsfremdeflaeche(boolean istBetriebsfremdeFlaeche) {
        this.istBetriebsfremdeFlaeche = istBetriebsfremdeFlaeche;
    }
    public String getBemerkung() {
        return bemerkung;
    }

    public void setBemerkung(String bemerkung) {
        this.bemerkung = bemerkung;
    }
    public int getFactcode() {
        return FACTCode;
    }

    public void setFactcode(int FACTCode) {
        this.FACTCode = FACTCode;
    }
    public int getGroesse() {
        return groesse;
    }

    public void setGroesse(int groesse) {
        this.groesse = groesse;
    }
    public String getLprvertrag() {
        return LPRVertrag;
    }

    public void setLprvertrag(String LPRVertrag) {
        this.LPRVertrag = LPRVertrag;
    }
    public int getSchlagnummer() {
        return schlagnummer;
    }

    public void setSchlagnummer(int schlagnummer) {
        this.schlagnummer = schlagnummer;
    }

    public List<WIS_Weidefl_che> getWis_weidefl_ches() {
        return wis_weidefl_ches;
    }

    public void addWis_weidefl_che(Wis_weidefl_che wis_weidefl_che) {
        this.wis_weidefl_ches.add(wis_weidefl_che);
    }
    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}