





import java.util.List;
import java.util.ArrayList;

public class auftrag  {

    private String name;
    private String auftragsPlaetzchen;
    private String anzahl;





    private plaetzchen plaetzchen;




    private zutat zutat;


    public auftrag(
        String name,        String auftragsPlaetzchen,        String anzahl    ) {
        this.name = name;
        this.auftragsPlaetzchen = auftragsPlaetzchen;
        this.anzahl = anzahl;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuftragsplaetzchen() {
        return auftragsPlaetzchen;
    }

    public void setAuftragsplaetzchen(String auftragsPlaetzchen) {
        this.auftragsPlaetzchen = auftragsPlaetzchen;
    }
    public String getAnzahl() {
        return anzahl;
    }

    public void setAnzahl(String anzahl) {
        this.anzahl = anzahl;
    }

    public plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public zutat getZutat() {
        return zutat;
    }

    public void setZutat(zutat zutat) {
        this.zutat = zutat;
    }

}