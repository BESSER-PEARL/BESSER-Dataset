





import java.util.List;
import java.util.ArrayList;

public class Classes_Customers_Customer  {

    private String firstname;
    private String bookings;
    private String email;
    private String title;
    private String requests;
    private String ssid;
    private String lastname;
    private String phone;



    public Classes_Customers_Customer(
        String firstname,        String bookings,        String email,        String title,        String requests,        String ssid,        String lastname,        String phone    ) {
        this.firstname = firstname;
        this.bookings = bookings;
        this.email = email;
        this.title = title;
        this.requests = requests;
        this.ssid = ssid;
        this.lastname = lastname;
        this.phone = phone;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getBookings() {
        return bookings;
    }

    public void setBookings(String bookings) {
        this.bookings = bookings;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getRequests() {
        return requests;
    }

    public void setRequests(String requests) {
        this.requests = requests;
    }
    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}