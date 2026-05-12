




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Sale  {

    private None customer;
    private None car;
    private String billable;
    private LocalDate date;



    public Sale(
        None customer,        None car,        String billable,        LocalDate date    ) {
        this.customer = customer;
        this.car = car;
        this.billable = billable;
        this.date = date;
    }


    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }
    public None getCar() {
        return car;
    }

    public void setCar(None car) {
        this.car = car;
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


}