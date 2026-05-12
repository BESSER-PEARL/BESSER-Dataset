





import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private String email;
    private String phone;
    private String address;
    private String name;





    private Booking booking;


    public Contact(
        String email,        String phone,        String address,        String name    ) {
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}