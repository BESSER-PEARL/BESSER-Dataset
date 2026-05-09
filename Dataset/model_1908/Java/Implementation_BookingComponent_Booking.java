




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_Booking  {

    private String isActive;
    private String bookingReference;
    private String currentCost;
    private String isPaid;
    private LocalDate arrivalDate;
    private LocalDate departureDate;





    private Implementation_BookingComponent_PaymentDetails implementation_bookingcomponent_paymentdetails;


    public Implementation_BookingComponent_Booking(
        String isActive,        String bookingReference,        String currentCost,        String isPaid,        LocalDate arrivalDate,        LocalDate departureDate    ) {
        this.isActive = isActive;
        this.bookingReference = bookingReference;
        this.currentCost = currentCost;
        this.isPaid = isPaid;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }


    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }
    public String getBookingreference() {
        return bookingReference;
    }

    public void setBookingreference(String bookingReference) {
        this.bookingReference = bookingReference;
    }
    public String getCurrentcost() {
        return currentCost;
    }

    public void setCurrentcost(String currentCost) {
        this.currentCost = currentCost;
    }
    public String getIspaid() {
        return isPaid;
    }

    public void setIspaid(String isPaid) {
        this.isPaid = isPaid;
    }
    public LocalDate getArrivaldate() {
        return arrivalDate;
    }

    public void setArrivaldate(LocalDate arrivalDate) {
        this.arrivalDate = arrivalDate;
    }
    public LocalDate getDeparturedate() {
        return departureDate;
    }

    public void setDeparturedate(LocalDate departureDate) {
        this.departureDate = departureDate;
    }

    public Implementation_BookingComponent_PaymentDetails getImplementation_bookingcomponent_paymentdetails() {
        return implementation_bookingcomponent_paymentdetails;
    }

    public void setImplementation_bookingcomponent_paymentdetails(Implementation_BookingComponent_PaymentDetails implementation_bookingcomponent_paymentdetails) {
        this.implementation_bookingcomponent_paymentdetails = implementation_bookingcomponent_paymentdetails;
    }

}