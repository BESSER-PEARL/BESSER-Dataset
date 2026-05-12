





import java.util.List;
import java.util.ArrayList;

public class delivery  {

    private None password;
    private None name;





    private product product;




    private Payment payment;


    public delivery(
        None password,        None name    ) {
        this.password = password;
        this.name = name;
    }


    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }

    public product getProduct() {
        return product;
    }

    public void setProduct(product product) {
        this.product = product;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}