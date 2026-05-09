





import java.util.List;
import java.util.ArrayList;

public class shr5_Fokus extends MagischeStufe, Erlernbar {

    private int bindungskosten;



    public shr5_Fokus(
        int bindungskosten    ) {
        super(
        );
        this.bindungskosten = bindungskosten;
    }


    public int getBindungskosten() {
        return bindungskosten;
    }

    public void setBindungskosten(int bindungskosten) {
        this.bindungskosten = bindungskosten;
    }


}