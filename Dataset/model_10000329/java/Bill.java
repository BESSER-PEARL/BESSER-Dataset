





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private int Tax;
    private int Tip;
    private int TotalAmount;





    private Waiter waiter;


    public Bill(
        int Tax,        int Tip,        int TotalAmount    ) {
        this.Tax = Tax;
        this.Tip = Tip;
        this.TotalAmount = TotalAmount;
    }


    public int getTax() {
        return Tax;
    }

    public void setTax(int Tax) {
        this.Tax = Tax;
    }
    public int getTip() {
        return Tip;
    }

    public void setTip(int Tip) {
        this.Tip = Tip;
    }
    public int getTotalamount() {
        return TotalAmount;
    }

    public void setTotalamount(int TotalAmount) {
        this.TotalAmount = TotalAmount;
    }

    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}