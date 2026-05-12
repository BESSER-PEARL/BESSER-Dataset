




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Repair  {

    private LocalDate date;
    private None customer;
    private None part;
    private None car;



    public Repair(
        LocalDate date,        None customer,        None part,        None car    ) {
        this.date = date;
        this.customer = customer;
        this.part = part;
        this.car = car;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }
    public None getPart() {
        return part;
    }

    public void setPart(None part) {
        this.part = part;
    }
    public None getCar() {
        return car;
    }

    public void setCar(None car) {
        this.car = car;
    }


}