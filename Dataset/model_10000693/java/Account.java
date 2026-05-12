




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int id;
    private LocalDate openDate;
    private String billingAddress;





    private ShoppingCart shoppingcart;


    public Account(
        int id,        LocalDate openDate,        String billingAddress    ) {
        this.id = id;
        this.openDate = openDate;
        this.billingAddress = billingAddress;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getOpendate() {
        return openDate;
    }

    public void setOpendate(LocalDate openDate) {
        this.openDate = openDate;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}