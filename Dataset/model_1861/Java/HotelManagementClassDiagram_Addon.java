





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Addon  {

    private String name;
    private String description;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Addon(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}