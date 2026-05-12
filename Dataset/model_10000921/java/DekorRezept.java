





import java.util.List;
import java.util.ArrayList;

public class DekorRezept  {

    private int basismenge;
    private None dekor;
    private None zutaten;
    private None basis;





    private Zutat zutat;




    private GUI gui;


    public DekorRezept(
        int basismenge,        None dekor,        None zutaten,        None basis    ) {
        this.basismenge = basismenge;
        this.dekor = dekor;
        this.zutaten = zutaten;
        this.basis = basis;
    }


    public int getBasismenge() {
        return basismenge;
    }

    public void setBasismenge(int basismenge) {
        this.basismenge = basismenge;
    }
    public None getDekor() {
        return dekor;
    }

    public void setDekor(None dekor) {
        this.dekor = dekor;
    }
    public None getZutaten() {
        return zutaten;
    }

    public void setZutaten(None zutaten) {
        this.zutaten = zutaten;
    }
    public None getBasis() {
        return basis;
    }

    public void setBasis(None basis) {
        this.basis = basis;
    }

    public Zutat getZutat() {
        return zutat;
    }

    public void setZutat(Zutat zutat) {
        this.zutat = zutat;
    }
    public GUI getGui() {
        return gui;
    }

    public void setGui(GUI gui) {
        this.gui = gui;
    }

}