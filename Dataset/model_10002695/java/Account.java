




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate open;
    private String Valid_invalid;





    private ShoppingCart shoppingcart;


    public Account(
        LocalDate open,        String Valid_invalid    ) {
        this.open = open;
        this.Valid_invalid = Valid_invalid;
    }


    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public String getValid_invalid() {
        return Valid_invalid;
    }

    public void setValid_invalid(String Valid_invalid) {
        this.Valid_invalid = Valid_invalid;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}