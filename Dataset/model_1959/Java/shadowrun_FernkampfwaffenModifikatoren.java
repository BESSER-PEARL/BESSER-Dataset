





import java.util.List;
import java.util.ArrayList;

public class shadowrun_FernkampfwaffenModifikatoren  {

    private boolean Schalldaempfer;
    private String Smartgun;
    private int Vergroesserung;
    private boolean lasterPointer;
    private int Rueckstoss;



    public shadowrun_FernkampfwaffenModifikatoren(
        boolean Schalldaempfer,        String Smartgun,        int Vergroesserung,        boolean lasterPointer,        int Rueckstoss    ) {
        this.Schalldaempfer = Schalldaempfer;
        this.Smartgun = Smartgun;
        this.Vergroesserung = Vergroesserung;
        this.lasterPointer = lasterPointer;
        this.Rueckstoss = Rueckstoss;
    }


    public boolean getSchalldaempfer() {
        return Schalldaempfer;
    }

    public void setSchalldaempfer(boolean Schalldaempfer) {
        this.Schalldaempfer = Schalldaempfer;
    }
    public String getSmartgun() {
        return Smartgun;
    }

    public void setSmartgun(String Smartgun) {
        this.Smartgun = Smartgun;
    }
    public int getVergroesserung() {
        return Vergroesserung;
    }

    public void setVergroesserung(int Vergroesserung) {
        this.Vergroesserung = Vergroesserung;
    }
    public boolean getLasterpointer() {
        return lasterPointer;
    }

    public void setLasterpointer(boolean lasterPointer) {
        this.lasterPointer = lasterPointer;
    }
    public int getRueckstoss() {
        return Rueckstoss;
    }

    public void setRueckstoss(int Rueckstoss) {
        this.Rueckstoss = Rueckstoss;
    }


}