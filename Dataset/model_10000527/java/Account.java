




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate open;
    private String billingAddress;
    private boolean isClosed;
    private LocalDate closed;





    private ShoppingCart shoppingcart;


    public Account(
        LocalDate open,        String billingAddress,        boolean isClosed,        LocalDate closed    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.closed = closed;
    }


    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}