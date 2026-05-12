





import java.util.List;
import java.util.ArrayList;

public class GussRezept  {

    private None basis;
    private None zutat;
    private int basismenge;



    public GussRezept(
        None basis,        None zutat,        int basismenge    ) {
        this.basis = basis;
        this.zutat = zutat;
        this.basismenge = basismenge;
    }


    public None getBasis() {
        return basis;
    }

    public void setBasis(None basis) {
        this.basis = basis;
    }
    public None getZutat() {
        return zutat;
    }

    public void setZutat(None zutat) {
        this.zutat = zutat;
    }
    public int getBasismenge() {
        return basismenge;
    }

    public void setBasismenge(int basismenge) {
        this.basismenge = basismenge;
    }


}