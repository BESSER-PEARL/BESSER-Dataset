





import java.util.List;
import java.util.ArrayList;

public class backstrasse  {

    private String ofenlaenge;
    private String BLECHLAENGE;
    private String gestoppt;
    private String geschwindigkeit;
    private String temperatur;
    private String zutatenVorrat;
    private String eingabeAusgabe;
    private String backAuftrag;
    private String BLECHBREITE;





    private zutat zutat;




    private auftrag auftrag;


    public backstrasse(
        String ofenlaenge,        String BLECHLAENGE,        String gestoppt,        String geschwindigkeit,        String temperatur,        String zutatenVorrat,        String eingabeAusgabe,        String backAuftrag,        String BLECHBREITE    ) {
        this.ofenlaenge = ofenlaenge;
        this.BLECHLAENGE = BLECHLAENGE;
        this.gestoppt = gestoppt;
        this.geschwindigkeit = geschwindigkeit;
        this.temperatur = temperatur;
        this.zutatenVorrat = zutatenVorrat;
        this.eingabeAusgabe = eingabeAusgabe;
        this.backAuftrag = backAuftrag;
        this.BLECHBREITE = BLECHBREITE;
    }


    public String getOfenlaenge() {
        return ofenlaenge;
    }

    public void setOfenlaenge(String ofenlaenge) {
        this.ofenlaenge = ofenlaenge;
    }
    public String getBlechlaenge() {
        return BLECHLAENGE;
    }

    public void setBlechlaenge(String BLECHLAENGE) {
        this.BLECHLAENGE = BLECHLAENGE;
    }
    public String getGestoppt() {
        return gestoppt;
    }

    public void setGestoppt(String gestoppt) {
        this.gestoppt = gestoppt;
    }
    public String getGeschwindigkeit() {
        return geschwindigkeit;
    }

    public void setGeschwindigkeit(String geschwindigkeit) {
        this.geschwindigkeit = geschwindigkeit;
    }
    public String getTemperatur() {
        return temperatur;
    }

    public void setTemperatur(String temperatur) {
        this.temperatur = temperatur;
    }
    public String getZutatenvorrat() {
        return zutatenVorrat;
    }

    public void setZutatenvorrat(String zutatenVorrat) {
        this.zutatenVorrat = zutatenVorrat;
    }
    public String getEingabeausgabe() {
        return eingabeAusgabe;
    }

    public void setEingabeausgabe(String eingabeAusgabe) {
        this.eingabeAusgabe = eingabeAusgabe;
    }
    public String getBackauftrag() {
        return backAuftrag;
    }

    public void setBackauftrag(String backAuftrag) {
        this.backAuftrag = backAuftrag;
    }
    public String getBlechbreite() {
        return BLECHBREITE;
    }

    public void setBlechbreite(String BLECHBREITE) {
        this.BLECHBREITE = BLECHBREITE;
    }

    public zutat getZutat() {
        return zutat;
    }

    public void setZutat(zutat zutat) {
        this.zutat = zutat;
    }
    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }

}