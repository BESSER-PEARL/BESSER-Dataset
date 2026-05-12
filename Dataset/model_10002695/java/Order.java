





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Items;
    private String number;





    private Payment payment;




    private Account account;


    public Order(
        String Items,        String number    ) {
        this.Items = Items;
        this.number = number;
    }


    public String getItems() {
        return Items;
    }

    public void setItems(String Items) {
        this.Items = Items;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}