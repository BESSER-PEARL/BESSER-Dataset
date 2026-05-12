





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Amount;
    private String Payment_Option;





    private List<System_order> system_orders;


    public Payment(
        int Amount,        String Payment_Option    ) {
        this.Amount = Amount;
        this.Payment_Option = Payment_Option;
        this.system_orders = new ArrayList<>();
    }

    public Payment(
        int Amount,        String Payment_Option        ArrayList<System_order> system_orders    ) {
        this.Amount = Amount;
        this.Payment_Option = Payment_Option;
        this.system_orders = system_orders;
    }

    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }
    public String getPayment_option() {
        return Payment_Option;
    }

    public void setPayment_option(String Payment_Option) {
        this.Payment_Option = Payment_Option;
    }

    public List<System_order> getSystem_orders() {
        return system_orders;
    }

    public void addSystem_order(System_order system_order) {
        this.system_orders.add(system_order);
    }

}