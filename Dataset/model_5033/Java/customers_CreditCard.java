




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class customers_CreditCard  {

    private String type;
    private String ccNumber;
    private LocalDate expiresDate;





    private customers_Customer customers_customer;




    private customers_Customer customers_customer;


    public customers_CreditCard(
        String type,        String ccNumber,        LocalDate expiresDate    ) {
        this.type = type;
        this.ccNumber = ccNumber;
        this.expiresDate = expiresDate;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCcnumber() {
        return ccNumber;
    }

    public void setCcnumber(String ccNumber) {
        this.ccNumber = ccNumber;
    }
    public LocalDate getExpiresdate() {
        return expiresDate;
    }

    public void setExpiresdate(LocalDate expiresDate) {
        this.expiresDate = expiresDate;
    }

    public customers_Customer getCustomers_customer() {
        return customers_customer;
    }

    public void setCustomers_customer(customers_Customer customers_customer) {
        this.customers_customer = customers_customer;
    }
    public customers_Customer getCustomers_customer() {
        return customers_customer;
    }

    public void setCustomers_customer(customers_Customer customers_customer) {
        this.customers_customer = customers_customer;
    }

}