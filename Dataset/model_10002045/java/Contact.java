





import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private String name;
    private String email;
    private String address;
    private String phone;





    private Booking booking;


    public Contact(
        String name,        String email,        String address,        String phone    ) {
        this.name = name;
        this.email = email;
        this.address = address;
        this.phone = phone;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}