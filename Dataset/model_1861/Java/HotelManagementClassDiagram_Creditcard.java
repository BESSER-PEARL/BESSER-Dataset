





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Creditcard  {

    private String number;
    private String owner;
    private int cvc;
    private int expirationMonth;
    private int expirationDay;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Creditcard(
        String number,        String owner,        int cvc,        int expirationMonth,        int expirationDay    ) {
        this.number = number;
        this.owner = owner;
        this.cvc = cvc;
        this.expirationMonth = expirationMonth;
        this.expirationDay = expirationDay;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
    public int getCvc() {
        return cvc;
    }

    public void setCvc(int cvc) {
        this.cvc = cvc;
    }
    public int getExpirationmonth() {
        return expirationMonth;
    }

    public void setExpirationmonth(int expirationMonth) {
        this.expirationMonth = expirationMonth;
    }
    public int getExpirationday() {
        return expirationDay;
    }

    public void setExpirationday(int expirationDay) {
        this.expirationDay = expirationDay;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}