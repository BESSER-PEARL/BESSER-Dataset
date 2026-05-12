




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Sale  {

    private None customer;
    private LocalDate date;
    private String billable;
    private None car;



    public Sale(
        None customer,        LocalDate date,        String billable,        None car    ) {
        this.customer = customer;
        this.date = date;
        this.billable = billable;
        this.car = car;
    }


    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getBillable() {
        return billable;
    }

    public void setBillable(String billable) {
        this.billable = billable;
    }
    public None getCar() {
        return car;
    }

    public void setCar(None car) {
        this.car = car;
    }


}