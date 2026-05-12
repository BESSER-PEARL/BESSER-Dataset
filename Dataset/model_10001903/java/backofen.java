





import java.util.List;
import java.util.ArrayList;

public class backofen  {

    private String bandgeschwindigkeit;
    private String backzeit;
    private None teigmaschine;
    private String ofenlaenge;
    private String backtemp;





    private auftrag auftrag;


    public backofen(
        String bandgeschwindigkeit,        String backzeit,        None teigmaschine,        String ofenlaenge,        String backtemp    ) {
        this.bandgeschwindigkeit = bandgeschwindigkeit;
        this.backzeit = backzeit;
        this.teigmaschine = teigmaschine;
        this.ofenlaenge = ofenlaenge;
        this.backtemp = backtemp;
    }


    public String getBandgeschwindigkeit() {
        return bandgeschwindigkeit;
    }

    public void setBandgeschwindigkeit(String bandgeschwindigkeit) {
        this.bandgeschwindigkeit = bandgeschwindigkeit;
    }
    public String getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(String backzeit) {
        this.backzeit = backzeit;
    }
    public None getTeigmaschine() {
        return teigmaschine;
    }

    public void setTeigmaschine(None teigmaschine) {
        this.teigmaschine = teigmaschine;
    }
    public String getOfenlaenge() {
        return ofenlaenge;
    }

    public void setOfenlaenge(String ofenlaenge) {
        this.ofenlaenge = ofenlaenge;
    }
    public String getBacktemp() {
        return backtemp;
    }

    public void setBacktemp(String backtemp) {
        this.backtemp = backtemp;
    }

    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }

}