





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Creditcard  {

    private int expirationMonth;
    private String number;
    private int cvc;
    private int expirationYear;
    private String owner;





    private HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking;


    public HotelManagementClassDiagram_Creditcard(
        int expirationMonth,        String number,        int cvc,        int expirationYear,        String owner    ) {
        this.expirationMonth = expirationMonth;
        this.number = number;
        this.cvc = cvc;
        this.expirationYear = expirationYear;
        this.owner = owner;
    }


    public int getExpirationmonth() {
        return expirationMonth;
    }

    public void setExpirationmonth(int expirationMonth) {
        this.expirationMonth = expirationMonth;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public int getCvc() {
        return cvc;
    }

    public void setCvc(int cvc) {
        this.cvc = cvc;
    }
    public int getExpirationyear() {
        return expirationYear;
    }

    public void setExpirationyear(int expirationYear) {
        this.expirationYear = expirationYear;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public HotelManagementClassDiagram_Booking getHotelmanagementclassdiagram_booking() {
        return hotelmanagementclassdiagram_booking;
    }

    public void setHotelmanagementclassdiagram_booking(HotelManagementClassDiagram_Booking hotelmanagementclassdiagram_booking) {
        this.hotelmanagementclassdiagram_booking = hotelmanagementclassdiagram_booking;
    }

}