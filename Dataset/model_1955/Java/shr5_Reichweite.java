





import java.util.List;
import java.util.ArrayList;

public class shr5_Reichweite extends Beschreibbar, Identifiable {

    private int weit;
    private int mittel;
    private int min;
    private int extrem;
    private int kurz;





    private shr5_Munition shr5_munition;


    public shr5_Reichweite(
        int weit,        int mittel,        int min,        int extrem,        int kurz    ) {
        super(
        );
        this.weit = weit;
        this.mittel = mittel;
        this.min = min;
        this.extrem = extrem;
        this.kurz = kurz;
    }


    public int getWeit() {
        return weit;
    }

    public void setWeit(int weit) {
        this.weit = weit;
    }
    public int getMittel() {
        return mittel;
    }

    public void setMittel(int mittel) {
        this.mittel = mittel;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getExtrem() {
        return extrem;
    }

    public void setExtrem(int extrem) {
        this.extrem = extrem;
    }
    public int getKurz() {
        return kurz;
    }

    public void setKurz(int kurz) {
        this.kurz = kurz;
    }

    public shr5_Munition getShr5_munition() {
        return shr5_munition;
    }

    public void setShr5_munition(shr5_Munition shr5_munition) {
        this.shr5_munition = shr5_munition;
    }

}