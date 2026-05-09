





import java.util.List;
import java.util.ArrayList;

public class shadowrun_BerechneteAttribute  {

    private int ReaktionW;
    private int Reaktion;
    private int Kampfpool;



    public shadowrun_BerechneteAttribute(
        int ReaktionW,        int Reaktion,        int Kampfpool    ) {
        this.ReaktionW = ReaktionW;
        this.Reaktion = Reaktion;
        this.Kampfpool = Kampfpool;
    }


    public int getReaktionw() {
        return ReaktionW;
    }

    public void setReaktionw(int ReaktionW) {
        this.ReaktionW = ReaktionW;
    }
    public int getReaktion() {
        return Reaktion;
    }

    public void setReaktion(int Reaktion) {
        this.Reaktion = Reaktion;
    }
    public int getKampfpool() {
        return Kampfpool;
    }

    public void setKampfpool(int Kampfpool) {
        this.Kampfpool = Kampfpool;
    }


}