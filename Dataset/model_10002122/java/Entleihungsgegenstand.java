





import java.util.List;
import java.util.ArrayList;

public class Entleihungsgegenstand  {

    private String kurzbeschreibung;
    private String titel;
    private String einkaufspreis;



    public Entleihungsgegenstand(
        String kurzbeschreibung,        String titel,        String einkaufspreis    ) {
        this.kurzbeschreibung = kurzbeschreibung;
        this.titel = titel;
        this.einkaufspreis = einkaufspreis;
    }


    public String getKurzbeschreibung() {
        return kurzbeschreibung;
    }

    public void setKurzbeschreibung(String kurzbeschreibung) {
        this.kurzbeschreibung = kurzbeschreibung;
    }
    public String getTitel() {
        return titel;
    }

    public void setTitel(String titel) {
        this.titel = titel;
    }
    public String getEinkaufspreis() {
        return einkaufspreis;
    }

    public void setEinkaufspreis(String einkaufspreis) {
        this.einkaufspreis = einkaufspreis;
    }


}