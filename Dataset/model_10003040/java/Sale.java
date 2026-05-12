




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Sale  {

    private None customer;
    private String billable;
    private LocalDate date;
    private None car;



    public Sale(
        None customer,        String billable,        LocalDate date,        None car    ) {
        this.customer = customer;
        this.billable = billable;
        this.date = date;
        this.car = car;
    }


    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }
    public String getBillable() {
        return billable;
    }

    public void setBillable(String billable) {
        this.billable = billable;
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