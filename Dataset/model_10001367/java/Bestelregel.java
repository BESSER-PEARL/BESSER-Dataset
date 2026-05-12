





import java.util.List;
import java.util.ArrayList;

public class Bestelregel  {

    private int aantal;





    private Factuur factuur;


    public Bestelregel(
        int aantal    ) {
        this.aantal = aantal;
    }


    public int getAantal() {
        return aantal;
    }

    public void setAantal(int aantal) {
        this.aantal = aantal;
    }

    public Factuur getFactuur() {
        return factuur;
    }

    public void setFactuur(Factuur factuur) {
        this.factuur = factuur;
    }

}