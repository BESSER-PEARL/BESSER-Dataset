





import java.util.List;
import java.util.ArrayList;

public class Discription  {

    private String Discription;
    private String Email;





    private Order order;


    public Discription(
        String Discription,        String Email    ) {
        this.Discription = Discription;
        this.Email = Email;
    }


    public String getDiscription() {
        return Discription;
    }

    public void setDiscription(String Discription) {
        this.Discription = Discription;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}