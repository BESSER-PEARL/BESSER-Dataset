





import java.util.List;
import java.util.ArrayList;

public class teigmaschine  {

    private None blechgroesse;
    private String anzPlaetzchenLetzesBlech;
    private String anzBleche;
    private None anzBlechePlaetzchen;
    private String abstand;





    private auftrag auftrag;




    private groesse groesse;


    public teigmaschine(
        None blechgroesse,        String anzPlaetzchenLetzesBlech,        String anzBleche,        None anzBlechePlaetzchen,        String abstand    ) {
        this.blechgroesse = blechgroesse;
        this.anzPlaetzchenLetzesBlech = anzPlaetzchenLetzesBlech;
        this.anzBleche = anzBleche;
        this.anzBlechePlaetzchen = anzBlechePlaetzchen;
        this.abstand = abstand;
    }


    public None getBlechgroesse() {
        return blechgroesse;
    }

    public void setBlechgroesse(None blechgroesse) {
        this.blechgroesse = blechgroesse;
    }
    public String getAnzplaetzchenletzesblech() {
        return anzPlaetzchenLetzesBlech;
    }

    public void setAnzplaetzchenletzesblech(String anzPlaetzchenLetzesBlech) {
        this.anzPlaetzchenLetzesBlech = anzPlaetzchenLetzesBlech;
    }
    public String getAnzbleche() {
        return anzBleche;
    }

    public void setAnzbleche(String anzBleche) {
        this.anzBleche = anzBleche;
    }
    public None getAnzblecheplaetzchen() {
        return anzBlechePlaetzchen;
    }

    public void setAnzblecheplaetzchen(None anzBlechePlaetzchen) {
        this.anzBlechePlaetzchen = anzBlechePlaetzchen;
    }
    public String getAbstand() {
        return abstand;
    }

    public void setAbstand(String abstand) {
        this.abstand = abstand;
    }

    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }
    public groesse getGroesse() {
        return groesse;
    }

    public void setGroesse(groesse groesse) {
        this.groesse = groesse;
    }

}