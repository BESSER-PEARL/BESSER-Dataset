




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tda593_booking_Booking  {

    private String specialRequest;
    private LocalDate startDate;
    private LocalDate endDate;
    private float price;
    private boolean isCanceled;
    private int id;





    private booking_LegalEntity booking_legalentity;




    private facilities_RoomType facilities_roomtype;




    private booking_RoomStay booking_roomstay;


    public tda593_booking_Booking(
        String specialRequest,        LocalDate startDate,        LocalDate endDate,        float price,        boolean isCanceled,        int id    ) {
        this.specialRequest = specialRequest;
        this.startDate = startDate;
        this.endDate = endDate;
        this.price = price;
        this.isCanceled = isCanceled;
        this.id = id;
    }


    public String getSpecialrequest() {
        return specialRequest;
    }

    public void setSpecialrequest(String specialRequest) {
        this.specialRequest = specialRequest;
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
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public boolean getIscanceled() {
        return isCanceled;
    }

    public void setIscanceled(boolean isCanceled) {
        this.isCanceled = isCanceled;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public booking_LegalEntity getBooking_legalentity() {
        return booking_legalentity;
    }

    public void setBooking_legalentity(booking_LegalEntity booking_legalentity) {
        this.booking_legalentity = booking_legalentity;
    }
    public facilities_RoomType getFacilities_roomtype() {
        return facilities_roomtype;
    }

    public void setFacilities_roomtype(facilities_RoomType facilities_roomtype) {
        this.facilities_roomtype = facilities_roomtype;
    }
    public booking_RoomStay getBooking_roomstay() {
        return booking_roomstay;
    }

    public void setBooking_roomstay(booking_RoomStay booking_roomstay) {
        this.booking_roomstay = booking_roomstay;
    }

}