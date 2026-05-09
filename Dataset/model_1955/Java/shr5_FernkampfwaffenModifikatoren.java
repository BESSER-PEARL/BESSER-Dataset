





import java.util.List;
import java.util.ArrayList;

public class shr5_FernkampfwaffenModifikatoren extends ModifikatorAttribute {

    private int sichtverbesserung;
    private boolean schalldaempfer;
    private int vergroesserung;
    private int rueckstoss;
    private String smartgun;
    private boolean lasterPointer;



    public shr5_FernkampfwaffenModifikatoren(
        int sichtverbesserung,        boolean schalldaempfer,        int vergroesserung,        int rueckstoss,        String smartgun,        boolean lasterPointer    ) {
        super(
        );
        this.sichtverbesserung = sichtverbesserung;
        this.schalldaempfer = schalldaempfer;
        this.vergroesserung = vergroesserung;
        this.rueckstoss = rueckstoss;
        this.smartgun = smartgun;
        this.lasterPointer = lasterPointer;
    }


    public int getSichtverbesserung() {
        return sichtverbesserung;
    }

    public void setSichtverbesserung(int sichtverbesserung) {
        this.sichtverbesserung = sichtverbesserung;
    }
    public boolean getSchalldaempfer() {
        return schalldaempfer;
    }

    public void setSchalldaempfer(boolean schalldaempfer) {
        this.schalldaempfer = schalldaempfer;
    }
    public int getVergroesserung() {
        return vergroesserung;
    }

    public void setVergroesserung(int vergroesserung) {
        this.vergroesserung = vergroesserung;
    }
    public int getRueckstoss() {
        return rueckstoss;
    }

    public void setRueckstoss(int rueckstoss) {
        this.rueckstoss = rueckstoss;
    }
    public String getSmartgun() {
        return smartgun;
    }

    public void setSmartgun(String smartgun) {
        this.smartgun = smartgun;
    }
    public boolean getLasterpointer() {
        return lasterPointer;
    }

    public void setLasterpointer(boolean lasterPointer) {
        this.lasterPointer = lasterPointer;
    }


}