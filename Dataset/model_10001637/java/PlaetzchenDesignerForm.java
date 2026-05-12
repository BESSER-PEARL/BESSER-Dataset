





import java.util.List;
import java.util.ArrayList;

public class PlaetzchenDesignerForm  {

    private String BLECHBREITE;
    private String BLECHLAENGE;
    private String neuerAuftrag;
    private boolean plaetzchenGeaendert;
    private String neuesPlaetzchen;
    private String datei;





    private Plaetzchen plaetzchen;


    public PlaetzchenDesignerForm(
        String BLECHBREITE,        String BLECHLAENGE,        String neuerAuftrag,        boolean plaetzchenGeaendert,        String neuesPlaetzchen,        String datei    ) {
        this.BLECHBREITE = BLECHBREITE;
        this.BLECHLAENGE = BLECHLAENGE;
        this.neuerAuftrag = neuerAuftrag;
        this.plaetzchenGeaendert = plaetzchenGeaendert;
        this.neuesPlaetzchen = neuesPlaetzchen;
        this.datei = datei;
    }


    public String getBlechbreite() {
        return BLECHBREITE;
    }

    public void setBlechbreite(String BLECHBREITE) {
        this.BLECHBREITE = BLECHBREITE;
    }
    public String getBlechlaenge() {
        return BLECHLAENGE;
    }

    public void setBlechlaenge(String BLECHLAENGE) {
        this.BLECHLAENGE = BLECHLAENGE;
    }
    public String getNeuerauftrag() {
        return neuerAuftrag;
    }

    public void setNeuerauftrag(String neuerAuftrag) {
        this.neuerAuftrag = neuerAuftrag;
    }
    public boolean getPlaetzchengeaendert() {
        return plaetzchenGeaendert;
    }

    public void setPlaetzchengeaendert(boolean plaetzchenGeaendert) {
        this.plaetzchenGeaendert = plaetzchenGeaendert;
    }
    public String getNeuesplaetzchen() {
        return neuesPlaetzchen;
    }

    public void setNeuesplaetzchen(String neuesPlaetzchen) {
        this.neuesPlaetzchen = neuesPlaetzchen;
    }
    public String getDatei() {
        return datei;
    }

    public void setDatei(String datei) {
        this.datei = datei;
    }

    public Plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(Plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }

}