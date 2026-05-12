





import java.util.List;
import java.util.ArrayList;

public class Plaetzchen  {

    private String teig;
    private String belag;
    private String laenge;
    private String breite;
    private String form;
    private String temperatur;
    private String backzeit;





    private Zutaten zutaten;




    private Zutat zutat;


    public Plaetzchen(
        String teig,        String belag,        String laenge,        String breite,        String form,        String temperatur,        String backzeit    ) {
        this.teig = teig;
        this.belag = belag;
        this.laenge = laenge;
        this.breite = breite;
        this.form = form;
        this.temperatur = temperatur;
        this.backzeit = backzeit;
    }


    public String getTeig() {
        return teig;
    }

    public void setTeig(String teig) {
        this.teig = teig;
    }
    public String getBelag() {
        return belag;
    }

    public void setBelag(String belag) {
        this.belag = belag;
    }
    public String getLaenge() {
        return laenge;
    }

    public void setLaenge(String laenge) {
        this.laenge = laenge;
    }
    public String getBreite() {
        return breite;
    }

    public void setBreite(String breite) {
        this.breite = breite;
    }
    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }
    public String getTemperatur() {
        return temperatur;
    }

    public void setTemperatur(String temperatur) {
        this.temperatur = temperatur;
    }
    public String getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(String backzeit) {
        this.backzeit = backzeit;
    }

    public Zutaten getZutaten() {
        return zutaten;
    }

    public void setZutaten(Zutaten zutaten) {
        this.zutaten = zutaten;
    }
    public Zutat getZutat() {
        return zutat;
    }

    public void setZutat(Zutat zutat) {
        this.zutat = zutat;
    }

}