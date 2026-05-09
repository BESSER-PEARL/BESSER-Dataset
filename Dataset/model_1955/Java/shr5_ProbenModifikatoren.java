





import java.util.List;
import java.util.ArrayList;

public class shr5_ProbenModifikatoren extends ModifikatorAttribute {

    private int heilung;
    private int schadenswiederstand;



    public shr5_ProbenModifikatoren(
        int heilung,        int schadenswiederstand    ) {
        super(
        );
        this.heilung = heilung;
        this.schadenswiederstand = schadenswiederstand;
    }


    public int getHeilung() {
        return heilung;
    }

    public void setHeilung(int heilung) {
        this.heilung = heilung;
    }
    public int getSchadenswiederstand() {
        return schadenswiederstand;
    }

    public void setSchadenswiederstand(int schadenswiederstand) {
        this.schadenswiederstand = schadenswiederstand;
    }


}