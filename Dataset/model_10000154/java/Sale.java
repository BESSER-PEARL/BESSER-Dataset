




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Sale  {

    private String billable;
    private None customer;
    private LocalDate date;
    private None car;



    public Sale(
        String billable,        None customer,        LocalDate date,        None car    ) {
        this.billable = billable;
        this.customer = customer;
        this.date = date;
        this.car = car;
    }


    public String getBillable() {
        return billable;
    }

    public void setBillable(String billable) {
        this.billable = billable;
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
    public None getCar() {
        return car;
    }

    public void setCar(None car) {
        this.car = car;
    }


}