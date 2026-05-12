




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Repair  {

    private None car;
    private None customer;
    private LocalDate date;
    private None part;



    public Repair(
        None car,        None customer,        LocalDate date,        None part    ) {
        this.car = car;
        this.customer = customer;
        this.date = date;
        this.part = part;
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


}