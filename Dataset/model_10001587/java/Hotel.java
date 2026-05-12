





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String Hotel_Rent;
    private String Hotel_Type;
    private String Hotel_Name;
    private String Hotel_ID;
    private String Hotel_Address;





    private Booking booking;




    private Customer customer;




    private Room room;




    private Payment payment;




    private Admin admin;


    public Hotel(
        String Hotel_Rent,        String Hotel_Type,        String Hotel_Name,        String Hotel_ID,        String Hotel_Address    ) {
        this.Hotel_Rent = Hotel_Rent;
        this.Hotel_Type = Hotel_Type;
        this.Hotel_Name = Hotel_Name;
        this.Hotel_ID = Hotel_ID;
        this.Hotel_Address = Hotel_Address;
    }


    public String getHotel_rent() {
        return Hotel_Rent;
    }

    public void setHotel_rent(String Hotel_Rent) {
        this.Hotel_Rent = Hotel_Rent;
    }
    public String getHotel_type() {
        return Hotel_Type;
    }

    public void setHotel_type(String Hotel_Type) {
        this.Hotel_Type = Hotel_Type;
    }
    public String getHotel_name() {
        return Hotel_Name;
    }

    public void setHotel_name(String Hotel_Name) {
        this.Hotel_Name = Hotel_Name;
    }
    public String getHotel_id() {
        return Hotel_ID;
    }

    public void setHotel_id(String Hotel_ID) {
        this.Hotel_ID = Hotel_ID;
    }
    public String getHotel_address() {
        return Hotel_Address;
    }

    public void setHotel_address(String Hotel_Address) {
        this.Hotel_Address = Hotel_Address;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}