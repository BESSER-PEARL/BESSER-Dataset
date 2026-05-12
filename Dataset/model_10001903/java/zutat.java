





import java.util.List;
import java.util.ArrayList;

public class zutat  {

    private String einheit;
    private String name;
    private String menge;





    private plaetzchen plaetzchen;




    private teig teig;




    private auftrag auftrag;




    private lager lager;


    public zutat(
        String einheit,        String name,        String menge    ) {
        this.einheit = einheit;
        this.name = name;
        this.menge = menge;
    }


    public String getEinheit() {
        return einheit;
    }

    public void setEinheit(String einheit) {
        this.einheit = einheit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMenge() {
        return menge;
    }

    public void setMenge(String menge) {
        this.menge = menge;
    }

    public plaetzchen getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(plaetzchen plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public teig getTeig() {
        return teig;
    }

    public void setTeig(teig teig) {
        this.teig = teig;
    }
    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }
    public lager getLager() {
        return lager;
    }

    public void setLager(lager lager) {
        this.lager = lager;
    }

}