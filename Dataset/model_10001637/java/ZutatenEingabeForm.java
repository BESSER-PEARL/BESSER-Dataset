





import java.util.List;
import java.util.ArrayList;

public class ZutatenEingabeForm  {

    private String neueZutat;





    private PlaetzchenDesignerForm plaetzchendesignerform;




    private Zutat zutat;


    public ZutatenEingabeForm(
        String neueZutat    ) {
        this.neueZutat = neueZutat;
    }


    public String getNeuezutat() {
        return neueZutat;
    }

    public void setNeuezutat(String neueZutat) {
        this.neueZutat = neueZutat;
    }

    public PlaetzchenDesignerForm getPlaetzchendesignerform() {
        return plaetzchendesignerform;
    }

    public void setPlaetzchendesignerform(PlaetzchenDesignerForm plaetzchendesignerform) {
        this.plaetzchendesignerform = plaetzchendesignerform;
    }
    public Zutat getZutat() {
        return zutat;
    }

    public void setZutat(Zutat zutat) {
        this.zutat = zutat;
    }

}