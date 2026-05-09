





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Discount  {

    private String name;
    private float amount;
    private String isPercentage;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Discount(
        String name,        float amount,        String isPercentage    ) {
        this.name = name;
        this.amount = amount;
        this.isPercentage = isPercentage;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getIspercentage() {
        return isPercentage;
    }

    public void setIspercentage(String isPercentage) {
        this.isPercentage = isPercentage;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}