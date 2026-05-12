





import java.util.List;
import java.util.ArrayList;

public class Auftrag  {

    private String keks;
    private String name;
    private String anzahl;





    private Plaetzchen plaetzchen;




    private PlaetzchenDesignerForm plaetzchendesignerform;




    private DateiEA dateiea;


    public Auftrag(
        String keks,        String name,        String anzahl    ) {
        this.keks = keks;
        this.name = name;
        this.anzahl = anzahl;
    }


    public String getKeks() {
        return keks;
    }

    public void setKeks(String keks) {
        this.keks = keks;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAnzahl() {
        return anzahl;
    }

    public void setAnzahl(String anzahl) {
        this.anzahl = anzahl;
    }

    public Plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(Plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public PlaetzchenDesignerForm getPlaetzchendesignerform() {
        return plaetzchendesignerform;
    }

    public void setPlaetzchendesignerform(PlaetzchenDesignerForm plaetzchendesignerform) {
        this.plaetzchendesignerform = plaetzchendesignerform;
    }
    public DateiEA getDateiea() {
        return dateiea;
    }

    public void setDateiea(DateiEA dateiea) {
        this.dateiea = dateiea;
    }

}