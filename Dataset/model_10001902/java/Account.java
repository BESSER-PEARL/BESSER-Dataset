




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate closed;
    private LocalDate open;
    private boolean isClosed;
    private String billingAddress;



    public Account(
        LocalDate closed,        LocalDate open,        boolean isClosed,        String billingAddress    ) {
        this.closed = closed;
        this.open = open;
        this.isClosed = isClosed;
        this.billingAddress = billingAddress;
    }


    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }


}