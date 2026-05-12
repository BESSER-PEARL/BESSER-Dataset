





import java.util.List;
import java.util.ArrayList;

public class IncomeTax  {

    private float taxRate;





    private Board1 board1;


    public IncomeTax(
        float taxRate    ) {
        this.taxRate = taxRate;
    }


    public float getTaxrate() {
        return taxRate;
    }

    public void setTaxrate(float taxRate) {
        this.taxRate = taxRate;
    }

    public Board1 getBoard1() {
        return board1;
    }

    public void setBoard1(Board1 board1) {
        this.board1 = board1;
    }

}