




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private LocalDate openDate;
    private String billingAddress;
    private int id;



    public Account(
        LocalDate openDate,        String billingAddress,        int id    ) {
        this.openDate = openDate;
        this.billingAddress = billingAddress;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}