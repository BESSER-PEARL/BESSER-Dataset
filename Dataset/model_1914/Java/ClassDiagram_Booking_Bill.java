





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Booking_Bill  {

    private float paidAmount;





    private ClassDiagram_Hotel_Booking classdiagram_hotel_booking;


    public ClassDiagram_Booking_Bill(
        float paidAmount    ) {
        this.paidAmount = paidAmount;
    }


    public float getPaidamount() {
        return paidAmount;
    }

    public void setPaidamount(float paidAmount) {
        this.paidAmount = paidAmount;
    }

    public ClassDiagram_Hotel_Booking getClassdiagram_hotel_booking() {
        return classdiagram_hotel_booking;
    }

    public void setClassdiagram_hotel_booking(ClassDiagram_Hotel_Booking classdiagram_hotel_booking) {
        this.classdiagram_hotel_booking = classdiagram_hotel_booking;
    }

}