





import java.util.List;
import java.util.ArrayList;

public class updatePayment  {

    private String paymentInformation;





    private Customer customer;


    public updatePayment(
        String paymentInformation    ) {
        this.paymentInformation = paymentInformation;
    }


    public String getPaymentinformation() {
        return paymentInformation;
    }

    public void setPaymentinformation(String paymentInformation) {
        this.paymentInformation = paymentInformation;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}