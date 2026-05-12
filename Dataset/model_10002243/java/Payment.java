





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Amount;





    private System_Order system_order;


    public Payment(
        int Amount    ) {
        this.Amount = Amount;
    }


    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }

    public System_Order getSystem_order() {
        return system_order;
    }

    public void setSystem_order(System_Order system_order) {
        this.system_order = system_order;
    }

}