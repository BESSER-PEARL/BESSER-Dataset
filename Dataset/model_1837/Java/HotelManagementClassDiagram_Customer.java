





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Customer extends Person {

    private int customerID;
    private int bonusPoints;
    private String miscInfo;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Customer(
        int customerID,        int bonusPoints,        String miscInfo    ) {
        super(
        );
        this.customerID = customerID;
        this.bonusPoints = bonusPoints;
        this.miscInfo = miscInfo;
    }


    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }
    public int getBonuspoints() {
        return bonusPoints;
    }

    public void setBonuspoints(int bonusPoints) {
        this.bonusPoints = bonusPoints;
    }
    public String getMiscinfo() {
        return miscInfo;
    }

    public void setMiscinfo(String miscInfo) {
        this.miscInfo = miscInfo;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}