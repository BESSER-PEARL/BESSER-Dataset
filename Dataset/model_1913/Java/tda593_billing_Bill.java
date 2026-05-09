




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tda593_billing_Bill  {

    private boolean isPaid;
    private LocalDate date;
    private int id;
    private boolean isPublished;





    private booking_LegalEntity booking_legalentity;


    public tda593_billing_Bill(
        boolean isPaid,        LocalDate date,        int id,        boolean isPublished    ) {
        this.isPaid = isPaid;
        this.date = date;
        this.id = id;
        this.isPublished = isPublished;
    }


    public boolean getIspaid() {
        return isPaid;
    }

    public void setIspaid(boolean isPaid) {
        this.isPaid = isPaid;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getIspublished() {
        return isPublished;
    }

    public void setIspublished(boolean isPublished) {
        this.isPublished = isPublished;
    }

    public booking_LegalEntity getBooking_legalentity() {
        return booking_legalentity;
    }

    public void setBooking_legalentity(booking_LegalEntity booking_legalentity) {
        this.booking_legalentity = booking_legalentity;
    }

}