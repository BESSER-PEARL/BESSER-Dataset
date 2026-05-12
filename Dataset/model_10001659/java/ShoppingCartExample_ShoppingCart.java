




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_ShoppingCart  {

    private LocalDate creationDate;





    private ShoppingCartExample_Account shoppingcartexample_account;


    public ShoppingCartExample_ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public ShoppingCartExample_Account getShoppingcartexample_account() {
        return shoppingcartexample_account;
    }

    public void setShoppingcartexample_account(ShoppingCartExample_Account shoppingcartexample_account) {
        this.shoppingcartexample_account = shoppingcartexample_account;
    }

}