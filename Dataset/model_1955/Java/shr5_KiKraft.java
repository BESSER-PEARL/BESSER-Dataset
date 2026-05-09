





import java.util.List;
import java.util.ArrayList;

public class shr5_KiKraft extends MagischeMods, Erlernbar {

    private int kraftpunkte;





    private shr5_QiFokus shr5_qifokus;


    public shr5_KiKraft(
        int kraftpunkte    ) {
        super(
        );
        this.kraftpunkte = kraftpunkte;
    }


    public int getKraftpunkte() {
        return kraftpunkte;
    }

    public void setKraftpunkte(int kraftpunkte) {
        this.kraftpunkte = kraftpunkte;
    }

    public shr5_QiFokus getShr5_qifokus() {
        return shr5_qifokus;
    }

    public void setShr5_qifokus(shr5_QiFokus shr5_qifokus) {
        this.shr5_qifokus = shr5_qifokus;
    }

}