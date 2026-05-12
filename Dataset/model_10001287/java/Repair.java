




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Repair  {

    private None part;
    private None car;
    private LocalDate date;
    private None customer;



    public Repair(
        None part,        None car,        LocalDate date,        None customer    ) {
        this.part = part;
        this.car = car;
        this.date = date;
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


}