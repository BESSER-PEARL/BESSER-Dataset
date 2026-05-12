





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String toppings;
    private String Quantity;





    private Online_pizza_ordering online_pizza_ordering;


    public Menu(
        String toppings,        String Quantity    ) {
        this.toppings = toppings;
        this.Quantity = Quantity;
    }


    public String getToppings() {
        return toppings;
    }

    public void setToppings(String toppings) {
        this.toppings = toppings;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }

    public Online_pizza_ordering getOnline_pizza_ordering() {
        return online_pizza_ordering;
    }

    public void setOnline_pizza_ordering(Online_pizza_ordering online_pizza_ordering) {
        this.online_pizza_ordering = online_pizza_ordering;
    }

}