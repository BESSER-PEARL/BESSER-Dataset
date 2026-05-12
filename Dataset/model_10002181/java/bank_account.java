





import java.util.List;
import java.util.ArrayList;

public class bank_account  {






    private System1 system1;




    private List<Payment1> payment1s;




    private System1 system1;


    public bank_account(
    ) {
        this.payment1s = new ArrayList<>();
    }

    public bank_account(
        ArrayList<Payment1> payment1s    ) {
        this.payment1s = payment1s;
    }


    public System1 getSystem1() {
        return system1;
    }

    public void setSystem1(System1 system1) {
        this.system1 = system1;
    }
    public List<Payment1> getPayment1s() {
        return payment1s;
    }

    public void addPayment1(Payment1 payment1) {
        this.payment1s.add(payment1);
    }
    public System1 getSystem1() {
        return system1;
    }

    public void setSystem1(System1 system1) {
        this.system1 = system1;
    }

}