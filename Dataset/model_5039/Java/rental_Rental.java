




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class rental_Rental  {

    private LocalDate startDate;
    private LocalDate endDate;





    private rental_Customer rental_customer;




    private rental_RentalAgency rental_rentalagency;




    private rental_RentalAgency rental_rentalagency;




    private rental_RentalObject rental_rentalobject;


    public rental_Rental(
        LocalDate startDate,        LocalDate endDate    ) {
        this.startDate = startDate;
        this.endDate = endDate;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public rental_Customer getRental_customer() {
        return rental_customer;
    }

    public void setRental_customer(rental_Customer rental_customer) {
        this.rental_customer = rental_customer;
    }
    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }
    public rental_RentalAgency getRental_rentalagency() {
        return rental_rentalagency;
    }

    public void setRental_rentalagency(rental_RentalAgency rental_rentalagency) {
        this.rental_rentalagency = rental_rentalagency;
    }
    public rental_RentalObject getRental_rentalobject() {
        return rental_rentalobject;
    }

    public void setRental_rentalobject(rental_RentalObject rental_rentalobject) {
        this.rental_rentalobject = rental_rentalobject;
    }

}