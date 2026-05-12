





import java.util.List;
import java.util.ArrayList;

public class PlaetzchenAnzeigeForm  {

    private String form;
    private String laenge;
    private String breite;





    private PlaetzchenDesignerForm plaetzchendesignerform;


    public PlaetzchenAnzeigeForm(
        String form,        String laenge,        String breite    ) {
        this.form = form;
        this.laenge = laenge;
        this.breite = breite;
    }


    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
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

    public PlaetzchenDesignerForm getPlaetzchendesignerform() {
        return plaetzchendesignerform;
    }

    public void setPlaetzchendesignerform(PlaetzchenDesignerForm plaetzchendesignerform) {
        this.plaetzchendesignerform = plaetzchendesignerform;
    }

}