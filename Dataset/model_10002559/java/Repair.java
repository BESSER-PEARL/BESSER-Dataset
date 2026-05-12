




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Repair  {

    private None car;
    private LocalDate date;
    private None part;
    private None customer;



    public Repair(
        None car,        LocalDate date,        None part,        None customer    ) {
        this.car = car;
        this.date = date;
        this.part = part;
        this.customer = customer;
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
    public None getPart() {
        return part;
    }

    public void setPart(None part) {
        this.part = part;
    }
    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }


}