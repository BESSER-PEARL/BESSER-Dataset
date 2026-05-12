




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private boolean isClosed;
    private LocalDate open;
    private LocalDate closed;
    private String billingAddress;



    public Account(
        boolean isClosed,        LocalDate open,        LocalDate closed,        String billingAddress    ) {
        this.isClosed = isClosed;
        this.open = open;
        this.closed = closed;
        this.billingAddress = billingAddress;
    }


    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }


}