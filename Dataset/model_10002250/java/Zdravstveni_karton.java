





import java.util.List;
import java.util.ArrayList;

public class Zdravstveni_karton  {

    private int BrKart;





    private Pregled pregled;


    public Zdravstveni_karton(
        int BrKart    ) {
        this.BrKart = BrKart;
    }


    public int getBrkart() {
        return BrKart;
    }

    public void setBrkart(int BrKart) {
        this.BrKart = BrKart;
    }

    public Pregled getPregled() {
        return pregled;
    }

    public void setPregled(Pregled pregled) {
        this.pregled = pregled;
    }

}