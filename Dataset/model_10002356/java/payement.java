





import java.util.List;
import java.util.ArrayList;

public class payement  {

    private int pay_date;
    private int pay_amt;
    private int transc_id;
    private String paymethod;
    private String customer_info;





    private customer customer;


    public payement(
        int pay_date,        int pay_amt,        int transc_id,        String paymethod,        String customer_info    ) {
        this.pay_date = pay_date;
        this.pay_amt = pay_amt;
        this.transc_id = transc_id;
        this.paymethod = paymethod;
        this.customer_info = customer_info;
    }


    public int getPay_date() {
        return pay_date;
    }

    public void setPay_date(int pay_date) {
        this.pay_date = pay_date;
    }
    public int getPay_amt() {
        return pay_amt;
    }

    public void setPay_amt(int pay_amt) {
        this.pay_amt = pay_amt;
    }
    public int getTransc_id() {
        return transc_id;
    }

    public void setTransc_id(int transc_id) {
        this.transc_id = transc_id;
    }
    public String getPaymethod() {
        return paymethod;
    }

    public void setPaymethod(String paymethod) {
        this.paymethod = paymethod;
    }
    public String getCustomer_info() {
        return customer_info;
    }

    public void setCustomer_info(String customer_info) {
        this.customer_info = customer_info;
    }

    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }

}