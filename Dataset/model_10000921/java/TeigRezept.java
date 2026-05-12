





import java.util.List;
import java.util.ArrayList;

public class TeigRezept  {

    private None zutaten;
    private int backtemp;
    private int backzeit;
    private None basis;
    private int basismenge;





    private GUI gui;




    private Zutat zutat;


    public TeigRezept(
        None zutaten,        int backtemp,        int backzeit,        None basis,        int basismenge    ) {
        this.zutaten = zutaten;
        this.backtemp = backtemp;
        this.backzeit = backzeit;
        this.basis = basis;
        this.basismenge = basismenge;
    }


    public None getZutaten() {
        return zutaten;
    }

    public void setZutaten(None zutaten) {
        this.zutaten = zutaten;
    }
    public int getBacktemp() {
        return backtemp;
    }

    public void setBacktemp(int backtemp) {
        this.backtemp = backtemp;
    }
    public int getBackzeit() {
        return backzeit;
    }

    public void setBackzeit(int backzeit) {
        this.backzeit = backzeit;
    }
    public None getBasis() {
        return basis;
    }

    public void setBasis(None basis) {
        this.basis = basis;
    }
    public int getBasismenge() {
        return basismenge;
    }

    public void setBasismenge(int basismenge) {
        this.basismenge = basismenge;
    }

    public GUI getGui() {
        return gui;
    }

    public void setGui(GUI gui) {
        this.gui = gui;
    }
    public Zutat getZutat() {
        return zutat;
    }

    public void setZutat(Zutat zutat) {
        this.zutat = zutat;
    }

}