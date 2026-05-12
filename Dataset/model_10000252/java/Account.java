




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate openDate;
    private int id;
    private String billingAddress;



    public Account(
        LocalDate openDate,        int id,        String billingAddress    ) {
        this.openDate = openDate;
        this.id = id;
        this.billingAddress = billingAddress;
    }


    public LocalDate getOpendate() {
        return openDate;
    }

    public void setOpendate(LocalDate openDate) {
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


}