




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Booking_BookedService  {

    private LocalDate date;





    private ClassDiagram_Hotel_Booking classdiagram_hotel_booking;


    public ClassDiagram_Booking_BookedService(
        LocalDate date    ) {
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public ClassDiagram_Hotel_Booking getClassdiagram_hotel_booking() {
        return classdiagram_hotel_booking;
    }

    public void setClassdiagram_hotel_booking(ClassDiagram_Hotel_Booking classdiagram_hotel_booking) {
        this.classdiagram_hotel_booking = classdiagram_hotel_booking;
    }

}