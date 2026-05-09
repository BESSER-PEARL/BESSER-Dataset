





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Bill  {

    private boolean final;
    private float totalPrice;
    private boolean paid;





    private HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer;




    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Bill(
        boolean final,        float totalPrice,        boolean paid    ) {
        this.final = final;
        this.totalPrice = totalPrice;
        this.paid = paid;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public float getTotalprice() {
        return totalPrice;
    }

    public void setTotalprice(float totalPrice) {
        this.totalPrice = totalPrice;
    }
    public boolean getPaid() {
        return paid;
    }

    public void setPaid(boolean paid) {
        this.paid = paid;
    }

    public HotelManagementClassDiagram_Customer getHotelmanagementclassdiagram_customer() {
        return hotelmanagementclassdiagram_customer;
    }

    public void setHotelmanagementclassdiagram_customer(HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer) {
        this.hotelmanagementclassdiagram_customer = hotelmanagementclassdiagram_customer;
    }
    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}