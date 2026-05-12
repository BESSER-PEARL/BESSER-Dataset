




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int id;
    private String billingAddress;
    private LocalDate openDate;





    private ShoppingBAsket shoppingbasket;


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

    public ShoppingBAsket getShoppingbasket() {
        return shoppingbasket;
    }

    public void setShoppingbasket(ShoppingBAsket shoppingbasket) {
        this.shoppingbasket = shoppingbasket;
    }

}