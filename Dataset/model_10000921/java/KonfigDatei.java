





import java.util.List;
import java.util.ArrayList;

public class KonfigDatei  {

    private int menge1;
    private String attribute;
    private None name;
    private None plaetzchen;
    private int backtemp;
    private String attribute2;
    private int backzeit;
    private int menge;





    private GUI gui;


    public KonfigDatei(
        int menge1,        String attribute,        None name,        None plaetzchen,        int backtemp,        String attribute2,        int backzeit,        int menge    ) {
        this.menge1 = menge1;
        this.attribute = attribute;
        this.name = name;
        this.plaetzchen = plaetzchen;
        this.backtemp = backtemp;
        this.attribute2 = attribute2;
        this.backzeit = backzeit;
        this.menge = menge;
    }


    public int getMenge1() {
        return menge1;
    }

    public void setMenge1(int menge1) {
        this.menge1 = menge1;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public None getPlaetzchen() {
        return plaetzchen;
    }

    public void setPlaetzchen(None plaetzchen) {
        this.plaetzchen = plaetzchen;
    }
    public int getBacktemp() {
        return backtemp;
    }

    public void setBacktemp(int backtemp) {
        this.backtemp = backtemp;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public int getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(int backzeit) {
        this.backzeit = backzeit;
    }
    public int getMenge() {
        return menge;
    }

    public void setMenge(int menge) {
        this.menge = menge;
    }

    public GUI getGui() {
        return gui;
    }

    public void setGui(GUI gui) {
        this.gui = gui;
    }

}