




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Hotel_Booking  {

    private LocalDate startDate;
    private LocalDate endDate;
    private boolean checkedIn;
    private float price;
    private int bookingID;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;


    public ClassDiagram_Hotel_Booking(
        LocalDate startDate,        LocalDate endDate,        boolean checkedIn,        float price,        int bookingID    ) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.checkedIn = checkedIn;
        this.price = price;
        this.bookingID = bookingID;
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
    public boolean getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(boolean checkedIn) {
        this.checkedIn = checkedIn;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getBookingid() {
        return bookingID;
    }

    public void setBookingid(int bookingID) {
        this.bookingID = bookingID;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }

}