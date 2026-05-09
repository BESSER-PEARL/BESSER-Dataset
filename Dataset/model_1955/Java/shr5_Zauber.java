





import java.util.List;
import java.util.ArrayList;

public class shr5_Zauber extends Quelle, Beschreibbar {

    private String entzug;
    private String schaden;
    private String reichweite;
    private String dauer;
    private String merkmale;
    private String art;
    private String kategorie;



    public shr5_Zauber(
        String entzug,        String schaden,        String reichweite,        String dauer,        String merkmale,        String art,        String kategorie    ) {
        super(
        );
        this.entzug = entzug;
        this.schaden = schaden;
        this.reichweite = reichweite;
        this.dauer = dauer;
        this.merkmale = merkmale;
        this.art = art;
        this.kategorie = kategorie;
    }


    public String getEntzug() {
        return entzug;
    }

    public void setEntzug(String entzug) {
        this.entzug = entzug;
    }
    public String getSchaden() {
        return schaden;
    }

    public void setSchaden(String schaden) {
        this.schaden = schaden;
    }
    public String getReichweite() {
        return reichweite;
    }

    public void setReichweite(String reichweite) {
        this.reichweite = reichweite;
    }
    public String getDauer() {
        return dauer;
    }

    public void setDauer(String dauer) {
        this.dauer = dauer;
    }
    public String getMerkmale() {
        return merkmale;
    }

    public void setMerkmale(String merkmale) {
        this.merkmale = merkmale;
    }
    public String getArt() {
        return art;
    }

    public void setArt(String art) {
        this.art = art;
    }
    public String getKategorie() {
        return kategorie;
    }

    public void setKategorie(String kategorie) {
        this.kategorie = kategorie;
    }


}