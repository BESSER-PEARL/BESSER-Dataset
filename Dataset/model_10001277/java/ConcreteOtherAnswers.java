




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ConcreteOtherAnswers  {

    private boolean isClosed;
    private LocalDate open;
    private String billingAddress;
    private LocalDate closed;



    public ConcreteOtherAnswers(
        boolean isClosed,        LocalDate open,        String billingAddress,        LocalDate closed    ) {
        this.isClosed = isClosed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.closed = closed;
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
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }


}