




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CardInfo  {

    private int CVV;
    private int ID;
    private String name;
    private int number;
    private LocalDate expiryDate;
    private String billingAddress;



    public CardInfo(
        int CVV,        int ID,        String name,        int number,        LocalDate expiryDate,        String billingAddress    ) {
        this.CVV = CVV;
        this.ID = ID;
        this.name = name;
        this.number = number;
        this.expiryDate = expiryDate;
        this.billingAddress = billingAddress;
    }


    public int getCvv() {
        return CVV;
    }

    public void setCvv(int CVV) {
        this.CVV = CVV;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public LocalDate getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(LocalDate expiryDate) {
        this.expiryDate = expiryDate;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }


}