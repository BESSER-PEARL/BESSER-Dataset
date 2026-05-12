





import java.util.List;
import java.util.ArrayList;

public class plaetzchen  {

    private String temperatur;
    private String form;
    private String teig;
    private String laenge;
    private String belag;
    private String breite;
    private String backzeit;



    public plaetzchen(
        String temperatur,        String form,        String teig,        String laenge,        String belag,        String breite,        String backzeit    ) {
        this.temperatur = temperatur;
        this.form = form;
        this.teig = teig;
        this.laenge = laenge;
        this.belag = belag;
        this.breite = breite;
        this.backzeit = backzeit;
    }


    public String getTemperatur() {
        return temperatur;
    }

    public void setTemperatur(String temperatur) {
        this.temperatur = temperatur;
    }
    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }
    public String getTeig() {
        return teig;
    }

    public void setTeig(String teig) {
        this.teig = teig;
    }
    public String getLaenge() {
        return laenge;
    }

    public void setLaenge(String laenge) {
        this.laenge = laenge;
    }
    public String getBelag() {
        return belag;
    }

    public void setBelag(String belag) {
        this.belag = belag;
    }
    public String getBreite() {
        return breite;
    }

    public void setBreite(String breite) {
        this.breite = breite;
    }
    public String getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(String backzeit) {
        this.backzeit = backzeit;
    }


}