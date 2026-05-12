





import java.util.List;
import java.util.ArrayList;

public class billdesk_Interface  {






    private payment_Interface payment_interface;


    public billdesk_Interface(
    ) {
    }



    public payment_Interface getPayment_interface() {
        return payment_interface;
    }

    public void setPayment_interface(payment_Interface payment_interface) {
        this.payment_interface = payment_interface;
    }

}