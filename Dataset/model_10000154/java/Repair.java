




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Repair  {

    private LocalDate date;
    private None car;
    private None customer;
    private None part;



    public Repair(
        LocalDate date,        None car,        None customer,        None part    ) {
        this.date = date;
        this.car = car;
        this.customer = customer;
        this.part = part;
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


}