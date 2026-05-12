




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int id;
    private String billingAddress;
    private LocalDate openDate;





    private ShoppingCart shoppingcart;


    public Account(
        int id,        String billingAddress,        LocalDate openDate    ) {
        this.id = id;
        this.billingAddress = billingAddress;
        this.openDate = openDate;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }
    public LocalDate getOpendate() {
        return openDate;
    }

    public void setOpendate(LocalDate openDate) {
        this.openDate = openDate;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}