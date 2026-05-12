




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private LocalDate Update_cart;



    public ShoppingCart(
        LocalDate Update_cart    ) {
        this.Update_cart = Update_cart;
    }


    public LocalDate getUpdate_cart() {
        return Update_cart;
    }

    public void setUpdate_cart(LocalDate Update_cart) {
        this.Update_cart = Update_cart;
    }


}