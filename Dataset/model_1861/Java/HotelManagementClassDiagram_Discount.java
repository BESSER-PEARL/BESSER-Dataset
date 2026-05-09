





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Discount  {

    private String isPercentage;
    private float amount;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Discount(
        String isPercentage,        float amount    ) {
        this.isPercentage = isPercentage;
        this.amount = amount;
    }


    public String getIspercentage() {
        return isPercentage;
    }

    public void setIspercentage(String isPercentage) {
        this.isPercentage = isPercentage;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}